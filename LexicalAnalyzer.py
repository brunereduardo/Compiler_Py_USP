from pprint import pprint

class LexicalAnalyzer():
    # Tabela de Palavras reservadas da linguagem
    reserved_words_table = {
        'program': 'simb_program',
        'var': 'simb_var',
        'integer': 'simb_tipo',
        'real': 'simb_tipo',
        'begin': 'simb_begin',
        'end': 'simb_end',
        'while': 'simb_while',
        'read': 'simb_read',
        'write': 'simb_write',
        'const': 'simb_const',
        'procedure': 'simb_procedure',
        'else': 'simb_else',
        'then': 'simb_then',
        'if': 'simb_if',
        'do': 'simb_do',
        'to': 'simb_to'
    }

    # Lista de Todos os Tokens
    token_table = []

    def __init__(self, input_file):
        self.input_file = input_file

        line_number = 0
        
        buffer = ''

        try:
            with open(input_file, 'r') as fp:
                for line in fp:
                    line = line.replace('\t', '')

                    line_number += 1
                    char_position = -1

                    begin_comment, end_comment = self._commentary(line, line_number, char_position)

                    for character in line:
                        char_position += 1

                        if char_position >= begin_comment and char_position <= end_comment:
                            continue
                        elif character == ' ' or character == '\n' or self._is_operator(character):
                            
                            if buffer != '':
                                output = self._number(buffer, line_number)

                                if output is None:
                                    if self._is_keyword(buffer):
                                        output = (f'{buffer}, {self.reserved_words_table[buffer]}')
                                    else:
                                        output = self._identifier(buffer, line_number)

                                self.token_table.append(output)

                            if self._is_operator(character):
                                ouput = self._operator(character, line, line_number, char_position)
                                if ouput is not None:
                                    self.token_table.append(ouput)

                            buffer = ''

                        else:
                            buffer += character        

        except FileNotFoundError:
            raise FileNotFoundError()

    def _commentary(self, line, line_number, char_position):
        begin = -1
        end = -1

        if '{' in line or '}' in line:
            state = 0
            for i in range(char_position, len(line)):
                char_tmp = line[i]

                if state == 0:
                    if char_tmp == '{':
                        state = 1
                        begin = i
                    elif char_tmp == '}':
                        state = 3

                elif state == 1:
                    if i >= len(line) - 1:
                        self.token_table.append(f'Comentario, ERRO: {line_number} - Fechar comentario')
                        end = begin
                    elif char_tmp == '}':
                        state = 2

                elif state == 2:
                    end = i
                    break

                elif state == 3:
                    self.token_table.append(f'Comentario, ERRO: {line_number} - Fechamento de comentario sem abertura')
                    end = begin = i - 1
 
        return begin, end


    def _operator(self, character, line, line_number, char_position):
        output = None

        if character == ')':    output = '), simb_fpar'
        elif character == '(':
            state = 0

            for i in range(char_position, len(line)):
                char_tmp = line[i]

                if state == 0:
                    if i >= len(line) - 1:
                        output = '(, simb_apar'  
                    elif char_tmp == '(':
                        state = 1
                    elif char_tmp == ')':
                        state = 4
                        
                elif state == 1:
                    if i >= len(line) - 1 and char_tmp != ')':
                        line_tmp = line.replace("\n", "")
                        output = f'{line_tmp}, ERRO: {line_number} - Identacao dos parenteses'
                    elif char_tmp == '(':
                        state = 2
                    elif char_tmp == ')':
                        state = 0

                elif state == 2:
                    if i >= len(line) - 1 and char_tmp != ')':
                        line_tmp = line.replace("\n", "")
                        output = f'{line_tmp}, ERRO: {line_number} - Identacao dos parenteses'
                    elif char_tmp == '(':
                        state = 3
                    elif char_tmp == ')':
                        state = 1

                elif state == 3:
                    if i >= len(line) - 1 and char_tmp != ')':
                        line_tmp = line.replace("\n", "")
                        output = f'{line_tmp}, ERRO: {line_number} - Identacao dos parenteses'
                    elif char_tmp == '(':
                        state = 5
                    elif char_tmp == ')':
                        state = 2

                elif state == 4:
                    line_tmp = line.replace("\n", "")
                    output = f'{line_tmp}, ERRO: {line_number} - Nao ha parenteses abertos'

                elif state == 5:
                    line_tmp = line.replace("\n", "")
                    output = f'{line_tmp}, ERRO: {line_number} - Maximo de parenteses atingido'
                    
        else:
            state = 0
            for i in range(char_position, len(line)):
                char_tmp = line[i]

                if state == 0:
                    if char_tmp == ':':
                        state = 1
                    elif char_tmp == '<':
                        state = 4
                    elif char_tmp == '=':
                        if line[i - 1] != ':':
                            state = 8
                        else:
                            state = -1
                    elif char_tmp == '>':
                        if line[i - 1] != '<':
                            state = 9
                        else:
                            state = -1
                    elif char_tmp == '+':
                        state = 12
                    elif char_tmp == '-':
                        state = 13
                    elif char_tmp == '*':
                        state = 14
                    elif char_tmp == '/':
                        state = 15
                    elif char_tmp == '.':
                        state = 16
                    elif char_tmp == ';':
                        state = 17
                    elif char_tmp == ',':
                        state = 18

                elif state == 1:
                    if char_tmp == '=':
                        state = 2
                    else:
                        state = 3
                        
                elif state == 2:
                    output = ':=, simb_atribuicao'

                elif state == 3:
                    output = ':, simb_dp'

                elif state == 4:
                    if char_tmp == '=':
                        state = 5
                    elif char_tmp == '>':
                        state = 6
                    else:
                        state = 7

                elif state == 5:
                    output = '<=, simb_menor_igual'

                elif state == 6:
                    output = '<>, simb_dif'

                elif state == 7:
                    output = '<, simb_menor'

                elif state == 8:
                    output = '=, simb_igual'

                elif state == 9:
                    if char_tmp == '=':
                        state = 10
                    else:
                        state = 11

                elif state == 10:
                    output = '>=, simb_maior_igual'

                elif state == 11:
                    output = '>, simb_maior'

                elif state == 12:
                    output = '+, simb_mais'

                elif state == 13:
                    output = '-, simb_menos'

                elif state == 14:
                    output = '*, simb_vezes'

                elif state == 15:
                    output = '/, simb_dividir'

                elif state == 16:
                    output = '., simb_ponto'

                elif state == 17:
                    output = ';, simb_ponto_virgula'

                elif state == 18:
                    output = ',, simb_virgula'

        return output
        

    def _is_operator(self, character):
        is_operator = False

        if character == ';':    is_operator = True
        elif character == ':':  is_operator = True
        elif character == '+':  is_operator = True
        elif character == '-':  is_operator = True
        elif character == '*':  is_operator = True
        elif character == '/':  is_operator = True
        elif character == '(':  is_operator = True
        elif character == ')':  is_operator = True
        elif character == '=':  is_operator = True
        elif character == ',':  is_operator = True
        elif character == '>':  is_operator = True
        elif character == '<':  is_operator = True
        elif character == '.':  is_operator = True


        return is_operator

    def _is_keyword(self, buffer):
        if self.reserved_words_table.get(buffer, None) is None:
            return False
        else:
            return True


    def _number(self, buffer, line_number):
        state = 0
        output = None
        size_count = 0

        for i in range(len(buffer)):
            character = buffer[i]

            if state == 0:
                if character >= '0' and character <= '9':
                    state = 2
                    size_count += 1

                    if len(buffer) == 1:
                        output = f'{buffer}, num_inteiro'

                elif character == '-' or character == '+':
                    state = 1
                elif character > ' ':
                    state = 5
      
            elif state == 1:
                if character >= '0' and character <= '9':
                    state = 2
                    size_count += 1
                else:
                    state = 6
                    
            elif state == 2:
                if size_count >= 32:
                    state = 4
                elif i >= len(buffer) - 1:
                    if character >= '0' and character <= '9':
                        output = f'{buffer}, num_inteiro'
                    else:
                        output = f'{buffer}, ERRO: {line_number}:{buffer} - Numero mal formado'
                    break
                elif character == '.':
                    state = 3
                elif character >= '0' and character <= '9':
                    size_count += 1
                else:
                    state = 6

            elif state == 3:
                if size_count >= 32:
                    state = 4
                elif i >= len(buffer) - 1:
                    if character >= '0' and character <= '9':
                        output = f'{buffer}, num_real'
                    else:
                        output = f'{buffer}, ERRO: {line_number}:{buffer} - Numero mal formado'
                    break
                elif character >= '0' and character <= '9':
                    size_count += 1
                else:
                    state = 6
                    
            elif state == 4:
                output = f'{buffer}, ERRO: {line_number}:{buffer} - Numero com excesso de tamanho'
                break

            elif state == 6:
                output = f'{buffer}, ERRO: {line_number}:{buffer} - Numero mal formado'
                break

        return output

    def _identifier(self, buffer, line_number):
        state = 0
        output = None
        size_count = 0

        for i in range(len(buffer)):
            char = buffer[i]

            if state == 0:
                if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
                    state = 1
                    size_count += 1

                    if len(buffer) == 1:
                        output = f'{buffer}, ident'

                elif char > ' ':
                    state = 2

            elif state == 1:
                if size_count >= 32:
                    state = 3
                elif i >= len(buffer) - 1:
                    output = f'{buffer}, ident'
                    break
                else:
                    size_count += 1

            elif state == 2:
                output = f'{buffer}, ERRO: {line_number}:{buffer} - Identificador com caracter invalido'
                break

            elif state == 3:
                output = f'{buffer}, ERRO: {line_number}:{buffer} - Identificador com excesso de tamanho'
                break

        return output


    def get_token_table(self):
        ''' 
            Retorna a tabela contendo todos os Tokens coletados pelo Analisador Lexico
        '''
        return self.token_table

    def get_token(self, position):
        ''' 
            Retorna Token que esta na posicao passada
        '''
        return self.token_table[position]

    def get_token_table_size(self):
        ''' 
            Retorna o tamanho da tabela de Tokens
        '''
        return len(self.token_table)