def linear_search(arr,index,num):
    if index == len(arr):
        return False
    if arr[index] == num:
        return True
    return linear_search(arr,index+1,num)

arr=[1,24,4,1,3,10,23]
print(linear_search(arr,0,12))