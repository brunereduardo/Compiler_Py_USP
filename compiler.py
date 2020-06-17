import sys
from pprint import pprint

from LexicalAnalyzer import LexicalAnalyzer
# from SyntacticAnalyzer import SyntacticAnalyzer

class PanicMode(Exception) :
    #colocar as funções aqui
    # e preciso voltar para o tolken anterior
    def display(self):
        print("TESTE", "\n")


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('ERRO: Caminho para arquivo codigo fonte nao digitado.')

        lexAnalyzer = LexicalAnalyzer(sys.argv[1])
        # synAnalyzer = SyntacticAnalyzer(lexAnalyzer)
        with open('saida.txt', 'w') as fp:
            for item in lexAnalyzer.get_token_table(): # aqui precisa ser sincornizada a escrita com o sintático.
                fp.write(str(item) + '\n')
            print('Sucesso!', '\n')
    except FileNotFoundError:
        print('ERRO: Arquivo nao existe.')
    except PanicMode:
        print("Entrou no modo panico") # talvez seja melhor a definição do modo panico estar no sytatic e não no compilador 
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()