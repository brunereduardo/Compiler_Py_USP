import sys

from LexicalAnalyzer import LexicalAnalyzer

def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('ERRO: Caminho para arquivo codigo fonte nao digitado.')

        lexAnalyzer = LexicalAnalyzer(sys.argv)
        lexAnalyzer.print_symbols_table()
        
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()