from datetime import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Erro: O ano deve estar entre 1922 e 2021.")
        except ValueError:
            print("Erro: Digite um número válido para o ano.")

def calcular_idade(ano_nascimento, ano_atual=2022):
    return ano_atual - ano_nascimento

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    
    print(f"{nome_completo}, você completou ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()
