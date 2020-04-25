import sys

from LexicalAnalyzer import LexicalAnalyzer

def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('ERRO: Caminho para arquivo codigo fonte nao digitado.')

        with open(sys.argv[1], 'r') as fp:
            lexAnalyzer = LexicalAnalyzer(fp.readlines())
            lexAnalyzer.print_input()
        
    except FileNotFoundError:
        print('ERRO: Arquivo nao existe.')
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()