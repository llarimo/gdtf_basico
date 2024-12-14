from imprimir_tarefas import categorias, tarefas
from normalizar import normalizar_acentos

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    
    
    prioridades_validas = ["alta", "média", "baixa"]
    
    prioridade = input("Prioridade (Alta, Média, Baixa): ").lower()  
    prioridade_normalizada = normalizar_acentos(prioridade)  

    while prioridade_normalizada not in [normalizar_acentos(p) for p in prioridades_validas]:
        print("Prioridade inválida. Escolha entre Alta, Média ou Baixa.")
        prioridade = input("Prioridade (Alta, Média, Baixa): ").lower()  
        prioridade_normalizada = normalizar_acentos(prioridade)
    
    
    prioridade = prioridade.capitalize()
    
    categoria = input(f"Categoria (existentes: {', '.join(categorias)}): ").capitalize()
    categoria_normalizada = normalizar_acentos(categoria) 

    categoria_encontrada = False
    for cat in categorias:
        if normalizar_acentos(cat) == categoria_normalizada:
            categoria_encontrada = True
            categoria = cat
            break
    
    if not categoria_encontrada:
        print(f"Categoria '{categoria}' não encontrada. Adicionando automaticamente.")
        categorias.add(categoria)
    
    tarefa = (descricao, prioridade, categoria, "Pendente")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")