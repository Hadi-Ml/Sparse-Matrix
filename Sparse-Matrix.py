
SparsMatrix = [[0 for _ in range(3)] for _ in range(100)]

n = int(input())

Value = 0

Row = 1

Count = 0

for i in range (n) :
    for j in range (n) :
        Value = int(input())
        if Value != 0 :
            Count += 1
            SparsMatrix[Row][0] = i
            SparsMatrix[Row][1] = j
            SparsMatrix[Row][2] = Value
            Row += 1

SparsMatrix[0][0] = n
SparsMatrix[0][1] = n
SparsMatrix[0][2] = Count

print (SparsMatrix[0:Count+1][:])
