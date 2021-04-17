a,b = input().split()
a,b = (a[::-1],b[::-1])
base = 'font'
carry = 0
resultLength = max(len(a),len(b))
result = ''
r = 1
i=0
while r!=0:
    op1 = 0 if i>=len(a) else base.index(a[i])
    op2 = 0 if i>=len(b) else base.index(a[i])
    r = op1+op2+carry
    carry = 0
    if r<3:
        result = base[r]+result
    else:
        result = base[r-3]+result
        carry = 1
    i+=1
print(result)