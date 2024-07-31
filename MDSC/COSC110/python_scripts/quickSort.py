def pivot(array, low, high):
    point = array[high]
    i = low - 1

    for j in range (low, high):
        if array[j] <= point:
            i = 1 + i
            (array[i], array[j]) = (array[j], array[i])
    
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
    

def quickSort (array, low, high):
    if low < high:
        pi = pivot(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 

 
data = [1, 7, 4, 1, 10, 9, -2]

print(data)
quickSort(data, 0, len(data))