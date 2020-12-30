import sys

from LexicalAnalyzer import LexicalAnalyzer
from SyntacticAnalyzer import SyntacticAnalyzer
from Errors import Errors

from pprint import pprint


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('ERRO: Caminho para arquivo codigo fonte nao digitado.')

        errors = Errors()

        lexAnalyzer = LexicalAnalyzer(sys.argv[1], errors)
        SyntacticAnalyzer(lexAnalyzer, errors)

        with open('saida.txt', 'w') as fp:
            if errors.has_errors:
                sorted_dict = sorted(errors.errors.keys())
                for key in sorted_dict:
                    for item in errors.errors[key]:
                        fp.write(item + '\n')
            else:
                fp.write('Sucesso!')
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()