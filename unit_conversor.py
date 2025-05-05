username = input("Digite o seu nome: ")
print(f"{username} seja-bem vindo(a) ao conversor de unidades!")


def menu():

    print("\nDigite quais unidades você gostaria de converter: ")
    print('*' * 30)
    print("1 - Quilomêtros para milhas")
    print("2 - Milhas para quilômetros")
    print("3 - Celsius para fahrenheit")
    print("4 - Fahrenheit para celsius")
    print("5 - Sair do sistema")
    print('*' * 30)

def main():
    while True:
        menu()
        try:
            opcao = int(input("Digite a opção que deseja (1 - 5): "))
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 5.")
            continue

        if opcao == 1:
            k = float(input("Digite os quilômetros a serem convertidos: "))
            m = k / 1.609
            print(f'O valor convertido é {round(m, 2)} milhas.')
        
        elif opcao == 2:
            m = float(input("Digite as milhas a serem convertidas: "))
            k = m * 1.609
            print(f'O valor convertido é {round(k, 2)} quilômetros.')
        
        elif opcao == 3:
            c = float(input("Digite os graus Celsius: "))
            f = (c * 9/5) + 32
            print(f'O valor convertido é {round(f, 2)} °F.')
        
        elif opcao == 4:
            f = float(input("Digite os graus Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f'O valor convertido é {round(c, 2)} °C.')
        
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
    
main()
