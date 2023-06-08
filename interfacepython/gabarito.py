import tkinter as tk
from ttkwidgets import FloatEntry
from tkinter import ttk
from tkinter import filedialog, simpledialog
import photogate as pt
from altera_arquivo import alterar_wifi

# variaveis


# region Janela de dialogo


def open_dialog(janela):

    opcao_selecionada = tk.StringVar()

    def get_modo():
        x = opcao_selecionada.get()
        md = ['Onegate', 'Dualgate', 'Leitura']
        return md.index(x)
    # region corpo do dialogo

    class MyDialog(simpledialog.Dialog):
        def __init__(self, master):
            super().__init__(master)
            self.title('Alterando arquivo')

        def body(self, master):
            # Criação dos widgets
            self.label1 = ttk.Label(master, text="Nome da Rede:")
            self.label1.grid(row=0, column=0)
            self.entry1 = ttk.Entry(master)
            self.entry1.grid(row=0, column=1)

            self.label2 = ttk.Label(master, text="Senha da rede:")
            self.label2.grid(row=1, column=0)
            self.entry2 = ttk.Entry(master, show='*')
            self.entry2.grid(row=1, column=1)

            self.label3 = ttk.Label(master, text="Modo:")
            self.label3.grid(row=2, column=0)
            self.entry3 = ttk.Combobox(
                master,
                state='readonly',
                textvariable=opcao_selecionada,
                values=[
                    'Onegate',
                    'Dualgate',
                    'Leitura'])
            self.entry3.grid(row=2, column=1)

            self.label4 = ttk.Label(
                master, text='Enter: Enviar | Esc: Cancelar')
            self.label4.grid(row=3)
    # endregion

        def apply(self):
            global arquivosel
            # Função chamada quando o botão de salvar é pressionado
            rede = self.entry1.get()
            senha = self.entry2.get()
            modo = get_modo()
            arquivo = r'teste.ino'
            if arquivo != 0:
                arquivosel = True

            alterar_wifi(rede, senha, modo, arquivo)
    dialog = MyDialog(janela)

# endregion


# Função para atualizar a tabela com os novos dados


def atualizar_tabela(dados: list[dict[str, int]], tabela: ttk.Treeview):
    # Limpar a tabela
    for linha in tabela.get_children():
        tabela.delete(linha)
    # Preencher a tabela com os novos dados
    count = 1
    for dado in dados:
        if count % 2 == 0:
            tag = 'par'
        else:
            tag = 'impar'
        tabela.insert(
            "",
            "end",
            values=(
                dado['Volta'],
                dado['Tempo'],
                dado['Acréscimo'],
                dado['Vel. Inst']),
            tags=tag)
        count += 1
# endregion

# region função para ordenar tabela


def ordenar_tabela(
        ascendente: bool, dados: list[dict[str, int]], tabela, chave: str):
    dados_ordenados = sorted(dados, key=lambda x: x[chave], reverse=ascendente)
    atualizar_tabela(dados_ordenados, tabela)
# endregion

# region Função para abrir arquivo


def abrir_arquivos():
    global dados
    global voltas
    filepaths = filedialog.askopenfilename(
        filetypes=[("Arquivos HTML", "*.html")])
    arquivosel.set(filepaths)
    # !!! adionar função de pegar tmn
    try:
        distancia = float(entrada_var.get())
    except ValueError:
        error_label.configure(text='Insira o tamanho')
        pass
    rebeci = pt.leitura_arquivo(filepaths)
    calculado = pt.calculo_acrescimos(rebeci)
    calculado = pt.calculo_velocidades(distancia, calculado)
    dados = [
        {'Volta': x[0], 'Tempo':x[1], 'Acréscimo':x[3], 'Vel. Inst':x[4]} for x in calculado
    ]


# endregion

# region configurando cores alternadas na tabela

def pega_valor(event, entry: ttk.Entry, error: ttk.Label):
    valor = entry.get()
    if len(valor) > 6:
        error.configure(text='Apenas duas casas decimais')
        return False
    else:
        if len(valor) == 3 and valor[2] != '.':
            entry.insert(2, '.')
        if not valor.isdigit():
            error.configure(text='Insira apenas digitos')
            return False
        elif float(valor) <= 0:
            error.configure(text='Insira Valores maiores que 0')
            return False
        else:
            error.configure(text='')
            return True


def muda_modo(col):
    global modos
    for chave, valor in modos.items():
        if chave == col:
            if valor == 0:
                tabela.heading(chave, text=f"{chave} ▲")
                ordenar_tabela(False, dados, tabela, chave)
                modos[chave] = 1
            else:
                tabela.heading(chave, text=f"{chave} ▼")
                ordenar_tabela(True, dados, tabela, chave)
                modos[chave] = 0
        else:
            tabela.heading(chave, text=chave)
            modos[chave] = 0
# endregion


def main():
    # region var Globais
    global montartabela
    global arquivosel
    global bota
    global tabela
    global voltas
    global dados
    global entrada_var
    global error_label

    bota = False
    dados = []
    voltas = []

    # endregion

    # region Configuração de janela
    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Minha Interface")
    janela.geometry('1200x600')
    janela.minsize(800, 380)
    largura_pagina = janela.winfo_screenwidth()  # Largura da página
    altura_pagina = janela.winfo_screenheight()  # Altura da página
    print(largura_pagina, altura_pagina)

    janela.tk.call(
        'source',
        r'C:\Users\User\Downloads\Comptu\Computação\Azure-ttk-theme-main\azure.tcl')
    janela.tk.call("set_theme", "dark")

    janela.columnconfigure(0, weight=6)
    janela.columnconfigure(1, weight=4)
    janela.rowconfigure(0, weight=1)
    janela.rowconfigure(1, weight=1)
    janela.rowconfigure(2, weight=3)

    entrada_var = tk.StringVar()
    arquivosel = tk.StringVar()
    # Imprime o tema atual

    # endregion

    # region Configurando tabela

    # region Configuração da tabela
    colunas = ('Volta', 'Tempo', 'Acréscimo', 'Vel. Inst')
    altura_tabela = int(altura_pagina * 0.8)
    tabela = ttk.Treeview(janela, columns=colunas, show='headings')
    # endregion
    # Configurando cabeçarios
    tabela.heading(
        'Volta',
        text='Volta',
        anchor='center',
        command=lambda: muda_modo('Volta'))
    tabela.heading(
        'Tempo',
        text='Tempo',
        anchor='center',
        command=lambda: muda_modo('Tempo'))
    tabela.heading(
        'Acréscimo',
        text='Acréscimo',
        anchor='center',
        command=lambda: muda_modo('Acréscimo'))
    tabela.heading(
        'Vel. Inst',
        text='Vel. Inst',
        anchor='center',
        command=lambda: muda_modo('Vel. Inst'))
    # Ajustar a largura da tabela para ocupar 45% da largura da página
    largura_tabela = int(largura_pagina * 0.25)

    for coluna in colunas:
        tabela.column(
            coluna,
            width=int(
                largura_tabela /
                len(colunas)),
            stretch=tk.YES,
            anchor='center',
        )

    tabela.grid(row=0, column=0, rowspan=3, sticky="nsew")

    tabela.tag_configure('impar', background='#383838')
    tabela.tag_configure('par', background='#696666')
    # criando um dicionario para receber os modos dos cabeçario
    global modos
    modos = {
        'Volta': 0,
        'Tempo': 1,
        'Acréscimo': 1,
        'Vel. Inst': 1
    }

    # endregion

    # region botões

    selec = ttk.LabelFrame(
        janela,
        text="configurações",
        width=altura_pagina * 0.25)
    selec.grid(row=0, column=1, sticky="new")

    # Selecionar o arquivo
    montartabel = ttk.Button(
        selec,
        text='Montar Tabela',
        command=lambda: atualizar_tabela(
            dados,
            tabela))
    montartabel.pack(pady=10, side='top', anchor='center')
    botao_selecionar_arquivo = ttk.Button(
        selec,
        text="Selecione o arquivo de log",
        command=lambda: abrir_arquivos(),
        padding=(
            0,
            5))
    botao_selecionar_arquivo.pack(
        pady=10,
        side='top',
        anchor='center',
        before=montartabel)
    button = ttk.Button(
        selec,
        text="Configurar Rede e Modo",
        command=lambda: open_dialog(janela))
    button.pack(pady=10, anchor='center', side='top', after=montartabel)

    widget_verde = tk.Frame(janela, bg="green")
    widget_verde.grid(row=2, column=1, sticky="nsew")

    # endregion

    # region Configurando onde serão inseridos as configurações
    error_label = tk.Label(janela, text="", fg="red")
    error_label.pack(
        pady=5,
        side='top',
        anchor='center',
        after=botao_selecionar_arquivo)

    tamanhoasa = ttk.Label(selec, text="Insira o tamanho ( ͡° ͜ʖ ͡°)")
    tamanhoasa.pack(
        pady=10,
        side='top',
        anchor='center',
        after=botao_selecionar_arquivo)
    insiratmn = ttk.Entry(selec, validate='key', textvariable=entrada_var)
    insiratmn.configure(
        validatecommand=(
            insiratmn.register(
                lambda value: pega_valor(
                    value,
                    insiratmn,
                    error_label)),
            '%d',
            '%i',
            '%P'))
    insiratmn.bind(
        '<KeyRelease>',
        lambda event: pega_valor(
            event,
            insiratmn,
            error_label))

    # error_label.configure(text= insiratmn.get())

    insiratmn.pack(pady=5, side='top', anchor='center', after=tamanhoasa)

    # endregion

    # Execução da interface
    janela.mainloop()


main()
