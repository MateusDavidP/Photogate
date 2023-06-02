import tkinter as tk
from tkinter import ttk
import photogate as pt


#Pegando os dados
distancia = 7
arquivo = r'C:\Users\User\OneDrive - Etec Centro Paula Souza\Desktop\Arquivos photogata\Photogate\Computação\tempos.CSV'
voltas = pt.leitura_arquivo(arquivo)
voltas = pt.calculo_acrescimos(voltas)
voltas = pt.calculo_velocidades(distancia, voltas)

# Dados de exemplo
dados = [
        {'Volta': x[0], 'Tempo':x[1], 'Acréscimo':x[2], 'Vel. Inst':[3]} for x in voltas
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
janela.tk.call('lappend', 'auto_path', r'C:\Users\User\Downloads\awthemes-10.4.0')
janela.tk.call('package', 'require', 'awdark')
# Configuração do tema escuro
janela.configure(bg='black')
style = ttk.Style(janela)
print(style.theme_names())
style.theme_use('awdark')
# Configuração da tabela
colunas = ('Volta', 'Tempo', 'Acréscimo', 'Vel. Inst')
tabela = ttk.Treeview(janela, columns=colunas, show='headings', )
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
tabela.pack(padx=0, pady=0, expand=False, anchor='n', side= 'left')

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

# Configurando Grade
# Execução da interface
janela.mainloop()
