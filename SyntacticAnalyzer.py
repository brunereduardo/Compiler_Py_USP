from LexicalAnalyzer import LexicalAnalyzer
from PanicMode import PanicMode

class SyntacticAnalyzer() :
    def __init__(self, lexical: LexicalAnalyzer, panic_mode: PanicMode):
        self.lexical = lexical

        self.token_number = 0


    def get_next_token(self):
        token = self.lexical.get_token(self.token_number)
        self.token_number += 1
        return token


    def programa(self):
        token = self.get_next_token()

        if token['token'] == 'simb_program':    token = self.get_next_token()
        # else:   ERRO

        if token['token'] == 'ident':    token = self.get_next_token()
        # else:   ERRO 
            
        if token['token'] != 'simb_ponto_virgula':
            # ERRO

        # CORPO

        if token['token'] != 'simb_ponto':
            # ERRO


    def corpo(self):
        # DC

        token = self.get_next_token()

        if token['token'] != 'simb_begin':
            # ERRO

        # COMANDOS

        token = self.get_next_token()

        if token['token'] != 'simb_end':
            # ERRO


    # print("Alanizador sintatico", '\n')
    # primeiro usaremos o exemplo do professor
    '''
    def __init__(self, uma_copida_do_lexicalAnalyser?):
        self.atr1 = uma_copida_do_lexicalAnalyser? 

    def obter_simbolo(LexicalAnalyzer) : 
        return lexAnalyzer.get_token_table()

    def program(simb):
        a
    
    def cmd(simb):
        b
    
    def dc_V(simb):

        if(simb != var):
            exit();
        
        if (simb == var) : 
            simb = obter_simbolo()
        
        elif : 
            raise "ERRO"
        
        if (simb == ident) : 
            simb = obter_simbolo();
            while (simb == simb_v) :
                simb = obter_simbolo()
                if (simb == ident) :
                    simb = obter_simbolo()
                elif : 
                    raise "ERRO"
        elif:
            raise "ERRO"

        if (simb == simb_dp) : 
            simb = obter_simbolo();
        
        elif :
            raise "ERRO"

        if ((simb == real) or (simb == integer)) : 
            simb = obter_simbolo();
        
        elif :
            raise "ERRO"

        if (simb == simb_pv) :
            simb = obter_simbolo();
        
        elif :
            raise "ERRO"

        if ((terminou_cadeia == FALSE) and (simb == var)) :
            dc_v();

    def begin():   
        #chamada do léxico para obtenção dos simbolos 
        simb = obter_simbolo(LexicalAnalyzer);
        
        #chama o procedimento inicial program
        #program(simb)

        if(item in lexAnalyzer.get_token_table() = fim) :
            printf("sucesso", "\n")
        else() :
            print("ERRO")
            raise ("joga pra cima o erro para ser tratado pelo modo pânico")

    '''

