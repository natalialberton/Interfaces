import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Cotação de Moedas")
#Configurando o tamanho da janela para que ela não tenha bordas sobrando se o usuário aumentar a tela
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width='35', height='5')
#O método grid nos deixa escolher aonde colocar o texto, tendo como referência linhas e colunas
mensagem.grid(row=0, column=0, columnspan=2, stick='NSEW')

mensagem2 = tk.Label(text = "Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

mensagem3 = tk.Label(text = "Caso você queira pegar mais de 1 cotação ao mesmo tempo, digite uma moeda em cada linha")
mensagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='NSWE')

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

moedas = list(dicionario_cotacoes.keys())
#Combobox cria uma lista de opções (valores = moedas)
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text = "Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)


def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
            mensagem4 = tk.Label(text="\n".join(mensagem_cotacoes))
            mensagem4.grid(row=6, column=0)


botao_multiplascotacoes = tk.Button(text="Buscar Cotações", command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=5, column=1)

#A função mainloop abre a janelinha e deixa ela rodando eternamente até o usuário fechá-la, ou ela completar sua função
janela.mainloop()

#Métodos não usados no código:
#O método pack insere o objeto mensagem dentro da janela
#mensagem.pack()
#O método entry permite que o usuário insira dados no programa
#moeda = tk.Entry()
