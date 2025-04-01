nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
if media>=7:
    print(f"Você está Aprovado{media}")
else:
    print(f"Você está Reprovado{media}")