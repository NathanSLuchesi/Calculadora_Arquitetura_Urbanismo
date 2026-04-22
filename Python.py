import os, sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    print (" =============================================================== ")
    print ("  _____ _____ _____ _____ _ _____ _____ _____ _____ _____ _____  ")
    print (" |  _  | __  |     |  |  |_|_   _|   __|_   _|  |  | __  |  _  | ")
    print (" |     |    -|  |  |  |  | | | | |   __| | | |  |  |    -|     | ")
    print (" |__|__|__|__|__  _|_____|_| |_| |_____| |_| |_____|__|__|__|__| ")
    print ("                |__|                                             ")
    print (" =============================================================== ")
    print ("      INSTRUÇÃO:CASO NÃO POSSUA O VALOR, COLOQUE 'X' OU 'x'      ")
    print ("                                                                 ")
    print ("                           CALCULADORA                           ")
    print ("                                                                 ")
    print ("  [1] INCLINAÇÂO DO TELHADO                                      ")
    print ("  [2] DIMENSIONAMENTO DE SAÍDAS DE EMERGÊNCIA                    ")
    print ("  [3] TRANSFORMAÇÃO DO NORTE MAGNÉTICO EM GEOGRÁFICO             ")
    print ("  [4] ÍNDICE DE RECINTO                                          ")
    print ("  [5] QUANTIDADE DE LÂMPADAS                                     ")
    print ("  [6] ILUMINÂNCIA REAL EM LUX                                    ")
    print ("                                                                 ")
    print ("                            [0] SAIR                             ")
    print ("                                                                 ")
    option = str(input("  SELECIONE UMA OPÇÃO(1, 2, 3, 4, 5, etc.): "))
    print (" =============================================================== ")
    return option

def calc_telhado():
    while True: # Em andamento
        clear()
        print (" ======================================= ")
        print ("    FÓRMULA DA INCLINAÇÃO DO TELHADO     ")
        print ("                     H                   ")
        print ("                I = ---                  ")
        print ("                     V                   ")
        i = input("ADICIONE O VALOR DA INCLINAÇÃO(I):")
        h = input("ADICIONE O VALOR DA ALTURA DO TELHADO(H):")
        v = input("ADICIONE O VALOR DO VÃO DA AGUÁ (V):")
        print (" ====================================== ")
        if i.upper() == 'X':
            h = float(h)
            v = float(v)
            i = h / v
        elif h.upper() == 'X':
            i = float(i)
            v = float(v)
            h = i * v
        elif v.upper() == 'X':
            h = float(h)
            i = float(i)
            v = h * i
        else:
            clear()
            print ("VALOR INCORRETO, SAINDO DO SISTEMA...")
            sys.exit()
        clear()
        print (" =============================================== ")
        print ("  RESULTADO DO CÁLCULO DA INCLINAÇÃO DO TELHADO  ")
        print ("                                                 ")
        print (f"                I = {i:.2f}                      ")
        print (f"                H = {h:.2f}                      ")
        print (f"                V = {v:.2f}                      ")
        print ("                                                 ")
        print ("   [1] CALCULAR OUTRO VALOR [2] MENU PRINCIPAL   ")
        print ("               [0] SAIR DO SISTEMA               ")
        print (" =============================================== ")
        option = str(input(" R:"))
        if option == '1':
            continue
        elif option == '2':
            return
        elif option == '0':
            sys.exit(0)
        else:
            clear()
            input("OPÇÃO INVÁLIDA, CLIQUE 'ENTER' PARA RETORNAR AO MENU")
            continue

def calc_emergencia():
    clear()
    print ("EM ANDAMENTO, SAINDO DO SISTEMA") # Em andamento
def calc_norte(): 
    clear()
    print ("EM ANDAMENTO, SAINDO DO SISTEMA") # Em andamento
def calc_indice():
    clear()
    print ("EM ANDAMENTO, SAINDO DO SISTEMA") # Em andamento
def calc_lampadas():
    clear()
    print ("EM ANDAMENTO, SAINDO DO SISTEMA") # Em andamento
def calc_lux():
    clear()
    print ("EM ANDAMENTO, SAINDO DO SISTEMA") # Em andamento

while True:

    user_choise = menu()
    
    match user_choise:

        case '1': #INCLINAÇÂO DO TELHADO                         
            calc_telhado()
        case '2': #DIMENSIONAMENTO DE SAÍDAS DE EMERGÊNCIA       
            pass # Em andamento
        case '3': #TRANSFORMAÇÃO DO NORTE MAGNÉTICO EM GEOGRÁFICO
            pass # Em andamento
        case '4': #ÍNDICE DE RECINTO                             
            pass # Em andamento
        case '5': #QUANTIDADE DE LÂMPADAS                        
            pass # Em andamento
        case '6': #ILUMINÂNCIA REAL EM LUX                       
            pass # Em andamento
        case '0': 
            sys.exit()