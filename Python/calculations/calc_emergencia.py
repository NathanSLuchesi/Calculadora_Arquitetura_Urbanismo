from ui import clear
import sys

# Esses "imports" sempre vão aparecer nos códigos de definição da fórmula, eu especifiquei qual seria função deles no "ui.py"

def formula_emergencia(): # Calcúlo da inclinação do telhado
    while True: 
        clear()
        print (" ======================================== ")
        print ("   FÓRMULA DO DIMENSIONAMENTO DE SAÍDAS   ")
        print ("              DE EMERGÊNCIA               ")
        print ("                                          ")
        print ("                      P                   ")
        print ("                 N = ---                  ")
        print ("                      c                   ")
        print ("                                          ")
        n = input("ADICIONE O NÚMERO DE UNIDADES DE PASSAGENS(N):") # Aqui vai começar a ler os valores        
        p = input("ADICIONE A QUANTIDADE DE POPULAÇÃO(P):")
        c = input("ADICIONE A CAPACIDADE DA UNIDADE DE PASSAGEM(c):")
        if n.upper() == 'X': # Caso não tenha o valor de n
            try:
                p = float(p)
                c = float(c)
                n = p / c
            except :
                clear()
                print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
                input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
                continue
        elif p.upper() == 'X': # Caso não tenha o valor de p
            try:
                n = float(n)
                c = float(c)
                p = n * c
            except:
                clear()
                print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
                input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
                continue
        elif c.upper() == 'X': # Caso não tenha o valor de c
            try:
                p = float(p)
                n = float(n)
                c = p * n
            except:
                clear()
                print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
                input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
                continue
        else: # Caso coloque algum tipo de valor que não corresponde para a fórmula
            clear()
            print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
            input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
            continue 
        clear()
        print (" =============================================== ")
        print ("    RESULTADO DO DIMENSIONAMENTO DE SAÍDA DE     ") # Vai mostrar os valores com du
        print ("                   EMERGÊNCIA                    ") # Vai mostrar os valores com du
        print ("                                                 ") #-as casas decimais.
        print (f"                N = {n:.2f}                      ") 
        print (f"                P = {p:.2f}                      ")
        print (f"                c = {c:.2f}                      ")
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