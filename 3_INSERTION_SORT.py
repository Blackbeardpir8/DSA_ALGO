def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [7232, 4, 234, 35, 645, 76, 8, 35, 231, 4, 6547, 867, 332]
print(f"Normal arr = {arr}")
insertion_sort(arr)
print(f"Sorted arr = {arr}")
