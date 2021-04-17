a=int(input())
paridade = a%2
while a>=paridade:
    i=a
    while i>=paridade:
        print(i,end=" ")
        i-=2
    print()
    a-=2