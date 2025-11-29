def binary_search(arr,low,high,num):
    if low > high:
        return False
    mid=(low+high)//2
    if arr[mid] == num:
        return True
    if arr[mid]<num:
        return binary_search(arr,mid+1,high,num)
    else:
        return binary_search(arr,low,mid-1,num)
    
arr=[1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr,0,len(arr)-1,11))