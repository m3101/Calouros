x = range(-50,100)
# y(x) = 2x³
y = [2*xi**3 for xi in x]
print(x)
print(y)
print(list(map(lambda x:2*x**3,x)))