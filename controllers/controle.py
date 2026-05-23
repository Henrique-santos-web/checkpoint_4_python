from models.modelo import inserir_nome_produto, buscar_nome_produto, atualizar_preco, deletar_produto


def validar_e_salvar(produto, quantidade_txt, preco_txt):
    if produto == "" or preco_txt == "":
        return False, "Campos vazios!"
    
    try:
        preco = float(preco_txt)
        quantidade = int(quantidade_txt)
    except ValueError:
        return False, "Erro nos números!"
    
    inserir_nome_produto(produto, preco, quantidade)
    return True


def validar_busca_produto():
    pass


def validar_preco():
    pass


def validar_delete():
    pass