def bubble_sort(arr):
    for i in range(len(arr)):
        print(f"Iteration : {i}, sorted till : {len(arr)-i}")
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
arr=list(map(int,input("Enter the array : ").split()))
print("Sorted array : ",bubble_sort(arr))