litros = float(input("Quantos litro de Gasolina você comprou? "))
combustivel = input("Qual tipo de combustivel você abasteceu? Digite E para etanol e G gasolina ")
val_gasolina = litros*5.80
val_etanol = litros*4.90
if combustivel == "g" or combustivel == "G":
    print(f"Você deve pagar {val_gasolina:.2f} em gasolina.")
else:
    if combustivel == "e" or combustivel == "E":
        print(f"Você deve pagar {val_etanol:.2f} em etanol.")
    else:
        print("Não foi nenhum dos dados solicitados!")


"""codigo do professor
tipo = input("Qual tipo de combustivel vc abasteceu? G para gasolina e E para etanol? ")
qtd = float(input("Quantos litros?"))
vgas = 5.8
veta = 4.9
valor = 0
if tipo == "G" or tipo == "g":
    valor = vgas*qtd
else:
    if tipo == "e" or tipo == "E":
        valor = veta*qtd
    else:
        print(f"Você gastou {valor:.2f}")"""


