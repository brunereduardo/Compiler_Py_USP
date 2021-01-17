# Compiler_Py_USP


<img src="https://i.imgur.com/AB1jB3n.jpg" alt="banner" width="640" height="360">

#### [English version here!](https://github.com/brunereduardo/Compiler_Py_USP/blob/master/Documents/README.md=200x200)

## Descrição do Projeto
<p>Com base na gramática da linguagem P--, disponível nos .PDF em Documents, enriquecida com
o comando “for”, desenvolvemos o analisador léxico para esta linguagem. Foram produzidos os autômatos projetados (usando a ferramenta JFlap) e o código-fonte correspondente aos autômatos projetados (na linguagem de programação python).</p>

<p>O analisador léxico aceita um arquivo txt com o programa escrito em P-- e produz um outro arquivo txt com a saída, com um par cadeia-token por linha (indicando os
erros léxicos, se houver). Para mais informações, basta procurar pelo arquivo .PDF na pasta <a href="https://github.com/brunereduardo/Compiler_Py_USP/tree/master/Documents">Documents.</a></p>

<p align="center">
<a href="#Descrição-do-Projeto">Descrição do Projeto</a> •  
<a href="#Pré-requisitos">Pré-requisitos</a> •	
<a href="#Licença">Licença</a> • 
<a href="#Autores">Autores</a>
</p>

<h4 align="center"> 
	🚧  Construído durante a matéria de Teoria da Computação e Compiladores 🚧  são necessárias para escalar o código 🚧
</h4>

### Pré-requisitos

Para começar a se aventurar pelo projeto você vai precisar instalar em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com) e um editor para trabalhar com o código, como [VSCode](https://code.visualstudio.com/), que servirá para todos os propósitos. Para preparar o terreno para a compilação, respeitando a linguagem utilizada, *python*, os  passos  essenciais dos códigos fonte dos analisadores sintático- ***syntacticAnalyzer.py*** - e léxico- ***LexicalAnalyzer.py*** -, são basicamente: ter a versão basica, python 3 ou superior, para que se possa ter acesso a um interpretador da linguagem utilizada e, assumindo que se tenha acesso a um terminal ou uma IDE para Python, basta rodar o código do compilador - ***compiler.py*** -para que o mesmo utilize o analisador léxico, o analisador sintático e o armazenamento de erros - ***Erros.py***-, na entrada do arquivo txt a ser analisado. Por fim, o compilador gera a saida - saida.txt  -com as análises feitas pelo léxico e sintático, com o intuito de ser utilizado em futuras implementações.


### Rodando a Aplicação 🎲

```bash
# Clone este repositório
$ git clone https://github.com/brunereduardo/Compiler_Py_USP

# Acesse a pasta do projeto no terminal/cmd
$ cd Compiler_Py_USP/Main Programs

# Execute a aplicação com o seguinte comando para injetar qualquer caso de test e compare a saída com os arquivos .out
$ python3  compiler.py < Compiler_Py_USP/Tests/nome_do_arquivo_de_entrada_test.txt 

```

### 🚀 Tecnologias

As seguintes ferramentas e bibliotecas foram usadas na construção do projeto:

- JFlap
- sys
- pprint 

### Licença

<p>Este projeto está sob a licença MIT, para mais informações procurar pelo arquivo <a href = "https://github.com/brunereduardo/Compiler_Py_USP/blob/master/LICENSE">LICENSE</a></p>
 
### Autores
Implementado e criado com ❤️ por [Bruner Eduardo Augusto Albrecht](https://github.com/brunereduardo) | [Carlos R Dos Santos Junior](https://github.com/CarlosSantosJr) | [Clayton Miccas Junior](https://github.com/ClaytonMiccas) 👋🏽
