# Estou criando uma calculadora 100% com PowerShell, estava com vontade de ajudar uma amiga minha e aprimorar a minha lógica de programação
# Como eu ainda não sou muito familiarizado com a ideia de interface, vou fazer com que o usuário utilize os números para se locomover pela calculadora
# Comecei a calculadora no dia 2/04 (2 de abril) e pretendo acabar com a calculadora até terça feira
# A calculadora vai conter algumas fórmulas do curso da minha amiga (Arquitetura e Urbanismo), que são elas: Inclinação do Telhado, Dimensionamento de saída de emergência, Transformação do norte magnético em geográfico, índice de recinto, Quantidade de Lampadas e Iluminância Real em Lux
# Não sei se vai ser futuramente adicionado mais fórmulas na calculadora porém ela só me pediu essas.
function InterfacePrincipal { #Interface bem bonitinha
    Clear-Host
    Write-Host " ================================================================= "
    Write-Host "|  _____ _____ _____ _____ _ _____ _____ _____ _____ _____ _____  |"
    Write-Host "| |  _  | __  |     |  |  |_|_   _|   __|_   _|  |  | __  |  _  | |"
    Write-Host "| |     |    -|  |  |  |  | | | | |   __| | | |  |  |    -|     | |"
    Write-Host "| |__|__|__|__|__  _|_____|_| |_| |_____| |_| |_____|__|__|__|__| |"
    Write-Host "|                |__|                                             |"
    Write-Host " ================================================================= "
    Write-Host "|                           CALCULADORA                           |"
    Write-Host "|  [1] INCLINAÇÂO DO TELHADO                                      |"
    Write-Host "|  [2] DIMENSIONAMENTO DE SAÍDAS DE EMERGÊNCIA                    |"
    Write-Host "|  [3] TRANSFORMAÇÃO DO NORTE MAGNÉTICO EM GEOGRÁFICO             |"
    Write-Host "|  [4] ÍNDICE DE RECINTO                                          |"
    Write-Host "|  [5] QUANTIDADE DE LÂMPADAS                                     |"
    Write-Host "|  [6] ILUMINÂNCIA REAL EM LUX                                    |"
    Write-Host "|                                                                 |"
    Write-Host "|                            [0] SAIR                             |"
    Write-Host "|                                                                 |"
    Write-Host "|       CASO UMA MEDIDA NÃO POSSUA VALOR COLOQUE 'X' ou 'x'       |"
    Write-Host " ================================================================= "
    }
while ($true) {            

    InterfacePrincipal

    $tecla = [System.Console]::ReadKey($true).KeyChar #vai ler a tecla/número que será digitado

    switch($tecla){ #Troca para a tela correspondente do número que foi digitado
        
        '1'{ #Calculando a inclinação do telhado
            while ($true){
            Clear-Host
            Write-Host " ============================================== "
            Write-Host "        FÓRMULA DE INCLINAÇÃO DO TELHADO        "
            Write-Host "                                                "
            Write-Host "                        H                       "
            Write-Host "                   I = ---                      "
            Write-Host "                        V                       "
            Write-Host "                                                "
        $i = Read-Host " ADICIONE O VALOR DA INCLINAÇÃO (I)"
        $h = Read-Host " ADICIONE O VALOR DA ALTURA DO TELHADO (H)"
        $v = Read-Host " ADICIONE O VALOR DO VÃO DE ÁGUA (V)" 
            Write-Host " ============================================== " 
            if ($i -eq 'x' -or $i -eq 'X' ){
                $i = [double]$h / [double]$v
            }elseif ($v -eq 'x' -or $v -eq 'X'){
                $v = [double]$i * [double]$h
            }elseif ($h -eq 'x' -or $h -eq 'X'){
                $h = [double]$i * [double]$v
            }else{
                for ($cont = 3; $cont -ge 0; $cont--){
                    Clear-Host
                    Write-Host"VALOR INCORRETO, SAINDO DO SISTEMA EM: [$cont]"
                    Start-Sleep -Seconds 1
                }
                exit
        }
            
            Clear-Host
            Write-Host " =============================================== "
            Write-Host "  RESULTADO DO CALCULO DA INCLINAÇÃO DO TELHADO  "
            Write-Host "                                                 "
            Write-Host "  I = $i             "
            Write-Host "  H = $h                    "
            Write-Host "  V = $v                  "
            Write-Host "                                                 "
            Write-Host "  [1] CALCULAR OUTRO VALOR | [2] MENU PRINCIPAL  "
            Write-Host "             [0] SAIR DA CALCULADORA             "
            Write-Host "                                                 "
            Write-Host " =============================================== "

            $escolha = [System.Console]::ReadKey($true).KeyChar

            if ($escolha -eq '1'){
                continue
            }
            elseif ($escolha -eq '2') {
                break
            }
            elseif ($escolha -eq '0') {
                exit
            }
    }
        } 
        '2'{
            while($true){
            Clear-Host
            Write-Host " ============================================== "
            Write-Host "     DIMENSIONAMENTO DE SAÍDAS DE EMERGÊNCIA    "
            Write-Host "                                                "
            Write-Host "                        P                       "
            Write-Host "                   N = ---                      "
            Write-Host "                        c                       "
            Write-Host "                                                "
        $n = Read-Host " ADICIONE O NÚMERO DE UNIDADES DE PASSAGEM (N)"
        $p = Read-Host " ADICIONE A QUANTIDADE DE POPULAÇÃO (P)"
        $c = Read-Host " ADICIONE A CAPACIDADE A UNIDADE DE PESSAGEM (c)"
            Write-Host " ============================================== "
            if ($n -eq 'x' -or $n -eq 'X'){
                $n = [double]$p / [double]$c
            }
            elseif ($p -eq 'x' -or $p -eq 'X'){
                $p = [double]$n * [double]$c
            }
            elseif ($c -eq 'x' -or $c -eq 'X'){
                $c = [double]$p * [double]$n
            }
            else {
                for ($cont = 3; $cont -ge 0; $cont--){
                    Clear-Host
                    Write-Host"VALOR INCORRETO, SAINDO DO SISTEMA EM: [$cont]"
                    Start-Sleep -Seconds 1
                }
                exit                
        }
            Clear-Host
            Write-Host " ====================================================== "
            Write-Host "  RESULTADO DO DIMENSIONAMENTO DE SAÍDAS DE EMERGÊNCIA  "
            Write-Host "                                                        "
            Write-Host "        N = $n                   "
            Write-Host "        P = $p               "
            Write-Host "        c = $c               "
            Write-Host "                                                        "
            Write-Host "     [1] CALCULAR OUTRO VALOR | [2] MENU PRINCIPAL      "
            Write-Host "                [0] SAIR DA CALCULADORA                 "
            Write-Host "                                                        "
            Write-Host " ====================================================== "

            $escolha = [System.Console]::ReadKey($true).KeyChar

            if ($escolha -eq '1'){
                continue
            }
            elseif ($escolha -eq '2') {
                break
            }
            elseif ($escolha -eq '0') {
                exit
            }
        
            } 
        }
        '3'{
            while($true){
            Clear-Host
            Write-Host " ============================================== "
            Write-Host " TRANSFORMAÇÃO DO NORTE MAGNÉTICO EM GEOGRÁFICO "
            Write-Host "                                                "
            Write-Host "                                                "
            Write-Host "                  AZV = AZM + D                 "
            Write-Host "                                                "
            Write-Host "                                                "
        $azv = Read-Host " ADICIONE O VALOR DO AZIMUTE VERDADEIRO (AZV)   "
        $azm = Read-Host " ADICIONE O VALOR DO AZIMUTE MAGNÉTICO (AZM)    "
        $d = Read-Host " ADICIONE O VALOR DA DECLINAÇÃO MAGNÉTICA (D)   "
            Write-Host " ============================================== "    
            }
            if ($azv -eq 'x' -or $avz -eq 'X') {
                $azv = [double]$azm + [double]$d
            }
            elseif ($azm -eq 'x' -or $azm -eq 'X') {
                $azm = [double]$d - [double]$azv
            }
            elseif ($azv -eq 'x' -or $azv -eq 'X') {
                $azv = [double]$d - [double]$azm
            }
            else {
                for ($cont = 3; $cont -ge 0; $cont--) {
                    
                }
            }
        }
        '4'{
            while($true){
                
            }
        }
        '5'{
            while($true){
                
            }
        }
        '6'{
            while($true){
                
            }
        }
        '0'{

        }

    }
}