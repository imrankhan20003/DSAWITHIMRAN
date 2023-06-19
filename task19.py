def bubblesort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range(0, n-i-1):
            if arr[j] >arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr = []
for i in range (5):
    item = input()
    arr.append(item)
print(arr)
bubblesort(arr)
print(arr)
      