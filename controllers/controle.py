from models.modelo import inserir_nome_produto, buscar_nome_produto, atualizar_preco, deletar_produto


def inserir_produtos(produto, quantidade_txt, preco_txt):
    if produto == "" or preco_txt == "":
        return False, "Campos vazios!"
    
    try:
        preco = float(preco_txt)
        quantidade = int(quantidade_txt)
    except ValueError:
        return False, "Erro nos números!"
    
    inserir_nome_produto(produto, preco, quantidade)
    return True


def validar_busca_produto(id_produto): # *adicionar ao método de busca no view, assim recebendo os dados aqui e fazendo a verificação
    
    if buscar_nome_produto(id_produto):
        produtos = buscar_nome_produto()

        for produto in produtos:
            return produto, produtos # *retornar a def para o view, pra poder mostrar para o usuário o resultado da busca


def validar_novo_preco(id_produto, novo_preco):
    # *mudar essa def, para a def que me manda os valores novos
    # *quem manda os valores é a view, o controller verifica e manda para o model
    # *uma var recebe os valores atualizados e adiciono como parametro à def do model que entra em contato com o banco de dados e retorna para o view esses dados

    if novo_preco == None or novo_preco <= 0.0:
    # *Se o preço for NADA ou menor/igual a Zero, não passa na verificação
        return False
    else:
        atualizar_preco(id_produto, novo_preco) # *Aqui eu atualizo o meu banco de dados
        return novo_preco # *Aqui eu atualizo o para o meu usuário o novo preço


def validar_delete(id_produto):
    if id_produto in deletar_produto: # *Se o id estiver no banco de dados, enviamos as informações para ele (através dos parâmetros)
        deletar_produto(id_produto)

    return False
