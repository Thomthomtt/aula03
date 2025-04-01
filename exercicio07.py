time1 = input("Qual o nome do primeiro time? ")
gols1 = int(input("Quantos gols foram marcados pelo primeito time? "))
time2 = input("Qual o nome do segundo time? ")
gols2 = int(input("Quantos gols foram marcados pelo segundo time? "))
if gols1>gols2:
    print(f"O time {time1} foi o vencedor com {gols1} gols")
else:
    if gols1==gols2:
        print(f"Não houve vencedor, deu empate")
    else:
        print(f"O time {time2} foi o vencedor com {gols2} gols")
