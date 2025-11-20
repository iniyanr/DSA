def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if end - start <= 1:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, mid, end)

arr = [2, 1, 4, 22, 34, 12, 99, 0]
merge_sort(arr)
print(arr)
