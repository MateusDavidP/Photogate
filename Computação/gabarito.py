import tkinter as tk
from tkinter import ttk

# Dados de exemplo
dados = [
    {'Volta': 1, 'Tempo': 10.5, 'Acréscimo': 0.2, 'Vel. Inst': 50},
    {'Volta': 2, 'Tempo': 9.8, 'Acréscimo': 0.3, 'Vel. Inst': 55},
    {'Volta': 3, 'Tempo': 11.2, 'Acréscimo': 0.1, 'Vel. Inst': 48},
    {'Volta': 4, 'Tempo': 10.1, 'Acréscimo': 0.5, 'Vel. Inst': 52},
    {'Volta': 5, 'Tempo': 9.5, 'Acréscimo': 0.2, 'Vel. Inst': 54},
]

# Função para ordenar os dados por tempo de forma ascendente ou descendente
def ordenar_tabela(ascendente):
    dados_ordenados = sorted(dados, key=lambda x: x['Tempo'], reverse=not ascendente)
    atualizar_tabela(dados_ordenados)

# Função para atualizar a tabela com os novos dados
def atualizar_tabela(dados):
    # Limpar a tabela
    for linha in tabela.get_children():
        tabela.delete(linha)
    # Preencher a tabela com os novos dados
    for dado in dados:
        tabela.insert("", "end", values=(dado['Volta'], dado['Tempo'], dado['Acréscimo'], dado['Vel. Inst']))

# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Interface")
largura_pagina = janela.winfo_screenwidth()  # Largura da página
altura_pagina = janela.winfo_screenheight()  # Altura da página

# Configuração do tema escuro
janela.configure(bg='black')
style = ttk.Style(janela)
style.theme_use('clam')
# Configuração da tabela
colunas = ('Volta', 'Tempo', 'Acréscimo', 'Vel. Inst')
tabela = ttk.Treeview(janela, columns=colunas, show='headings')
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
tabela.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Preencher a tabela com os dados iniciais
atualizar_tabela(dados)

# Botões para ordenar a tabela
botao_maior_menor = tk.Button(janela, text="Ordem Maior para Menor", command=lambda: ordenar_tabela(True))
botao_maior_menor.pack(pady=5)
botao_menor_maior = tk.Button(janela, text="Ordem Menor para Maior", command=lambda: ordenar_tabela(False))
botao_menor_maior.pack(pady=5)

# Ajustar a largura da tabela para ocupar 45% da largura da página
largura_tabela = int(largura_pagina * 0.45)
tabela.column('#0', width=largura_tabela, stretch=tk.NO)
for coluna in colunas:
    tabela.column(coluna, width=int(largura_tabela / len(colunas)), stretch=tk.NO)

# Execução da interface
janela.mainloop()
