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
            with open(input_file, 'r', encoding="ISO-8859-1") as fp:
                for line in fp:
                    line = line.replace('\t', '')

                    line_number += 1
                    char_position = -1

                    begin_comment, end_comment = self._commentary(line, line_number, char_position)

                    if (begin_comment == -1 or end_comment == -1) and begin_comment != end_comment:
                        continue

                    for character in line:
                        char_position += 1

                        if char_position >= begin_comment and char_position <= end_comment:
                            continue
                        elif character == ' ' or character == '\n' or self._is_operator(character):
                            
                            if buffer != '':
                                output = self._number(buffer, line_number)

                                if output is None:
                                    if self._is_keyword(buffer):
                                        output = {'token': self.reserved_words_table[buffer], 'lexema': buffer, 'line': line_number}
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
                        self.token_table.append({'lexema': '{', 'error': 'Comentario nao fechado', 'line': line_number})

                    elif char_tmp == '}':
                        state = 2

                elif state == 2:
                    end = i
                    break

                elif state == 3:
                    self.token_table.append({'lexema': '}', 'error': 'Comentario fechado sem abertura', 'line': line_number})
 
        return begin, end


    def _operator(self, character, line, line_number, char_position):
        output = None

        if character == ')':    output = {'token': 'simb_fpar', 'lexema': ')', 'line': line_number}
        elif character == '(':  output = {'token': 'simb_par', 'lexema': '(', 'line': line_number}
            # state = 0

            # for i in range(char_position, len(line)):
            #     char_tmp = line[i]

            #     if state == 0:
            #         if i >= len(line) - 1:
            #             output = '(, simb_apar'  
            #         elif char_tmp == '(':
            #             state = 1
            #         elif char_tmp == ')':
            #             state = 4
                        
            #     elif state == 1:
            #         if i >= len(line) - 1 and char_tmp != ')':
            #             line_tmp = line.replace("\n", "")
            #             output = f'{line_tmp}, ERRO: {line_number} - Identacao dos parenteses'
            #         elif char_tmp == '(':
            #             state = 2
            #         elif char_tmp == ')':
            #             state = 0

            #     elif state == 2:
            #         if i >= len(line) - 1 and char_tmp != ')':
            #             line_tmp = line.replace("\n", "")
            #             output = f'{line_tmp}, ERRO: {line_number} - Identacao dos parenteses'
            #         elif char_tmp == '(':
            #             state = 3
            #         elif char_tmp == ')':
            #             state = 1

            #     elif state == 3:
            #         if i >= len(line) - 1 and char_tmp != ')':
            #             line_tmp = line.replace("\n", "")
            #             output = f'{line_tmp}, ERRO: {line_number} - Identacao dos parenteses'
            #         elif char_tmp == '(':
            #             state = 5
            #         elif char_tmp == ')':
            #             state = 2

            #     elif state == 4:
            #         line_tmp = line.replace("\n", "")
            #         output = f'{line_tmp}, ERRO: {line_number} - Nao ha parenteses abertos'

            #     elif state == 5:
            #         line_tmp = line.replace("\n", "")
            #         output = f'{line_tmp}, ERRO: {line_number} - Maximo de parenteses atingido'
                    
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
                    output = {'token': 'simb_atribuicao', 'lexema': ':=', 'line': line_number}

                elif state == 3:
                    output = {'token': 'simb_dp', 'lexema': ':', 'line': line_number}

                elif state == 4:
                    if char_tmp == '=':
                        state = 5
                    elif char_tmp == '>':
                        state = 6
                    else:
                        state = 7

                elif state == 5:
                    output = {'token': 'simb_menor_igual', 'lexema': '<=', 'line': line_number}

                elif state == 6:
                    output = {'token': 'simb_dif', 'lexema': '<>', 'line': line_number}

                elif state == 7:
                    output = {'token': 'simb_menor', 'lexema': '<', 'line': line_number}

                elif state == 8:
                    output = {'token': 'simb_igual', 'lexema': '=', 'line': line_number}

                elif state == 9:
                    if char_tmp == '=':
                        state = 10
                    else:
                        state = 11

                elif state == 10:
                    output = {'token': 'simb_maior_igual', 'lexema': '>=', 'line': line_number}

                elif state == 11:
                    output = {'token': 'simb_maior', 'lexema': '>', 'line': line_number}

                elif state == 12:
                    output = {'token': 'simb_mais', 'lexema': '+', 'line': line_number}

                elif state == 13:
                    output = {'token': 'simb_menos', 'lexema': '-', 'line': line_number}

                elif state == 14:
                    output = {'token': 'simb_vezes', 'lexema': '*', 'line': line_number}

                elif state == 15:
                    output = {'token': 'simb_dividir', 'lexema': '/', 'line': line_number}

                elif state == 16:
                    output = {'token': 'simb_ponto', 'lexema': '.', 'line': line_number}

                elif state == 17:
                    output = {'token': 'simb_ponto_virgula', 'lexema': ';', 'line': line_number}

                elif state == 18:
                    output = {'token': 'simb_virgula', 'lexema': ',', 'line': line_number}

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
                        output = {'token': 'num_inteiro', 'lexema': buffer, 'line': line_number}

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
                        output = {'token': 'num_inteiro', 'lexema': buffer, 'line': line_number}
                    else:
                        output = {'lexema': buffer, 'error': 'Numero mal formado', 'line': line_number}
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
                        output = {'token': 'num_real', 'lexema': buffer, 'line': line_number}
                    else:
                        output = {'lexema': buffer, 'error': 'Numero mal formado', 'line': line_number}
                    break
                elif character >= '0' and character <= '9':
                    size_count += 1
                else:
                    state = 6
                    
            elif state == 4:
                output = {'lexema': buffer, 'error': 'Numero com excesso de tamanho', 'line': line_number}
                break

            elif state == 6:
                output = {'lexema': buffer, 'error': 'Numero mal formado', 'line': line_number}
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
                        output = {'token': 'ident', 'lexema': buffer, 'line': line_number}

                elif char > ' ':
                    if len(buffer) == 1:
                        output = {'lexema': buffer, 'error': 'Identificador com caracter invalido', 'line': line_number}
                    state = 2

            elif state == 1:
                if size_count >= 32:
                    state = 3
                elif i >= len(buffer) - 1:
                    output = {'token': 'ident', 'lexema': buffer, 'line': line_number}
                    break
                else:
                    size_count += 1

            elif state == 2:
                output = {'lexema': buffer, 'error': 'Identificador com caracter invalido', 'line': line_number}
                break

            elif state == 3:
                output = {'lexema': buffer, 'error': 'Identificador com excesso de tamanho', 'line': line_number}
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