l = [1,2,3,[1,1,1,1],[2,4,[1,1,1,1]]]
def soma(lista):
    acc = 0
    for item in lista:
        if type(item) == int:
            acc += item
        elif type(item) == list:
            acc += soma(item)
    return acc
print(soma(l))