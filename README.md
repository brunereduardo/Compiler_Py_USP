# Instruções para Compilar o Codigo-Fonte
 Para preparar o terreno para a compilação, respeitando a linguagem utilizada, *python*, os  passos  essenciais dos códigos fonte dos analisadores sintático- ***syntacticAnalyzer.py*** - e léxico- ***LexicalAnalyzer.py*** -, são basicamente: ter a versão basica, python 3 ou superior, para que se possa ter acesso a um interpretador da linguagem utilizada e, assumindo que se tenha acesso a um terminal ou uma IDE para Python, basta rodar o código do compilador - ***compiler.py*** -para que o mesmo utilize o analisador léxico, o analisador sintático e o armazenamento de erros - ***Erros.py***-, na entrada do arquivo txt a ser analisado. Por fim, o compilador gera a saida - saida.txt  -com as análises feitas pelo léxico e sintático, com o intuito de ser utilizado em futuras implementações. Abaixo temos um exemplo de execução, no qual basta fazer o uso da linha de comando a seguir:
```
python3  compiler.py caminho/nome_do_arquivo_de_entrada.txt 
```
@brunereduardo, @ClaytonMiccas e @CarlosSantosJr
