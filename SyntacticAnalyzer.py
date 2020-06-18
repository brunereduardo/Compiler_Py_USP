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

        # self.dc(['begin'] + seguidores_pai)

        if self.token_atual['token'] == 'simb_begin':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'begin esperado')
            # self.panic_mode(PRIMEIRO DE COMANDOS, seguidores_pai)

        # self.comandos(['end'] + seguidores_pai)

        if self.token_atual['token'] == 'simb_end':    self.token_atual = self.get_next_token()
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], 'end esperado')
            self.panic_mode(['simb_ponto'], seguidores_pai)

        if self.token_atual['token'] == 'simb_ponto':    return
        else:
            self.errors.add_error('sintatico', self.token_atual['line'], '. esperado')


    # def dc(self, seguidores_pai):
    #     self.dc_c(['simb_var'] + seguidores_pai)

    #     self.dc_v(['simb_procedure'] + seguidores_pai)

    #     self.dc_p(seguidores_pai)

    # def dc_c(self, seguidores_pai):
    #     if self.token_atual['token'] == 'simb_const':    self.token_atual = self.get_next_token()
    #     else:
    #         return

    #     if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
    #         self.panic_mode(seguidores_pai)
    #         return

    #     if self.token_atual['token'] == 'simb_igual':    self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], '= esperado')
    #         self.panic_mode(['num_inteiro', 'num_real'], seguidores_pai)

    #     if self.token_atual['token'] == 'num_inteiro' or self.token_atual['token'] == 'num_real':    
    #         self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], 'Numero esperado')
    #         self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

    #     if self.token_atual['token'] == 'simb_ponto_virgula' or self.token_atual['token'] == 'num_real':    
    #         self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
    #         if self.panic_mode([], seguidores_pai, ['simb_const']):
    #             dc_c(seguidores_pai)
    

    # def dc_v(self, seguidores_pai):
    #     if self.token_atual['token'] == 'simb_var':    self.token_atual = self.get_next_token()
    #     else:
    #         return

    #     if self.token_atual['token'] == 'ident':    self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
    #         self.panic_mode(seguidores_pai)
    #         return

    #     if self.token_atual['token'] == 'simb_igual':    self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], '= esperado')
    #         self.panic_mode(['num_inteiro', 'num_real'], seguidores_pai)

    #     if self.token_atual['token'] == 'num_inteiro' or self.token_atual['token'] == 'num_real':    
    #         self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], 'Numero esperado')
    #         self.panic_mode(['simb_ponto_virgula'], seguidores_pai)

    #     if self.token_atual['token'] == 'simb_ponto_virgula' or self.token_atual['token'] == 'num_real':    
    #         self.token_atual = self.get_next_token()
    #     else:
    #         self.errors.add_error('sintatico', self.token_atual['line'], 'identificador esperado')
    #         if self.panic_mode([], seguidores_pai, ['simb_const']):
    #             dc_c(seguidores_pai)