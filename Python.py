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


user_choise = menu()
while True:
    menu()
    match user_choise:
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':