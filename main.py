print('=' * 10 + '\033[91m 🚨 Password Generator 🚨 \033[0m' + '=' * 10)

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.digits + "!@#?" * 2
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
    tamanho_senha = int(input("Qual o tamanho da senha? "))
    senha_gerada = gerar_senha(tamanho_senha)
    print("Sua senha é: ", senha_gerada)

    while True:
        opcao = input("Deseja refazer a senha? (S/N): ")
        if opcao.lower() == 's':
            break
        elif opcao.lower() == 'n':
            print("Finalizando o programa...")
            exit()
        else:
            print("Opção inválida. Por favor, responda com 'S' ou 'N'.")
