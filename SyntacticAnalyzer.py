from LexicalAnalyzer import LexicalAnalyzer
from Errors import Errors

class SyntacticAnalyzer() :
    primeiro_seguidor = {
        'programa': {'primeiro': ['simb_program'], 'seguidor': []},
    }

    def __init__(self, lexical: LexicalAnalyzer, errors: Errors):
        self.lexical = lexical
        self.errors = errors

        self.posicao_token = 0
        self.token_atual = self.get_next_token()

        try:
            self.programa([])
        except:
            pass


    def get_next_token(self):
        token = self.lexical.get_token(self.posicao_token)
        self.posicao_token += 1
        return token


    def panic_mode(self, seguidores_imediatos = [], seguidores_pai = [], tokens_extras = []) -> bool:
        try:
            while True:
                print(self.token_atual)
                if self.token_atual['token'] in seguidores_imediatos:
                    return True
                
                if self.token_atual['token'] in seguidores_pai:
                    return False

                if self.token_atual['token'] in tokens_extras:
                    return True

                self.token_atual = self.get_next_token()
        except IndexError:
            raise Exception('Programa Terminou')


    def programa(self, seguidores_pai):
        if self.token_atual['token'] == 'simb_program':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'program esperado')
            self.panic_mode(['ident'], seguidores_pai)

        if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
            self.panic_mode(['simb_ponto_virgula'], seguidores_pai)
            
        if self.token_atual['token'] == 'simb_ponto_virgula':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'Ponto e virugla esperado')
            self.panic_mode(['simb_const', 'simb_var', 'simb_procedure'], seguidores_pai)

        self.dc(['begin'] + seguidores_pai)

        if self.token_atual['token'] == 'simb_begin':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'begin esperado')
            self.panic_mode(['simb_read', 'simb_write', 'simb_for', 'simb_while', 'simb_if', 'ident', 'simb_begin'], seguidores_pai)

        self.comandos(['end'] + seguidores_pai)

        if self.token_atual['token'] == 'simb_end':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'end esperado')
            self.panic_mode(['simb_ponto'], seguidores_pai)

        if self.token_atual['token'] == 'simb_ponto':    return
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '. esperado')


    def dc(self, seguidores_pai):
        self.dc_c(['simb_var'] + seguidores_pai)

        self.dc_v(['simb_procedure'] + seguidores_pai)

        self.dc_p(seguidores_pai)


    def dc_c(self, seguidores_pai):
        if self.token_atual['token'] == 'simb_const':    self.token_atual = self.get_next_token()
        else:
            return

        if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
            if self.panic_mode(['simb_const'], seguidores_pai):
                self.dc_c(seguidores_pai)
            else:
                return

        if self.token_atual['token'] == 'simb_igual':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '= esperado')
            self.panic_mode(['num_inteiro', 'num_real'], seguidores_pai)

        if self.token_atual['token'] == 'num_inteiro' or self.token_atual['token'] == 'num_real':    
            self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'Numero esperado')
            self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

        if self.token_atual['token'] == 'simb_ponto_virgula':    
            self.token_atual = self.get_next_token()
            self.dc_c(seguidores_pai)
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')
            if self.panic_mode([], seguidores_pai, ['simb_const']):
                self.dc_c(seguidores_pai)
    

    def dc_v(self, seguidores_pai):
        if self.token_atual['token'] == 'simb_var':    self.token_atual = self.get_next_token()
        else:
            return

        if self.token_atual['token'] == 'ident':
            self.token_atual = self.get_next_token()
            while (self.token_atual['token'] == 'simb_virgula'):
                self.token_atual = self.get_next_token()
                if self.token_atual['token'] == 'ident':   self.token_atual = self.get_next_token()
                else:
                    break
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
            self.panic_mode(seguidores_pai)
            return

        if self.token_atual['token'] == 'simb_dp':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], ': esperado')
            self.panic_mode(['simb_tipo'], seguidores_pai)

        if self.token_atual['token'] == 'simb_tipo':
            self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'Tipo de variavel esperado')
            self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

        if self.token_atual['token'] == 'simb_ponto_virgula':    
            self.token_atual = self.get_next_token()
            self.dc_v(seguidores_pai)
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')
            if self.panic_mode([], seguidores_pai, ['simb_const']):
                self.dc_v(seguidores_pai)


    def dc_p(self, seguidores_pai):
        parenteses = False

        if self.token_atual['token'] == 'simb_procedure':    self.token_atual = self.get_next_token()
        else:
            return

        if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
            self.panic_mode(seguidores_pai)
            return

        if self.token_atual['token'] == 'simb_par':    
            self.token_atual = self.get_next_token()
            parenteses = True
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '( esperado')
            self.panic_mode(['ident', 'simb_ponto_virgula'], seguidores_pai)

        while self.token_atual['token'] == 'ident':
            self.variaveis(['simb_dp'] + seguidores_pai)

            if self.token_atual['token'] == 'simb_dp':    self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], ': esperado')
                self.panic_mode(['simb_tipo'], seguidores_pai)

            if self.token_atual['token'] == 'simb_tipo':    self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], 'Tipo de variavel esperado')
                self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

            if self.token_atual['token'] == 'simb_ponto_virgula':    self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')
                self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

        if self.token_atual['token'] == 'simb_fpar' and parenteses == True:
            self.token_atual = self.get_next_token()
        else:
            if parenteses == True:
                self.errors.add_error('sintatico', self.token_atual['line'], ') esperado')
                self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

        if self.token_atual['token'] == 'simb_ponto_virgula':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')
            self.panic_mode(['simb_begin', 'simb_var'], seguidores_pai)

        self.corpo_p(seguidores_pai)


    def variaveis(self, seguidores_pai):
        if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
            self.panic_mode([], seguidores_pai)
            return

        while self.token_atual['token'] == 'simb_virgula':
            if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
            else:
                self.panic_mode([], seguidores_pai)
                return


    def corpo_p(self, seguidores_pai):
        self.dc_v(['begin'] + seguidores_pai)

        if self.token_atual['token'] == 'simb_begin':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'begin esperado')
            self.panic_mode(['simb_read', 'simb_write', 'simb_for', 'simb_while', 'simb_if', 'ident', 'simb_begin'], seguidores_pai)

        self.comandos(['simb_end'] + seguidores_pai)

        if self.token_atual['token'] == 'simb_end':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'end esperado')
            self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

        if self.token_atual['token'] == 'simb_ponto_virgula':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')


    def argumentos(self, seguidores_pai):
        if self.token_atual['token'] == 'simb_par': self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '( esperado')
            self.panic_mode(['ident'], seguidores_pai)

        while self.token_atual['token'] == 'ident':
            self.token_atual = self.get_next_token()

            if self.token_atual['token'] == 'simb_ponto_virgula': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')
                self.panic_mode(['ident', [')']], seguidores_pai)
        
        if self.token_atual['token'] == 'simb_fpar': self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], ') esperado')

    
    def relacao(self, seguidores_pai):
        if self.token_atual['token'] == 'simb_igual':   self.token_atual = self.get_next_token()
        elif self.token_atual['token'] == 'simb_diff':   self.token_atual = self.get_next_token()
        elif self.token_atual['token'] == 'simb_maior_igual':   self.token_atual = self.get_next_token()
        elif self.token_atual['token'] == 'simb_menor_igual':   self.token_atual = self.get_next_token()
        elif self.token_atual['token'] == 'simb_maior':   self.token_atual = self.get_next_token()
        elif self.token_atual['token'] == 'simb_menor':   self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'operador relacional esperado')


    def condicao(self, seguidores_pai):
        self.expressao(['simb_igual', 'simb_diff', 'simb_maior_igual', 'simb_menor_igual', 'simb_maior', 'simb_menor'] + seguidores_pai)
        self.relacao(['simb_mais', 'simb_menos', 'ident', 'num_inteiro', 'num_real', 'simb_par'] + seguidores_pai)
        self.expressao(seguidores_pai)


    def comandos(self, seguidores_pai):
        while self.cmd([';'] + seguidores_pai):
            if self.token_atual['token'] == 'simb_ponto_virgula':    self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], '; esperado')
                self.panic_mode(['simb_read', 'simb_write', 'simb_for', 'simb_while', 'simb_if', 'ident', 'simb_begin'], seguidores_pai)


    def expressao(self, seguidores_pai):
        self.panic_mode([], seguidores_pai)
        primeiro = ['simb_mais', 'simb_menos', 'ident', 'num_real', 'num_inteiro', 'simb_par']

        if self.token_atual['token'] not in primeiro:
            self.errors.add_error('sintatico', self.token_atual['line'], 'Expressao esperada')
            self.panic_mode([], seguidores_pai)
            return
        
        while self.token_atual['token'] in primeiro:
            if self.token_atual['token'] == 'simb_mais' or self.token_atual['token'] == 'simb_menos':
                self.token_atual = self.get_next_token()

            if self.token_atual['token'] == 'ident' or self.token_atual['token'] == 'num_inteiro' or self.token_atual['token'] == 'num_real':
                self.token_atual = self.get_next_token()

                

    
    def cmd(self, seguidores_pai):
        if self.token_atual['token'] == 'simb_read' or self.token_atual['token'] == 'simb_write':
            self.token_atual = self.get_next_token()

            if self.token_atual['token'] == 'simb_par': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], '( esperado')
                self.panic_mode(['ident'], seguidores_pai)

            self.variaveis([')'] + seguidores_pai)

            if self.token_atual['token'] == 'simb_fpar': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], ') esperado')

        elif self.token_atual['token'] == 'simb_for':
            self.token_atual = self.get_next_token()

            if self.token_atual['token'] == 'ident': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
                self.panic_mode(['simb_atribuicao'], seguidores_pai)

            if self.token_atual['token'] == 'simb_atribuicao': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], ':= esperado')
                self.panic_mode(['simb_igual', 'simb_dif', 'simb_maior_igual', 'simb_menor_igual', 'simb_maior', 'simb_menor'], seguidores_pai)

            self.relacao(['simb_to'] + seguidores_pai)

            if self.token_atual['token'] == 'simb_to': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], 'to esperado')
                self.panic_mode(['simb_igual', 'simb_dif', 'simb_maior_igual', 'simb_menor_igual', 'simb_maior', 'simb_menor'], seguidores_pai)

            self.relacao(['simb_to'] + seguidores_pai)

        elif self.token_atual['token'] == 'simb_while':
            self.token_atual = self.get_next_token()

            if self.token_atual['token'] == 'simb_par': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], '( esperado')
                self.panic_mode(['simb_mais', 'simb_menos', 'ident', 'num_inteiro', 'num_real', 'simb_par'], seguidores_pai)

            self.condicao([')'] + seguidores_pai)

            if self.token_atual['token'] == 'simb_fpar': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], ') esperado')
                self.panic_mode(['simb_do'], seguidores_pai)

            if self.token_atual['token'] == 'simb_do': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], 'to esperado')

        elif self.token_atual['token'] == 'simb_if':
            self.token_atual = self.get_next_token()

            self.condicao(['simb_then'] + seguidores_pai)

            if self.token_atual['token'] == 'simb_else': self.token_atual = self.get_next_token()

        elif self.token_atual['token'] == 'ident':
            self.token_atual = self.get_next_token()

            if self.token_atual['token'] == 'simb_atribuicao':  
                self.token_atual = self.get_next_token()
                self.relacao(seguidores_pai)
            else:
                self.argumentos(seguidores_pai)

        elif self.token_atual['token'] == 'simb_begin':
            self.token_atual = self.get_next_token()

            self.comandos(['simb_end'] + seguidores_pai)

            if self.token_atual['token'] == 'simb_end': self.token_atual = self.get_next_token()
            else:
                self.errors.add_error('sintatico', self.token_atual['line'], 'end esperado')

        else:   return False

        return True