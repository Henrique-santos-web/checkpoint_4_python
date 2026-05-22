import sqlite3

def conectar():
    return sqlite3.connect("gestor.db")

def salvar_produto(produto, quantidade):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (produto, quantidade) VALUE (?,?)", (produto, quantidade))
        conexao.commit()