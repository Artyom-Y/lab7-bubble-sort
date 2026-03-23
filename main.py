def bubble_sort(arr: list) -> list:
    end = len(arr)
    if end in [0, 1]:
        return arr

    while end > 1:
        for i in range(0, end - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        end -= 1
    return arr


print(bubble_sort([5, 2, 8, 6, 6]))
