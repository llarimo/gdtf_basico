import os
import unicodedata
from imprimir_tarefas import listar_tarefas
from concluir_tarefa import concluir_tarefa
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_terminal()

def normalizar_categoria(categoria):
    return ''.join((c for c in unicodedata.normalize('NFD', categoria) if unicodedata.category(c) != 'Mn')).lower().strip()

tarefas = []
categorias = set(["Trabalho", "Pessoal", "Estudos", "Saúde", "Lazer"])


import unicodedata

def normalizar_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

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

if __name__ == "__main__":
    menu()
