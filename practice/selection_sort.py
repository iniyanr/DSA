def selection_sort(arr):
    for i in range(len(arr)):
        print(f"Iteration : {i}, sorted till : {len(arr)-i}")
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=list(map(int,input("Enter the array : ").split()))
print("Sorted array : ",selection_sort(arr))