#grafo[13]
#def arg():

#grafo[12]
def realcao(lexico):
    if (lexico.getSimbolo() == "="):
        return lexico.getSimboloNext()
    if (lexico.getSimbolo() == "<>"):
        return lexico.getSimboloNext()
    if (lexico.getSimbolo() == ">="):
        return lexico.getSimboloNext()
    if (lexico.getSimbolo() == "<="):
        return lexico.getSimboloNext()
    if (lexico.getSimbolo() == ">"):
        return lexico.getSimboloNext()
    if (lexico.getSimbolo() == "<"):
        return lexico.getSimboloNext()


#grafo[11]
#def exp():

#grafo[10]
def condicao(lexico):
    simb = exp(lexico.getSimbolo())
    simb = relação(simb)
    simb = exp(simb)
    return simb

#grafo[9]
#def cmd():

#grafo[8]
def comandos(lexico):
    if (lexico.getSimbolo() == "cmd"):
        simb = lexico.getSimboloNext()
        simb = cmd(simb)
        if (simb == ";"):
            simb = lexico.getSimboloNext()
            if (simb == "comandos"):
                simb = lexico.getSimboloNext()
                simb = comandos(simb)
                return simb
            else:
                return simb # deu bom 
        else:
            print("erro!-> chama o pânico")
    else:
        print("erro!-> chama o pânico") # ainda nao sei se o certo não deveira ser return lexico

#grafo[7]
def corpo_p(lexico):
    if (lexico.getSimbolo() == "dc_v"):
        simb = lexico.getSimboloNext()
        simb = dc_v(simb)
        if (simb == "begin"):
            simb = lexico.getSimboloNext()
            if (simb == "comandos"):
                simb = lexico.getSimboloNext()
                simb = comandos(simb)
                if (simb == "end"):
                    simb = lexico.getSimboloNext()
                    if (simb == ";"):
                        return simb
                    else:
                        print("erro!-> chama o pânico")
                else:
                    print("erro!-> chama o pânico")
            else:
                print("erro!-> chama o pânico")
        else:
            print("erro!-> chama o pânico")
    else:
        print("erro!-> chama o pânico")

#grafo[6]
#def variaveis():

#grafo[5]
def dc_P(lexico):
    if (condition):
        pass
    else:
        pass

#grafo[4]
def dc_v(lexico):
    if ("var" == lexico.getSimbolo()):
        pass
    else:
        pass

#grafo[3]
def dc_c(lexico) :
    if("constant" == lexico.getSimbolo()) :
        simb = lexico.getSimboloNext();
        if( simb == "ident") :
            simb = lexico.getSimboloNext();
            if (simb == "="):
                simb = lexico.getSimboloNext();
                if (simb == "numero_int"):
                    simb = lexico.getSimboloNext();
                    if (simb == ";"):
                        simb = lexico.getSimboloNext();
                        if (simb == "dc_c"):
                            simb = dc_c(simb)
                            return simb
                        else:
                            return simb
                    else:
                        print("erro!-> chama o pânico")
                if (simb == "numero_real") :
                    simb = lexico.getSimboloNext();
                    if (simb == ";"):
                        simb = lexico.getSimboloNext();
                        if (simb == "dc_c"):
                            simb = dc_c(simb)
                            return simb
                        else:
                            return simb
                    else:
                        print("erro!-> chama o pânico")
                else :
                    print("erro!-> chama o pânico")
            else:
                print("erro!-> chama o pânico")
        else :
            print("erro!-> chama o pânico")    
    else : 
        print("erro!-> chama o pânico") # um preocupação é como colocar o lambda ?
    return lexico #um loop no grafo, pois depois do ponto e virgula eu posso voltar para dc_c, como o lambda leva ao fim da função

#grafo [2]
def dc(lexico):
    simb = dc_c(lexico)
    simb = dc_v(simb)
    simb = dc_p(simb) 
    return simb

#grafo [1]
def programa(lexico) :
    if("program" == lexico.getSimbolo()) :
        simb = lexico.getSimboloNext();
        if( simb == "ident") :
            simb = lexico.getSimboloNext();
            if( simb == ";") :
                simb = lexico.getSimboloNext();
                simb= dc(simb) # depois que voltar dessa função , precisamos ou retornar o proximo simbolo, ou pegamos o proximo de onde esta parado
                #na fungao lexico.getSimboloNext();
                if(simb == "begin") :
                    simb = lexico.getSimboloNext()
                    simb = comandos(simb) #outro grafo
                    if( simb == "end") :
                        simb = lexico.getSimboloNext()
                        if( simb == ".") :
                            print("fim\n") #ou return simb
                        else : 
                            print("erro!-> chama o pânico")
                    else : 
                        print("erro!-> chama o pânico")
                else : 
                    print("erro!-> chama o pânico")
            else : 
                print("erro!-> chama o pânico")
        else : 
            print("erro!-> chama o pânico")
    else : 
        print("erro!-> chama o pânico")
    
    print("sucesso ou não , quem sabe?!?!")


                        