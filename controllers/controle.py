from models.modelo import inserir_produto

def validar_e_salvar(produto, quantidade, preco):
    if produto == "" and quantidade >= 0:
        print("Erro: Verifique se os campos foram preenchidos corretamente")
        return False
    elif preco <= 0.0:
        print("Erro: O preço deve estar acima de R$1,00")
        return False
    
    inserir_produto(produto, quantidade)
    return True