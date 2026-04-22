from ui import clear # Importado de : ~/Calculadora_Arquitetura_Urbanismo/Python/ui.py

from calculations import calc_telhado, calc_norte, calc_emergencia, calc_indice, calc_lampadas, calc_lux

import sys

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

while True:
    user_choice = menu()

    match user_choice:

        case '1': # Inclinação do telhado
            calc_telhado.formula_telhado()
        
        case '2':
            calc_emergencia.formula_emergencia()
        
        case '3':
            calc_norte.formula_norte_magnetico()
        
        case '4':
            calc_indice.formula_indice_recinto()

        case '5':
            print("Em andamento")
    
        case '6':
            print("Em andamento")
        
        case '0':
            sys.exit()