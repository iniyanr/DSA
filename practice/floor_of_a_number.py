def floor_of_a_number(arr,n):
    low=0
    high=len(arr)-1
    if n<arr[0]:
        return -1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == n:
            return arr[mid]
        elif arr[mid]>n:
            high=mid-1
        else:
            low=mid+1
    return arr[low-1]

arr=list(map(int,input("Enter the array : ").split()))
n=int(input("Enter the number for which floor number should be found : "))
print(f"Flooe number : {floor_of_a_number(arr,n)}")
        
        