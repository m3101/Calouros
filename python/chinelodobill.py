bill = int(input())
chinelos = [i for i,k in enumerate(sorted(map(int,input().split()))) if k>=bill]
print(chinelos[0] if chinelos else -1)