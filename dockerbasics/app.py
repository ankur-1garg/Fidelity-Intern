def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = []
    right = []
    
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return quicksort(left) + [pivot] + quicksort(right)

# Get input from user
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

print(f"\nOriginal array: {arr}")
sorted_array = quicksort(arr)
print(f"Sorted array: {sorted_array}")
