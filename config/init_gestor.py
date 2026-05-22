import sqlite3

def conectar():
    return sqlite3.connect("gestor.db")

def criar_tabela():
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto TEXT NOT NULL,
                    quantidade TEXT NOT NULL          
                )
            """)

    except sqlite3.Error as erro:
        print(f"ERRO: Ocorreu um erro no banco: {erro}")

if __name__ == "__main__":
    criar_tabela()