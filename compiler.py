import sys
from pprint import pprint

from LexicalAnalyzer import LexicalAnalyzer
<<<<<<< HEAD
from SyntacticAnalyzer import SyntacticAnalyzer
=======
from SyntacticAnalyzer import SyntacticAnalyzer
>>>>>>> 58cf3efa998706f7206287c426f876dc796ad480

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
<<<<<<< HEAD
        synAnalyzer = SyntacticAnalyzer(lexAnalyzer)
=======
        synAnalyzer = SyntacticAnalyzer(lexAnalyzer)
>>>>>>> 58cf3efa998706f7206287c426f876dc796ad480
        with open('saida.txt', 'w') as fp:
            for item in lexAnalyzer.get_token_table(): # aqui precisa ser sincornizada a escrita com o sintático.
                fp.write(item + '\n')
                #fp.write(itemS + '\n')
            print('Sucesso!', '\n')
    except FileNotFoundError:
        print('ERRO: Arquivo nao existe.')
    except PanicMode:
        print("Entrou no modo panico") # talvez seja melhor a definição do modo panico estar no sytatic e não no compilador 
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()