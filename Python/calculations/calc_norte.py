from ui import clear
import sys

# Esses "imports" sempre vão aparecer nos códigos de definição da fórmula, eu especifiquei qual seria função deles no "ui.py"

def formula_norte_magnetico(): # Calcúlo da inclinação do telhado
    while True: 
        clear()
        print (" ======================================== ")
        print ("     FÓRMULA DE TRANSFORMAÇÃO DO NORTE    ")
        print ("          MAGNÉTICO EM GEOGRÁFICO         ")
        print ("                                          ")
        print ("               Azv = Azm + D              ")
        print ("                                          ")
        azv = input("ADICIONE O VALOR DO AZIMUTE VERDADEIRO(Azv):") # Aqui vai começar a ler os valores        
        azm = input("ADICIONE O VALOR DO AZIMUTE MAGNÉTICO(Azm):")
        d = input("ADICIONE O VALOR DA DECLINAÇÃO(D):")
        if azv.upper() == 'X': # Caso não tenha o valor de azv
            azm = float(azm)
            d = float(d)
            azv = azm + d
        elif azm.upper() == 'X': # Caso não tenha o valor de azm
            azv = float(azv)
            d = float(d)
            azm = azv - d
        elif d.upper() == 'X': # Caso não tenha o valor de d
            azm = float(azm)
            azv = float(azv)
            d = azv - azm
        else: # Caso coloque algum tipo de valor que não corresponde para a fórmula
            clear()
            print("VALOR INCORRETO, PREENCHA TODOS OS NÚMEROS DA FÓRMULA PARA FUNCIONAR CORRETAMENTE.")
            input("PRESSIONE ENTER PARA TENTAR NOVAMENTE.")
            continue
        clear()
        print (" =============================================== ")
        print ("       RESULTADO DA TRANSFORMAÇÃO DO NORTE       ") # Vai mostrar os valores com du
        print ("             MAGNÉTICO EM GEOGRÁFICO             ") # Vai mostrar os valores com du
        print ("                                                 ") #-as casas decimais.
        print (f"              Azv = {azv:.2f}                   ") 
        print (f"              Azm = {azm:.2f}                   ")
        print (f"                D = {d:.2f}                     ")
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