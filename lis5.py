peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))


def calc(peso, altura):
  imc = peso / (altura**2)
  return imc


if calc(peso, altura) < 18.5:
  print("Abaixo do peso")

elif calc(peso, altura) > 18.5 and calc(peso, altura) < 25:
  print("Peso normal")

elif calc(peso, altura) > 25 and calc(peso, altura) < 30:
  print("Sobrepeso")

elif calc(peso, altura) > 30 and calc(peso, altura) < 35:
  print("Obesidade I")

elif calc(peso, altura) > 35 and calc(peso, altura) < 40:
  print("Obesidade II")

elif calc(peso, altura) > 40:
  print("Obesidade III")

else:
  print("Fica sossegado que tá ok!")