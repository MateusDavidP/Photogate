def calculo_acrescimos(voltas: list) -> list:
    anterior = voltas[0][1]
    for volta in voltas:
        acrescimo = volta[1] - anterior
        volta.append(acrescimo)
        anterior = volta[1]

    return voltas


def calculo_velocidades(distancia: float, voltas: list) -> list:
    
    for volta in voltas:
        velocidade = distancia / volta[2]
        velocidade = round(velocidade, 3)
        volta.append(velocidade)

    return voltas

def leitura_arquivo(nome_arquivo: str) -> list:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    # Processando os dados
    linhas = conteudo.strip().split('<body>')
    linhas = linhas[1]
    linhas = linhas.split('<br>')
    linhas = [linha.split(',') for linha in linhas]
    linhas = linhas[1:len(linhas)-1]
    for x in range(len(linhas)):
        for y in [1,2]:
            linhas[x][y] = round(int(linhas[x][y])/1000, 3)
    return linhas
   



def ordenacao_velocidades(voltas: list, inverso: bool) -> list:
    voltas_ordenadas = sorted(voltas, key = lambda x: x[3], reverse= inverso)
    return voltas_ordenadas


def main():
    distancia = int(input())
    arquivo = input()
    voltas = leitura_arquivo(arquivo)
    voltas = calculo_acrescimos(voltas)
    voltas = calculo_velocidades(distancia, voltas)
    voltas_ordenadas = ordenacao_velocidades(voltas, invero = False)
    voltas_ordenadas_reversa = ordenacao_velocidades(voltas, inverso= True)

#problema: forma como será o output dos dados

if __name__ == "__main__":
    main()





