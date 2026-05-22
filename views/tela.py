import customtkinter as ctk
from controllers.controle import validar_e_salvar

def verificar_produto():
    produto_digitado = produto.get()
    quantidade_digitada = quantidade.get()

    if produto_digitado == "" or quantidade_digitada == "":
        lbl_aviso.configure(text="Este campo não pode estar vazio", text_color="red")
        
        if validar_e_salvar(produto_digitado, quantidade_digitada):
            lbl_aviso.configure(text="Produto cadastrado!", text_color="green") 
        else:
            lbl_aviso.configure(text="")

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

    janela.mainloop()