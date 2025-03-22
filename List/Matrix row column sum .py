lst = eval(input())
r = len(lst)
c = len(lst[0])
rowsum =[]
colsum = [0]*c

for i in range(r):
    row = 0 
    for j in range(c):
        row += lst[i][j]
        colsum[j] += lst[i][j]
    rowsum.append(row)
print(rowsum+colsum)
