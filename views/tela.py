import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controllers.controle import inserir_produtos, validar_busca_produto, validar_delete, validar_novo_preco

def verificar_produto(): #crianção do produto 
    produto_digitado = produto.get()
    quantidade_digitada = quantidade.get()
    preco = preco_txt.get()

    sucesso, mensagem = inserir_produtos(produto_digitado, quantidade_digitada, preco)

    if sucesso:
        lbl_aviso.configure(text=mensagem, text_color="green")
    else:
        lbl_aviso.configure(text=mensagem, text_color="red")


def vizualizar_produto():
    janela_produtos = ctk.CTkToplevel(janela)
    janela_produtos.attributes('-topmost', True)
    janela_produtos.title("Estoque")
    janela_produtos.geometry("600x400")

    titulo_janela_produtos = ctk.CTkLabel(janela_produtos, text="Produtos em estoque", text_color="white")
    titulo_janela_produtos.pack(pady=20)

    visualizar_estoque = ctk.CTkTextbox(janela_produtos, width=500, height=300)
    visualizar_estoque.pack(pady=10)
    visualizar_estoque.delete("0.0", "end")  

    sucesso, produtos = validar_busca_produto()

    nome_produto = [] # *Lista vazia que recebe os nomes
    quantidade_produto = [] # *Lista vazia que recebe os produtos

    if sucesso:
        for produto in produtos:     
            estoque = f"ID: {produto[0]} | Produto: {produto[1]} | Preço: {produto[2]} | Quantidade: {produto[3]}\n"
            visualizar_estoque.insert("end", estoque)
            nome_produto.append(produto[1])
            quantidade_produto.append(produto[3])
    else:
        visualizar_estoque.insert("end", produtos)

    figura, ax = plt.subplots(figsize = (5, 4))
    ax.pie(quantidade_produto, labels=nome_produto, autopct='%1.1f%%')
    # *quantidade_produto = os valores de cada fatia
    # *labels = os nomes de cada fatia
    # *autopct = mostra a porcentagem em cada fatia | %1.1f numero 1 em casa decimal | %% coloca % no final 

    canvas = FigureCanvasTkAgg(figura, master=janela_produtos)
    # *FigureCanvasTkAgg = ponte entre matplotlib e customtkinter
    # *figura = o gráfico criado
    # *master = em qual janela ele aparece
    
    canvas.draw()  # *renderiza o gráfico
    canvas.get_tk_widget().pack(pady=10)  # *coloca na tela como widget


def msg_confirmar_exclusao(id_produto, lbl_delete_aviso):
    sucesso, mensagem = validar_delete(id_produto)

    if sucesso:
        lbl_delete_aviso.configure(text=mensagem, text_color="green")
    else:
        lbl_delete_aviso.configure(text=mensagem, text_color="red")


def deletar_produto():
    janela_delete = ctk.CTkToplevel(janela)
    janela_delete.attributes('-topmost', True)
    janela_delete.title("Descarte de Produto")
    janela_delete.geometry("600x400")

    titulo_janela_delete = ctk.CTkLabel(janela_delete, text="Produtos para Deletar", text_color="red")
    titulo_janela_delete.pack(pady=20)
    lbl_delete_aviso = ctk.CTkLabel(janela_delete, text="")
    lbl_delete_aviso.pack(pady=5)

    delete_id = ctk.CTkEntry(janela_delete, placeholder_text="Digite o ID do produto...")
    delete_id.pack(pady=20)

    vizualizar_estoque = ctk.CTkTextbox(janela_delete, width=500, height=300)
    vizualizar_estoque.pack(pady=20)
    vizualizar_estoque.delete("0.0", "end")

    sucesso, produtos  = validar_busca_produto()

    if sucesso:
        for produto in produtos:
            estoque = f"ID: {produto[0]} | Produto: {produto[1]} | Preço: {produto[2]} | Quantidade: {produto[3]}\n"
            vizualizar_estoque.insert("end", estoque)
    else:
        vizualizar_estoque.insert("end", produtos)

    btn_confirmar_delete = ctk.CTkButton(janela_delete, text="Excluir", command=lambda: msg_confirmar_exclusao(int(delete_id.get()), lbl_delete_aviso))
    btn_confirmar_delete.pack(pady=10)


def msg_atualizar_produto(id_produto, novo_preco, lbl_atualize_aviso):
    sucesso, mensagem = validar_novo_preco(id_produto, novo_preco)

    if sucesso:
        lbl_atualize_aviso.configure(text=mensagem, text_color="green")
    else:
        lbl_atualize_aviso.configure(text=mensagem, text_color="red")

def editar_produto():
    janela_edicao = ctk.CTkToplevel(janela)
    janela_edicao.attributes('-topmost', True)
    janela_edicao.title("Atualizar Produtos")
    janela_edicao.geometry("600x400")

    titulo_janela_edicao = ctk.CTkLabel(janela_edicao, text="Atualizar Produtos")
    titulo_janela_edicao.pack(pady=5)

    lbl_atualize_aviso = ctk.CTkLabel(janela_edicao, text="")
    lbl_atualize_aviso.pack(pady=20)

    produto_id = ctk.CTkEntry(janela_edicao, placeholder_text="Digite o ID do produto...")
    produto_id.pack(pady=20)

    novo_preco = ctk.CTkEntry(janela_edicao, placeholder_text="Digite o novo preço...")
    novo_preco.pack(pady=20)

    vizualizar_estoque = ctk.CTkTextbox(janela_edicao, width=500, height=300)
    vizualizar_estoque.pack(pady=20)

    vizualizar_estoque.delete("0.0", "end")

    sucesso, produtos  = validar_busca_produto()

    if sucesso:
        for produto in produtos:
            estoque = f"ID: {produto[0]} | Produto: {produto[1]} | Preço: {produto[2]} | Quantidade: {produto[3]}\n"
            vizualizar_estoque.insert("end", estoque)
    else:
        vizualizar_estoque.insert("end", produtos)

    btn_salvar = ctk.CTkButton(janela_edicao, text="Salvar", command=lambda: msg_atualizar_produto(produto_id.get(), novo_preco.get(), lbl_atualize_aviso))
    btn_salvar.pack(pady=10)


def iniciar_janela_principal():
    global janela, produto, preco_txt, quantidade, lbl_aviso

    janela = ctk.CTk()
    janela.title("Gestor de produtos")
    janela.geometry("600x400")

    lbl_titilo = ctk.CTkLabel(janela, text="Cadastre o seu produto")
    lbl_titilo.pack(pady=20)

    produto = ctk.CTkEntry(janela, placeholder_text="Digite o nome do produto...")
    produto.pack(pady=20)

    preco_txt = ctk.CTkEntry(janela, placeholder_text="Digite o valor do produto...")
    preco_txt.pack(pady=20)

    quantidade = ctk.CTkEntry(janela, placeholder_text="Digite o quantidade do produto...")
    quantidade.pack(pady=20)

    btn_salvar = ctk.CTkButton(janela, text="Salvar", command=verificar_produto)
    btn_salvar.pack(pady=20)

    btn_buscar_produto = ctk.CTkButton(janela, text="Estoque", width=140, height=28, corner_radius=25, command=vizualizar_produto)
    btn_buscar_produto.pack(pady=20)

    btn_delete_produto = ctk.CTkButton(janela, text="Deletar", width=140, height=28, corner_radius=25, command=deletar_produto)
    btn_delete_produto.pack(pady=20)

    btn_editar_produto = ctk.CTkButton(janela, text="Editar", width=140, height=28, corner_radius=25, command=editar_produto)
    btn_editar_produto.pack(pady=20)

    lbl_aviso = ctk.CTkLabel(janela, text= "")
    lbl_aviso.pack(pady=10)

    janela.mainloop()