# Gestor de Produtos

Sistema desktop de gestão de estoque desenvolvido em Python com interface gráfica.

## Funcionalidades
- Cadastrar produtos com nome, preço e quantidade
- Visualizar estoque com gráfico pizza
- Deletar produtos pelo ID
- Editar preço de produtos pelo ID

## Tecnologias utilizadas
- Python 3.14
- CustomTkinter — interface gráfica
- SQLite3 — banco de dados
- Matplotlib — gráficos

## Como executar

1. Instale as dependências:

pip install customtkinter matplotlib

2. Execute o programa:

python main.py

## Estrutura do projeto

checkpoint_4_python/

├── main.py

├── models/

│   └── modelo.py

├── controllers/

│   └── controle.py

└── views/

    └── tela.py