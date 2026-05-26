
dolar = 5  

def real_para_dolar(valor_real):
    return valor_real / dolar

def dolar_para_real(valor_dolar):
    return valor_dolar * dolar

while dolar:
    print("1 - Converter Dólar para Real")
    print("2 - Converter Real para Dólar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Valor em dólar: "))
        real = dolar_para_real(n1)
        print("O valor em real é:", real)

    elif opcao == "2":
        n1 = float(input("Valor em real: "))
        dolar = real_para_dolar(n1)
        print("O valor em dólar é:", dolar)

    elif opcao == "3":
        print("Programa encerrado")

    else:
        print("Opção inválida! Tente novamente.")