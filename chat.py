import os

mensagens = []

nome = input("Nome: ")

while True:

    # limpando o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    
    print ("_____________________")

    # Obtendo Textos
    texto = input ("mensagem: ")
    if texto == "fim":
        break
    # Criando a Mensagem
    mensagens.append({
        'nome': nome,
        'texto': texto
    })
    