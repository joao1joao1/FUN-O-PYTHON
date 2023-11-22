salario = float(input("Digite o salário: "))

gift = float(input("Digite o valor do Bônus em porcentagem: "))

des = float(input("Digite o valor do desconto: "))


def con(salario, gift, des):
  liq = salario + (salario * (gift / 100)) - des
  return liq


print(f"Salário líquido = {con(salario, gift, des)}")
