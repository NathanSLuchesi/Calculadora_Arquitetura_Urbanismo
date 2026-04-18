import os, sys # Importa os módulos
# OS é um módulo que faz com que eu tenha mais liberdade com o sistema operacional que está rodando
# o meu código, estou usando ele para que eu possa limpar o terminal com mais facilidade, indepen-
# te do sistema

# SYS é um módulo que faz com que eu possa interagir melhor com o interpretador do Python.


def clear(): # Função para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')

#Essa definição vai ser usada nas fórmulas que estão no código.
#Ela faz com que eu digite "clear()" no começo do "código" e ele limpe o terminal, fica com uma
#função mais limpa para o usuário.