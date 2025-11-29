def sorted_array(arr,index):
    if index+1 == len(arr):
        return True
    if arr[index] > arr[index+1]:
        return False
    else:
        return sorted_array(arr,index+1)

arr=[1,2,3,4,5,6,7,8,9,0]
print(sorted_array(arr,0))
    
