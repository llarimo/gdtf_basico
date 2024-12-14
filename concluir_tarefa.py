from imprimir_tarefas import listar_tarefas
from menu import tarefas
def concluir_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    indice = input("\nDigite o número da tarefa que deseja marcar como concluída: ")
    if not indice.isdigit() or not (1 <= int(indice) <= len(tarefas)):
        print("Número inválido. Operação cancelada.")
        return

    indice = int(indice) - 1
    desc, pri, cat, _ = tarefas[indice]
    tarefas[indice] = (desc, pri, cat, "Concluída")
    print("Tarefa marcada como concluída!")