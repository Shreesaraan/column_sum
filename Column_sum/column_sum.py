def column_sum(rows,columns,matrix):
    sum=[]
    for i in range(columns):
        add=0
        for j in range(rows):
            add+=matrix[j][i]
        sum.append(add)
    return sum

matrix=[]
rows=int(input("Number of rows : "))
columns=int(input("Number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print("Column Sum : ",column_sum(rows,columns,matrix))