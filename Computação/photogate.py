
def leitura_arquivo(nome_arquivo: str) -> list:
    arquivo = open(nome_arquivo)

    voltas = []

    for linha in arquivo:
        dados = linha.split()
        voltas.append([dados[0], float(dados[1])])

    return voltas

def calculo_acrescimos(voltas: list) -> list:
    anterior = voltas[0][1]
    for volta in voltas:
        acrescimo = volta[1] - anterior
        volta.append(acrescimo)
        anterior = volta[1]

    return voltas


def calculo_velocidades(distancia: float, voltas: list) -> list:
    
    for volta in voltas:
        velocidade = distancia / volta[1]
        volta.append(velocidade)

    return voltas

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

main()





