import tkinter as tk


def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('2ª Janela')
    botao_fechar = tk.Button(janela2, text="Fechar", command=janela2.destroy)
    botao_fechar.grid(row=1, column=0)


janela = tk.Tk()
janela.title("1ª Janela")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

botao = tk.Button(janela, text="Ir para outra janela", command=abrir_janela)
botao.grid(row=2, column=3)

janela.mainloop()