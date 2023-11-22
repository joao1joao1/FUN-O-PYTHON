valor= int(input("Digite o valor da compra: "))
parcs= int(input("Digite a qtd de parcelas: "))
def par(valor,parcs):
    result = valor/parcs
    return result

print(f"Valor da conta R${valor}, parcelado em {parcs}x de {par(valor,parcs)}")
