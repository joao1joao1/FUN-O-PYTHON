f= int(input("Digite o número de faltas: "))
nota= 0
for a in range(1,3+1):
    n= int(input(f"Digite a {a}° nota: "))
    nota= nota+n

def ava (nota):
    m= nota/3
    return m

if f >= 30:
    print("Reprovado por FALTA!")
elif ava(nota) >= 8:
        print("Aprovado com sucesso!")
elif ava(nota) > 6 and ava(nota) <8:
    print("Aprovado!")
elif ava(nota) > 3 and ava(nota) <5.9:
    print("Recuperação!")
elif ava(nota) < 3:
    print("Reprovado!")
elif ava(nota) ==0:
    print("DESISTENTE")

print(f"O aluno está: {ava(nota)}")