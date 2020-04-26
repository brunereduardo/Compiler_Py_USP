from pprint import pprint

class LexicalAnalyzer():
    reserved_symbols_table = {
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
        ';': 'simb_pv',
        ':': 'simb_dp',
        ':=': 'simb_atrib',
        '.': 'simb_p',
        '+': 'simb_mais',
        '-': 'simb_menos',
        '*': 'simb_mult',
        '/': 'simb_div',
        '+': 'simb_mais',
        '<': 'simb_menor',
        '>': 'simb_maior',
        '=': 'simb_igual'
    }

    symbols_table = []

    def __init__(self, input_file):
        self.input_file = input_file

        try:
            with open(input_file, 'r') as fp:
                buffer = ''
                while True:
                    c = fp.read(1)
                    if not c:
                        break
                    elif c is ' ' or c is '\n':
                        if self.isKeyword(buffer):
                            self.symbols_table.append(f'{buffer}, {self.reserved_symbols_table[buffer]}') 
                        elif self.isNumber(buffer):
                            self.symbols_table.append(f'{buffer}, num') 
                        elif self.isIdentifier(buffer):
                            self.symbols_table.append(f'{buffer}, ident')

                if self.isOperator(c):
                    buffer = c
                    c = fp.read(1)

                    if self.isOperator(c):
                        buffer = buffer + c
                        # pegar qual e o operador
                        buffer = ''
                    else:
                        self.symbols_table[buffer] = self.reserved_symbols_table[buffer]
                        buffer = ''
                else:
                    buffer = buffer + c



        except FileNotFoundError:
            print('Arquivo nao existe.')

                    
    def print_symbols_table(self):
        pprint(self.symbols_table)

    def isIdentifier(self, buffer):
        return False
    
    def isNumber(self, buffer):
        return False

    def isOperator(self, buffer):
        return False

    def isKeyword(self, buffer):
        return False