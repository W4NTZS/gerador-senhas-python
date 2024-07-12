import random
import string

def senha(quant_caractere, vezes=1):
    simbolos = "!@#$%&*"
    for c in range(0, vezes):
        caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + simbolos
        password = "".join(random.choice(caracteres) for _ in range(quant_caractere))
        print(password)

if __name__ == '__main__':
    print(f"{'-' * 5} Gerador de Senhas {'-' * 5}")
    try:
        quantidade = int(input('Quantas senhas deseja criar?: '))
        tamanho = int(input('Digite o tamanho de caracteres da senha: '))
        if tamanho < 6:
            print('\033[33mA senha precisa conter mais de 5 Caracteres.\033[m')
        else:
            senha = senha(tamanho, quantidade)

    except (ValueError, TypeError):
        print('\033[31mERRO: Digite um número Válido.\033[m')
    except KeyboardInterrupt:
        print('\n\033[31mERRO: O Usuário decidiu não informar os dados\033[m')
    except:
        print('\033[31mERRO no Sistema')
    finally:
        print('-' * 27)
        print('Obrigado por acessar nosso Programa.')
