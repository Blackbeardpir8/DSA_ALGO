def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        is_sorted = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                is_sorted = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if is_sorted:
            break

arr = [1, 2, 5, 3, 7, 4, 6, 8, 22, 44, 54, 64, 66456, 77, 867]
print(f"Normal arr = {arr}")

bubble_sort(arr)
print(f"Bubble sorted arr = {arr}")
