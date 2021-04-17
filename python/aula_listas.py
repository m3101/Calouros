import pdb

N = int(input())
lista_pessoas = []
for i in range(N):
    nome = input()
    idade = int(input())
    lista_pessoas.append([nome,idade])
print(lista_pessoas)
contador_renatos = 0
for pessoa in lista_pessoas:
    if pessoa[0]=="renato":
        contador_renatos+=1

print(f"Há {contador_renatos} renatos.")