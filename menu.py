
from imprimir_tarefas import listar_tarefas, tarefas, categorias
from concluir import concluir_tarefa
from adicionar import adicionar_tarefa
from atualizar import atualizar_tarefa, remover_tarefa
from categorias import gerenciar_categorias

def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa\n2. Listar Tarefas\n3. Atualizar Tarefa\n4. Remover Tarefa\n5. Gerenciar Categorias\n6. Concluir tarefa\n7. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            atualizar_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            gerenciar_categorias()
        elif opcao == "6":
            concluir_tarefa()
        elif opcao == "7":
            print("Espero ansiosamente por uma nova tarefa. Até logo!")
            break
        else:
            print("Opção inválida.")
