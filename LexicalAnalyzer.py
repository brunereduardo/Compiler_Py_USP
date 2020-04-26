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
        'do': 'simb_do'
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
                    for character in line:
                        char_position += 1
                        if character == ' ' or character == '\n' or self._is_operator(character):
                            
                            output = self._number(buffer, line_number)

                            if output is None:
                                if self._is_keyword(buffer):
                                    output = (f'{buffer}, {self.reserved_words_table[buffer]}')
                                else:
                                    output = self._identifier(buffer, line_number)

                            if output is not None:
                                self.token_table.append(output)

                            if self._is_operator(character):
                                # self.token_table.append(self._operator(character, line, line_number, char_position))
                                self.token_table.append('------------------------')

                            buffer = ''

                        else:
                            buffer += character        

        except FileNotFoundError:
            raise FileNotFoundError()
        

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
        elif character == '{':  is_operator = True
        elif character == '}':  is_operator = True
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
                    output = f'{buffer}, num_inteiro'
                    break
                elif character == '.':
                    state = 3
                elif character < '0' or character > '9':
                    state = 6

            elif state == 3:
                if size_count >= 32:
                    state = 4
                elif i >= len(buffer) - 1:
                    output = f'{buffer}, num_real'
                    break
                elif character < '0' or character > '9':
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