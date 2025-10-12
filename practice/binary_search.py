def binary_search(arr,n):
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>n:
            high=mid-1
        elif arr[mid]<n:
            low=mid+1
        else:
            return mid
    return -1
arr=list(map(int,input("Enter the array : ").split()))
n=int(input("Enter the number to be searched : "))
print(f"Element found in index : {binary_search(arr,n)}")
