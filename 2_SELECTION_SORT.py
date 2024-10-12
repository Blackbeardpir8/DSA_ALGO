def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]



arr = [7232,4,234,35,645,76,8,35,231,4,6547,867,332]
print(f"Normal arr = {arr}")
selection_sort(arr)
print(f"Sorted arr = {arr}")