def cyclic_sort(arr):
    n=len(arr)
    i=0
    while i < n:
        correct_index=arr[i]-1
        if arr[i] != arr[correct_index]:
            arr[i],arr[correct_index]=arr[correct_index],arr[i]
        else:
            i+=1
        print(arr)
    return arr
arr=list(map(int,input("Enter the array : ").split()))
print("Sorted array : ",cyclic_sort(arr))