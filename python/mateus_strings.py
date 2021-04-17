n = int(input())
for linha in range(n):
    string = input()
    numeros = [int(numero) for numero in 
                       "".join([(c if c.isnumeric() else ",") for c in string]).split(",")
                if numero]
    letras  = [letra       for letra  in
                       "".join([("," if c.isnumeric() else c) for c in string]).split(",")
                if letra]
    print("".join([letras[i]*numeros[i] for i in range(len(numeros))]))