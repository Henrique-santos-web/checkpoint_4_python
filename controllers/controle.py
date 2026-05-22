from models.modelo import salvar_produto

def validar_e_salvar(produto, quantidade):
    if produto == "" and quantidade >= 0:
        print("Erro: Verifique se os campos foram preenchidos corretamente")
        return False
    
    salvar_produto(produto, quantidade)
    return True