tarefas = []
categorias = set(["Trabalho", "Pessoal", "Estudos", "Saúde", "Lazer"])
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\nTarefas:")
    for i, (desc, pri, cat, status) in enumerate(tarefas, start=1):
        print(f"{i}. {desc} - Prioridade: {pri} - Categoria: {cat} - Status: {status}")