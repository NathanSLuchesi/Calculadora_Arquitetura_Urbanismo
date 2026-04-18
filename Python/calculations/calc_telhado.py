from ui import clear
import sys

def formula_telhado(): # Calcúlo da inclinação do telhado
    while True: 
        clear()
        print (" ======================================= ")
        print ("    FÓRMULA DA INCLINAÇÃO DO TELHADO     ")
        print ("                     H                   ")
        print ("                I = ---                  ")
        print ("                     V                   ")
        i = input("ADICIONE O VALOR DA INCLINAÇÃO(I):") # Aqui vai começar a ler os valores        
        h = input("ADIOCIONE O VALOR DA ALTURA DO TELHADO(H):")
        v = input("ADICIONE O VALOR DO VÃO DA AGUÁ (V):")
        print (" ====================================== ")
        if i.upper() == 'X': # Caso não tenha o valor de i
            h = float(h)
            v = float(v)
            i = h / v
        elif h.upper() == 'X': # Caso não tenha o valor de h
            i = float(i)
            v = float(v)
            h = i * v
        elif v.upper() == 'X': # Caso não tenha o valor de v
            h = float(h)
            i = float(i)
            v = h * i
        else: # Caso coloque algum tipo de valor que não corresponde para a fórmula
            clear()
            print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
            input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
            continue 
        clear()
        print (" =============================================== ")
        print ("  RESULTADO DO CÁLCULO DA INCLINAÇÃO DO TELHADO  ") # Vai mostrar os valores com du
        print ("                                                 ") #-as casas decimais.
        print (f"                I = {i:.2f}                      ") 
        print (f"                H = {h:.2f}                      ")
        print (f"                V = {v:.2f}                      ")
        print ("                                                 ")
        print ("   [1] CALCULAR OUTRO VALOR [2] MENU PRINCIPAL   ")
        print ("               [0] SAIR DO SISTEMA               ")
        print (" =============================================== ")
        option = input(" R:") 
        if option == '1': # Vai voltar para o começo do menu para calcular outro valor
            continue
        elif option == '2': # Retorna para o menu principal
            return
        elif option == '0': # Sai do sistema
            sys.exit(0)
        else: # Caso o usuário coloque uma letra aleatória ele vai ser jogado para o menu principal
            clear()
            input("OPÇÃO INVÁLIDA, CLIQUE 'ENTER' PARA RETORNAR AO MENU")
            continue