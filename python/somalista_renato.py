a = [1,2,3,4,5,6]
b = [7,8,9,10,11,12]
soma = []
for i in range(len(a)):
    soma.append(a[i]+b[i])
print(soma)
soma = [a[i]+b[i] for i in range(len(a))]
print(soma)