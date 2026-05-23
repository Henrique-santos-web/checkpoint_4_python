import sqlite3

def conectar():
    return sqlite3.connect("gestor.db")


def inserir_nome_produto(nome_produto, preco, quantidade):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO nome_produtos (nome_nome_produto, preco, quantidade) VALUE (?, ?, ?)", (nome_produto, preco, quantidade, ))
        conexao.commit()


def buscar_nome_produto():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM nome_produtos")
        nome_produtos = cursor.fetchall()

        return nome_produtos
    

def atualizar_preco(id_produto, novo_preco):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cmd_sql = "UPDATE produtos SET preco = ?  WHERE id = ?"
        cursor.execute(cmd_sql, (novo_preco, id_produto))
        conexao.commit()

def deletar_produto(id_produto):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cmd_sql = "DELETE FROM produtos WHERE id = ?"
        cursor.execute(cmd_sql, (id_produto))
        conexao.commit()