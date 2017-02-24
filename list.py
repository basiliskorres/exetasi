x = [1, 0, 3, 0, 0, 5, 7]
for _ in range(len(x)-1):
    for index in range(len(x)-1):
        if x[index]==0:
            x[index+1],x[index]=x[index],x[index+1]

print (x)
