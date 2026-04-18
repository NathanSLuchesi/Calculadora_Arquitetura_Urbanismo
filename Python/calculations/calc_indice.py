from ui import clear
import sys

# Esses "imports" sempre vão aparecer nos códigos de definição da fórmula, eu especifiquei qual seria função deles no "ui.py"

def formula_indice_recinto(): # Calcúlo da inclinação do telhado
    while True: 
        clear()
        print (" ======================================== ")
        print ("       FÓRMULA DO ÍNDICE DE RECINTO       ")
        print ("                                          ")   # k = c * l / hm * (c + l)
        print ("                    C x L                 ")
        print ("            K = --------------            ")
        print ("                 Hm x (C + L)             ")
        print ("                                          ")
        c = input("ADICIONE O COMPRIMENTO DO AMBIENTE EM METROS(C):") # Aqui vai começar a ler os valores        
        l = input("ADICIONE A LARGURA DO AMBIENTE EM METROS(L):")
        hm = input("ADICIONE A DISTÂNCIA VERTICAL EM METROS DE UMA \nSUPERFICIE DE TRABALHO A LUMINÁRIA(Hm):")

        try: # Já que não é possível de ter outro tipo de fórmula para ser usada caso um número não tenha valor (x), coloquei um try para verificar se é realmente um número
            c = float(c)
            l = float(l)
            hm = float(hm)
        
        except ValueError:
            clear()
            print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
            input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
            continue # Da uma segunda chance para o usuário colocar todos os valores da fórmula
        k = (c * l) / (hm * (c + l))

        clear()
        print (" =============================================== ")
        print ("          RESULTADO DO ÍNDICE DE RECINTO         ") # Vai mostrar os valores com duas casas decimais
        print ("                                                 ")
        print (f"                K = {k:.2f}                      ") 
        print (f"                C = {c:.2f}                      ") 
        print (f"                L = {l:.2f}                      ")
        print (f"               Hm = {hm:.2f}                      ")
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