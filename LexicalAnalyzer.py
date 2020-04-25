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

    symbols_table = {}

    def __init__(self, input_string):
        self.input_string = input_string
    
    def print_input(self):
        print(self.input_string)
        