from imprimir_tarefas import listar_tarefas, tarefas, categorias

def atualizar_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    indice = input("\nDigite o número da tarefa que deseja atualizar: ")
    if not indice.isdigit() or not (1 <= int(indice) <= len(tarefas)):
        print("Número inválido. Operação cancelada.")
        return

    indice = int(indice) - 1
    descricao = input("Nova descrição (ou Enter para manter): ")
    prioridade = input("Nova prioridade (Alta, Média, Baixa ou Enter para manter): ").capitalize()
    while prioridade and prioridade not in ["Alta", "Média", "Baixa"]:
        print("Prioridade inválida. Escolha entre Alta, Média ou Baixa.")
        prioridade = input("Nova prioridade (Alta, Média, Baixa ou Enter para manter): ").capitalize()

    categoria = input(f"Nova categoria (existentes: {', '.join(categorias)} ou Enter para manter): ").capitalize()
    if categoria and categoria not in categorias:
        print(f"Categoria '{categoria}' não encontrada. Adicionando automaticamente.")
        categorias.add(categoria)

    desc_atual, pri_atual, cat_atual, status_atual = tarefas[indice]
    descricao = descricao or desc_atual
    prioridade = prioridade or pri_atual
    categoria = categoria or cat_atual
    
    tarefas[indice] = (descricao, prioridade, categoria, status_atual)
    print("Tarefa atualizada com sucesso!")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    indice = input("\nDigite o número da tarefa que deseja remover: ")
    if not indice.isdigit() or not (1 <= int(indice) <= len(tarefas)):
        print("Número inválido. Operação cancelada.")
        return

    indice = int(indice) - 1
    tarefas.pop(indice)
    print("Tarefa removida com sucesso!")