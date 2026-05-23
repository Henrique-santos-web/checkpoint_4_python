import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controllers.controle import validar_e_salvar
from models.modelo import buscar_produto

def verificar_produto():
    produto_digitado = produto.get()
    quantidade_digitada = quantidade.get()

    if produto_digitado == "" or quantidade_digitada == "":
        lbl_aviso.configure(text="Este campo não pode estar vazio", text_color="red")
        
        if validar_e_salvar(produto_digitado, quantidade_digitada):
            lbl_aviso.configure(text="Produto cadastrado!", text_color="green") 
        else:
            lbl_aviso.configure(text="")


def buscar_produto(visualizar_estoque):
    janela_produtos
    janela_produtos = ctk.CTkToplevel(janela)
    janela_produtos.title("Estoque")
    janela_produtos.geometry("600x400")

    janela_produtos = ctk.CTkLabel(janela, text="Produtos em estoque", text_color="white")
    visualizar_estoque.delete("0.0", "end")

    nome_produto, quantidade_produto = [], []

    produtos = buscar_produto()

    for produto in produtos:
        nome_produto.append(produto[1])
        quantidade_produto.append(produto[2])     
        estoque = f"Produto: {nome_produto} | Quantidade: {quantidade_produto}"

        figura, ax = plt.subplots(figsize=(5, 4)) 

        visualizar_estoque.insert("end", estoque)


def iniciar_janela_principal():
    global janela, produto, quantidade, lbl_aviso

    janela = ctk.CTk()
    janela.title("Gestor de produtos")
    janela.geometry("600x400")

    lbl_titilo = ctk.CTkLabel("Cadastre o seu produto")
    lbl_titilo.pack(pady=20)

    produto = ctk.CTkEntry(janela, placeholder_text="Digite o nome do produto...")
    produto.pack(pady=20)

    quantidade = ctk.CTkEntry(janela, placeholder_text="Digite o nome do produto...")
    quantidade.pack(pady=20)

    lbl_aviso = ctk.CTkLabel(janela, text= "")
    lbl_aviso.pack(pady=10)

    btn_salvar = ctk.CTkButton(
        janela,
        text="Salvar",
        command=verificar_produto
    )
    btn_salvar.pack(pady=20)

    visualizar_estoque = ctk.CTkTextbox(
        width=350,
        height=150
    )
    visualizar_estoque.pack(pady=10)

    janela.mainloop()