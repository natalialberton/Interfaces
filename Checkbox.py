import tkinter as tk

janela = tk.Tk()

janela.title("Ofertas Promocionais")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text = "Deseja receber e-mails promocionais?", variable = var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceitar termos de Uso e Políticas de Privacidade", variable = var_politicas)
checkbox_politicas.grid(row=1, column=0)

def enviar():
    if var_promocoes.get():
        print("Usuário deseja receber promoções")
    else:
        print("Usuário não deseja receber promoções")
    
    if var_politicas.get():
        print("Usuário concordou com Termos de Uso e Políticas de Privacidade")
    else:
        print("Usuário não concordou com Termos de Uso e Políticas de Privacidade")


botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()