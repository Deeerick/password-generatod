print('=' * 10 + '\033[91m 🚨 Password Generator 🚨 \033[0m' + '=' * 10)

import random
import string

def gerador(length):
    character = string.ascii_letters + string.digits + string.digits + "!@#?" * 2
    password = ''.join(random.choice(character) for _ in range(length))
    return password

while True:
    password_length = int(input("\033[91m > Qual o tamanho da senha? \033[0m"))
    generated_password = gerador(password_length)
    print("\033[91m > Sua senha é:  \033[0m", generated_password)

    while True:
        opcao = input("\033[91m > Deseja refazer a senha? (Y/N):  \033[0m")
        if opcao.lower() == 'y':
            break
        elif opcao.lower() == 'n':
            print("\033[91m > Finalizando o programa... \033[0m")
            exit()
        else:
            print("\033[91m > Opção inválida. Por favor, responda com 'S' ou 'N'. \033[0m")
