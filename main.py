print('>>>>>>> Password Generator <<<<<<<')

import random
import string

def gerador(length):
    character = string.ascii_letters + string.digits + string.digits + "!@#?" * 2
    password = ''.join(random.choice(character) for _ in range(length))
    return password

while True:
    password_length = int(input("> Qual o tamanho da senha? "))
    generated_password = gerador(password_length)
    print("> Sua senha é: ", generated_password)

    while True:
        opcao = input("> Deseja refazer a senha? (Y/N): ")
        if opcao.lower() == 'y':
            break
        elif opcao.lower() == 'n':
            print("> Finalizando o programa...")
            exit()
        else:
            print("> Opção inválida. Por favor, responda com 'S' ou 'N'.")
