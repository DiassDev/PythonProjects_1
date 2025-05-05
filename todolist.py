import datetime
import time

tarefas = []
username = input("Seja bem-vindo ao sistema de lista de afazeres!\nDigite seu nome: ")
print(f"Olá, {username}! Vamos começar a organizar sua lista de afazeres.\n")

def menu():
    print("\nEscolha a ação que deseja tomar: ")
    print("1 - Adicionar tarefa")
    print("2 - Alterar tarefa")
    print("3 - Marcar tarefa como concluída")
    print("4 - Adicionar data de vencimento a uma tarefa")
    print("5 - Mostrar tarefas")
    print("6 - Sair do sistema")

def mostrar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        for i, t in enumerate(tarefas):
            status = "✔️" if t["concluida"] else "❌"
            venc = f" (Vence em: {t['vencimento']})" if t["vencimento"] else ""
            print(f"{i+1}. {t['descricao']} {status}{venc}")

def main():
    while True:
        menu()
        opcao = input("Digite o número da opção desejada (1-6): ")
        if opcao == "1":
            descricao = input("Digite a tarefa que deseja adicionar: ")
            tarefas.append({"descricao": descricao, "concluida": False, "vencimento": None})
        elif opcao == "2":
            mostrar_tarefas()
            idx = int(input("Digite o número da tarefa que deseja alterar: ")) - 1
            if 0 <= idx < len(tarefas):
                nova = input("Digite a nova descrição: ")
                tarefas[idx]["descricao"] = nova
            else:
                print("Número inválido.")
        elif opcao == "3":
            mostrar_tarefas()
            idx = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
            if 0 <= idx < len(tarefas):
                tarefas[idx]["concluida"] = True
            else:
                print("Número inválido.")
        elif opcao == "4":
            mostrar_tarefas()
            idx = int(input("Digite o número da tarefa para adicionar data de vencimento: ")) - 1
            if 0 <= idx < len(tarefas):
                data = input("Digite a data de vencimento (dd/mm/aaaa): ")
                try:
                    datetime.datetime.strptime(data, "%d/%m/%Y")
                    tarefas[idx]["vencimento"] = data
                except ValueError:
                    print("Formato de data inválido.")
            else:
                print("Número inválido.")
        elif opcao == "5":
            mostrar_tarefas()
        elif opcao == "6":
            print("Saindo...")
            time.sleep(1)
            print("O sistema foi encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
