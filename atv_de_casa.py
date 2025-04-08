num = int(input("Digite um número: "))
for i in range(1, num):
    resto = i % 2
    if resto != 0:
        print(i)