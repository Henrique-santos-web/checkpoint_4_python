from models.modelo import inserir_nome_produto, buscar_id_produto, atualizar_preco, deletar_produto
                                   

def inserir_produtos(produto, quantidade_txt, preco_txt):
    if produto == "" or preco_txt == "":
        return False, "É obrigatório preencher este campo!"
    
    try:
        preco = float(preco_txt)
        quantidade = int(quantidade_txt)
    except ValueError:
        return False, "Erro nos números!"
    
    inserir_nome_produto(produto, preco, quantidade)
    return True, "Produto cadastrado"


def validar_busca_produto(): # *adicionar ao método de busca no view, assim recebendo os dados aqui e fazendo a verificação
    produtos = buscar_id_produto()

    if produtos:
        return True, produtos # *retornar a def para o view, pra poder mostrar ao usuário os produtos
                                
    return False, "ERRO: Nenhum produto encontrado!"


def validar_novo_preco(id_produto, novo_preco_txt):
    # *quem manda os valores é a view, o controller verifica e manda para o model
    # *uma var recebe os valores atualizados e adiciono como parametro à def do model que entra em contato com o banco de dados e retorna para o view esses dados

    if novo_preco_txt ==  "":
    # *Se o preço for NADA não passa na verificação
        return False, "ERRO: Este campo não pode ficar vazio!"

    # *Aqui o preço é convertido em float e verificado se não há letras entre os números
    try:
        novo_preco = float(novo_preco_txt)
    except ValueError:
        return False, "Preço inválido! Use apenas números!"
    
    # *Caso a conversão seja realizada com sucesso, é verificado se o valor está acima de 0
    if novo_preco <= 0:
        return False, "O preço deve ser maior que zero"
    
    atualizar_preco(id_produto, novo_preco)
    return True, "Preço atualizado com sucesso!"
    # *Tudo ok? Enviado para o banco de dados e retornado para o View os novos valores


def validar_delete(id_produto):
    if id_produto == "":
        return False, "Digite um ID válido!"
    
    produtos = buscar_id_produto()

    for produto in produtos:
        if int(id_produto) == produto[0]:
            deletar_produto(int(id_produto)) # *Aqui faço a conversão de novo para inteiro, pois eu não sabia se uma conversão já mantia ele por inteiro
            return True, "Produto deletado!"
        
    return False, "ID não localizado!"