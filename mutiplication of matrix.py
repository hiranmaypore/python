x=[[12,7,3],
   [4,5,6],
   [7,8,9]]
y=[[5,8,1],
   [6,7,4],
   [4,5,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
          result[i][j] += x[i][j]*y[k][j]
print(result)
        