nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
aumento = float(input("Qual a porcentagem de aumento?"))
calc_aumento = (salario*aumento)/100
soma_salario = calc_aumento+salario
print(f"Seu nome é: {nome}, sua idade é {idade} e seu salario é {salario:.2f}! Parabêns, você recebeu um aumento de: {calc_aumento}. O seu salario atual é: {soma_salario}!")