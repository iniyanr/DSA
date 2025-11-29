def roated_binary_search(arr,low,high):
    if low>high:
        return None
    if low==high:
        return low
    mid=(low+high)//2
    if mid <high and arr[mid]>arr[mid+1]:
        return mid+1
    if mid > low and arr[mid] > arr[mid-1]:
        return mid
    if arr[mid]>=arr[low]:
        return roated_binary_search(arr,mid+1,high)
    else:
        return roated_binary_search(arr,low,mid-1)
arr = [4,5,6,7,0,1,2]
print(roated_binary_search(arr, 0, len(arr)-1))
