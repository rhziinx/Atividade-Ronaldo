#entrada de dados
nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digita a nota2: "))

#processamento
media=(nota1 + nota2)/2

#saida com decisão
print(f"media final:{media:2f}")
if media>=6:
    print("aprovado")
else:
    print("reprovado")
