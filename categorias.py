from imprimir_tarefas import categorias
from normalizar import normalizar_categoria
def gerenciar_categorias():
    print("\nCategorias atuais:")
    for cat in categorias:
        print(f"- {cat}")
    
    opcao = input("\nDeseja adicionar ou remover uma categoria? (Adicionar/Remover/Cancelar): ").capitalize()
    if opcao == "Adicionar":
        nova_categoria = input("Digite o nome da nova categoria: ").capitalize()
        if nova_categoria not in categorias:
            categorias.add(nova_categoria)
            print(f"Categoria '{nova_categoria}' adicionada com sucesso!")
        else:
            print(f"Categoria '{nova_categoria}' já existe.")
    elif opcao == "Remover":
        categoria = input("Digite o nome da categoria que deseja remover: ").capitalize()
        if categoria in categorias:
            categorias.remove(categoria)
            print(f"Categoria '{categoria}' removida com sucesso!")
        else:
            print(f"Categoria '{categoria}' não encontrada.")
    elif opcao == "Cancelar":
        print("Operação cancelada.")
    else:
        print("Opção inválida.")