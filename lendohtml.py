# Lendo o arquivo HTML
with open('192.168.137.217.html', 'r') as arquivo:
    conteudo = arquivo.read()

# Processando os dados
linhas = conteudo.strip().split('<body>')
linhas = linhas[1]
linhas = linhas.split('<br>')

dados = [linha.split(',') for linha in linhas]
for x in range(len(dados)):
    for y in range(3):
        dados[x][y] = int(dados[x][y])

# Imprimindo os resultados
for linha in dados:
    print(linha)
