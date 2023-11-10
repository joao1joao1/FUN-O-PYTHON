# Função serve p/ executar a mesma tarefa varias vezes

# palavra que define a função "DEF"

def dobro(numero): #def = nome_da_função(parametro) parametro= valor que sera usado
    dobro = numero*2 # define a(s) operação(ões) da função
    return dobro # retorna variavel

numero = int(input("Informe um number: "))

print("Dobro: ", dobro(numero)) #chama(ou melhor, ativa) a função = nome(parametro-> valor p/cálculo)

#obs: a variavel da linha 6 pode ter outro nome e retornar na linha 7
#umafunçao pode ter mais de duas operações tipo:

def dobro(numero): 
    dobro = numero*2 
    return dobro 

x = int(input("Informe um number: "))
z = int(input("Informe um number: "))
y = int(input("Informe um number: "))

print(f"Dobro de {x}: {dobro(x)}")
print(f"Dobro de {z}: {dobro(z)}")
print(f"Dobro de {y}: {dobro(y)}")