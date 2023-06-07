def alterar_wifi(nome_rede= None, senha_rede= None, novo_modo= None, nome_arquivo= None):
    # Lê o arquivo .ino
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Procura pelo trecho a ser alterado
    if nome_rede != '':
        linhas[6] = 'const char* ssid = "{}";\n'.format(nome_rede)
    if senha_rede != '':
        linhas[7] = 'const char* password = "{}";\n'.format(senha_rede)
    if novo_modo != '':
        linhas[4] = '#define MODO {}\n'.format(novo_modo)

    # Escreve as alterações de volta no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)


def main():
    # Exemplo de uso
    nome_rede = input("Digite o novo nome da rede Wi-Fi: ")
    senha_rede = input("Digite a nova senha da rede Wi-Fi: ")
    novo_modo = input("Digite o novo valor para MODO: ")
    nome_arquivo = "teste.ino"

    alterar_wifi(nome_rede, senha_rede, novo_modo, nome_arquivo)

if __name__ == "__main__":
    main()