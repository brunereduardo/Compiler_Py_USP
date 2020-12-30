# Compiler_Py_USP

<p>Based on the P-- language grammar, available in .PDF in Documents, enriched with
the “for” command, we developed the lexical analyzer for this language. The designed automata (using the JFlap tool) and the source code corresponding to the designed automata (in the python programming language) were produced.</p>

<p>The lexical analyzer accepts a txt file with the program written in P-- and produces another txt file with the output, with one chain-token pair per line (indicating the lexical errors, if any). For more information, just search for the .PDF file in the folder <a href="https://github.com/brunereduardo/Compiler_Py_USP/tree/master/Documents">Documents.</a></p>

## Instructions for Compiling the Source Code
To prepare the ground for the compilation, respecting the language used, *python*, the essential steps of the parser source codes-***syntacticAnalyzer.py***- and lexicon- ***LexicalAnalyzer.py***-, are basically: having the basic version, python 3 or higher, so that you can have access to an interpreter of the language used and, assuming you have access to a terminal or an IDE for Python, just run the compiler code- ***compiler.py***-so that it uses the lexical analyzer, the parser and the error storage- ***Errors.py***-, at the entry of the txt file to be analyzed. Finally, the compiler generates the output -output.txt- with the analyzes made by the lexicon and syntactic, in order to be used in future implementations. Below is an example of execution, in which you simply use the following command line:
```
python3  compiler.py path/input_file_name.txt 
```
<p><b>The project belongs to the following developers:</b></p><a href="https://github.com/brunereduardo">Bruner Eduardo Augusto Albrecht</a><br></br>
<a href="https://github.com/CarlosSantosJr">Carlos R Dos Santos Junior</a><br></br>
<a href="https://github.com/ClaytonMiccas">Clayton Miccas Junior</a>

