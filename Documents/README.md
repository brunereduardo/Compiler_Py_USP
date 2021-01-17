# Compiler_Py_USP

<img src="https://i.imgur.com/AB1jB3n.jpg" alt="banner" width="640" height="360">

## Project description
<p>Based on the P-- language grammar, available in .PDF in Documents, enriched with
the “for” command, we developed the lexical analyzer for this language. The designed automata (using the JFlap tool) and the source code corresponding to the designed automata (in the python programming language) were produced.</p>

<p>The lexical analyzer accepts a txt file with the program written in P-- and produces another txt file with the output, with one chain-token pair per line (indicating the lexical errors, if any). For more information, just search for the .PDF file in the folder <a href="https://github.com/brunereduardo/Compiler_Py_USP/tree/master/Documents">Documents.</a></p>

<p align="center">
<a href="#Descrição-do-Projeto">Project description</a> •  
<a href="#Pré-requisitos">Prerequisites</a> •	
<a href="#License">License</a> • 
<a href="#Author">Authors</a>
</p>

<h4 align="center"> 
	🚧  Construído durante a matéria de Teoria da Computação e Compiladores 🚧 Parte otimizadora do compilador faltante🚧
</h4>


### Prerequisites
To start venturing into the application you will need to install the following tools on your machine:
[Git](https://git-scm.com), [Node.js](https://nodejs.org/en/). In addition, an editor to work with the code as [VSCode](https://code.visualstudio.com/) will serve all purposes. To prepare the ground for the compilation, respecting the language used, *python*, the essential steps of the parser source codes-***syntacticAnalyzer.py***- and lexicon- ***LexicalAnalyzer.py***-, are basically: having the basic version, python 3 or higher, so that you can have access to an interpreter of the language used and, assuming you have access to a terminal or an IDE for Python, just run the compiler code- ***compiler.py***-so that it uses the lexical analyzer, the parser and the error storage- ***Errors.py***-, at the entry of the txt file to be analyzed. Finally, the compiler generates the output -output.txt- with the analyzes made by the lexicon and syntactic, in order to be used in future implementations. Below is an example of execution, in which you simply use the following command line:

### Rodando a Aplicação 🎲

```bash
# Clone this repository
$ git clone https://github.com/brunereduardo/Compiler_Py_USP

# Access the project folder on terminal/cmd
$ cd Compiler_Py_USP/Main Programs

# Run an application with the following command to inject any test case and compare the output with the saida.txt files
$ python3  compiler.py < Compiler_Py_USP/Tests/nome_do_arquivo_de_entrada_test.txt 

```

### 🚀 Technology

As seguintes ferramentas e bibliotecas foram usadas na construção do projeto:

- JFlap
- sys
- pprint 

### License

<p>This project is under the MIT license, for more information look for the file <a href = "https://github.com/brunereduardo/Compiler_Py_USP/blob/master/LICENSE">LICENSE</a></p>
 
### Authors
Implemented and designed with ❤️ by [Bruner Eduardo Augusto Albrecht](https://github.com/brunereduardo) | [Carlos R Dos Santos Junior](https://github.com/CarlosSantosJr) | [Clayton Miccas Junior](https://github.com/ClaytonMiccas) 👋🏽

