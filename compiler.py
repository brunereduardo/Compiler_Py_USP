import sys

from LexicalAnalyzer import LexicalAnalyzer
# from SyntacticAnalyzer import SyntacticAnalyzer
from PanicMode import PanicMode


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('ERRO: Caminho para arquivo codigo fonte nao digitado.')

        panic_mode = PanicMode()

        lexAnalyzer = LexicalAnalyzer(sys.argv[1], panic_mode)
        # synAnalyzer = SyntacticAnalyzer(lexAnalyzer, panic_mode)

        # with open('saida.txt', 'w') as fp:
        if panic_mode.panic_has_errors():
            print(panic_mode.errors)
        else:
            print('Sucesso!')
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()