arr = [[1,1,3],[1,1,-5]]

def lud(arr):
    if len(arr) != len(arr[0]): return "Matrix not a square"
    counter, upperArr = 1, arr.copy()
    for pivot in range(0, len(arr)):
        #error handling start
        rowCounter = pivot
        if upperArr[pivot][pivot] == 0:
            for i in range(pivot+1, len(arr)):
                if upperArr[i][pivot] != 0:
                    upperArr[pivot], upperArr[i], counter = upperArr[i], upperArr[pivot], counter*-1
                    break
                else: rowCounter += 1
        if rowCounter == len(arr)-1:
            continue
        if (pivot == len(arr)-1) and (upperArr[pivot][pivot] == 0):
            print(0, "last is zero")
        #error handling end
        #LUD start
        dividend = upperArr[pivot][pivot]
        for row in range(pivot+1, len(arr)):
            factor = upperArr[row][pivot]/dividend
            for column in range(pivot, len(arr)):
                upperArr[row][column] = upperArr[row][column] - upperArr[pivot][column]*factor
    determinant = 1
    for pivot in range(len(arr)):
        determinant *= upperArr[pivot][pivot]
    return(determinant*counter)

def lud_minlined(arr):
    if len(arr) != len(arr[0]): return "Matrix not a square"
    determinant, counter, upperArr = 1, 1, arr.copy()
    for pivot in range(0, len(arr)):
        rowCounter, determinant = pivot, determinant*upperArr[pivot][pivot]
        if upperArr[pivot][pivot] == 0:
            for i in range(pivot+1, len(arr)):
                if upperArr[i][pivot] != 0:
                    upperArr[pivot], upperArr[i], counter = upperArr[i], upperArr[pivot], counter*-1
                    break
                else: rowCounter += 1
        if rowCounter == len(arr)-1: continue
        if (pivot == len(arr)-1) and (upperArr[pivot][pivot] == 0): return 0
        for row in range(pivot+1, len(arr)):
            for column in range(pivot, len(arr)):
                upperArr[row][column] = upperArr[row][column] - upperArr[pivot][column]*(upperArr[row][pivot]/upperArr[pivot][pivot])
    return(determinant*counter)

print(lud(arr))
print(lud_minlined(arr))