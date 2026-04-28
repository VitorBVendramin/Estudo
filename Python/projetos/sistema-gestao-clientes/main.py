from models.cliente import cadastrar_cliente, buscar_todos, buscar_por_nome, buscar_por_id, atualizar_cliente, deletar_cliente
from models.produtos import cadastrar_produto, listar_produtos, buscar_por_nome_produto, buscar_por_id_produtos, atualizar_produto, deletar_produto
from models.venda import registrar_venda, listar_vendas, vendas_por_cliente, vendas_por_produto, produtos_mais_vendido

def menu_clientes():
    while True:
        print("=== MENU CLIENTES ===")
        print("1 - Cadastrar cliente")
        print("2 - Buscar todos os clientes")
        print("3 - Buscar por nome do cliente")
        print("4 - Buscar pelo ID do cliente")
        print("5 - Atualizar informações cliente")
        print("6 - Deletar cliente")
        print("7 - Voltar")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_cliente()

        elif opcao == 2:
            buscar_todos()

        elif opcao == 3:
            buscar_por_nome()

        elif opcao == 4:
            buscar_por_id()
        
        elif opcao == 5:
            atualizar_cliente()
        
        elif opcao == 6:
            deletar_cliente()
        
        elif opcao == 7:
            break

        else:
            print("Opção inserida não é válida, somente 1 a 7!")

def menu_produtos():
    while True:
        print("1 - Adicionar produto")
        print("2 - Listar todos")
        print("3 - Buscar por nome")
        print("4 - Buscar por ID")
        print("5 - Atualizar produto")
        print("6 - Remover produto")
        print("7 - Voltar")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_produto()

        elif opcao == 2:
            listar_produtos()

        elif opcao == 3:
            buscar_por_nome_produto()

        elif opcao == 4:
            buscar_por_id_produtos()
        
        elif opcao == 5:
            atualizar_produto()
        
        elif opcao == 6:
            deletar_produto()
        
        elif opcao == 7:
            break

        else:
            print("Selecione um número de 1 a 7 somente!")

def menu_vendas():
    while True:
        print("=== MENU VENDAS ===")
        print("1 - Registrar vendas")
        print("2 - Listar vendas")
        print("3 - Vendas por cliente")
        print("4 - Vendas por produto")
        print("5 - Produtos mais vendidos")
        print("6 - Voltar")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            registrar_venda()

        elif opcao == 2:
            listar_vendas()
        
        elif opcao == 3:
            vendas_por_cliente()
        
        elif opcao == 4:
            vendas_por_produto()
        
        elif opcao == 5:
            produtos_mais_vendido()

        elif opcao == 6:
            break

        else:
            print("Opção inválida. Utilize número de 1 a 7 somente!")

def menu_principal():
    while True:
        print("=== SISTEMA DE GESTÃO ===")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Vendas")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            menu_clientes()

        elif opcao == 2:
            menu_produtos()

        elif opcao == 3:
            menu_vendas()

        elif opcao == 4:
            break

        else:
            print("Opção não existe!")

menu_principal()