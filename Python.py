import os, sys

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpar()
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

def calc_telhado(): # Em andamento
    limpar()
    print (" ======================================= ")
    print ("    FÓRMULA DA INCLINAÇÃO DO TELHADO     ")
    print ("                     H                   ")
    print ("                I = ---                  ")
    print ("                     V                   ")
    i = float(input("ADICIONE O VALOR DA INCLINAÇÃO(I):"))
    h = float(input("ADIOCIONE O VALOR DA ALTURA DO TELHADO(H):"))
    v = float(input("ADICIONE O VALOR DO VÃO DA AGUÁ (V):"))
    print (" ====================================== ")
    if i == 'X' and 'x':
        i = h / v
    elif h == 'X' and 'x':
        h = i * v
    elif v == 'X' and 'x':
        v = h * i
    else:
        limpar()
        print ("VALOR INCORRETO, SAINDO DO SISTEMA...")
        sys.exit()
    limpar()
    print (" =============================================== ")
    print ("  RESULTADO DO CÁLCULO DA INCLINAÇÃO DO TELHADO  ")
    print (" I =")
    print (" H =")
    print (" V =" )
    print ("  ")
    print ("  ")
    print ("  ")
    print ("  ")
    print ("  ")

def calc_emergencia():
    # Em andamento
def calc_norte():
    # Em andamento
def calc_indice():
    # Em andamento
def calc_lampadas():
    # Em andamento
def calc_lux():
    # Em andamento

user_choise = menu()

while True:
    menu()
    match user_choise:
        case '1': #INCLINAÇÂO DO TELHADO                         
        case '2': #DIMENSIONAMENTO DE SAÍDAS DE EMERGÊNCIA       
        case '3': #TRANSFORMAÇÃO DO NORTE MAGNÉTICO EM GEOGRÁFICO
        case '4': #ÍNDICE DE RECINTO                             
        case '5': #QUANTIDADE DE LÂMPADAS                        
        case '6': #ILUMINÂNCIA REAL EM LUX                       
        case '0': sys.exit()