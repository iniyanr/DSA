def patterns_recursion(arr,r,c):
    if r==0:
        return arr
    if c<r:
        if arr[c]>arr[c+1]:
            arr[c],arr[c+1]=arr[c+1],arr[c]
        return patterns_recursion(arr,r,c+1)
    else:
        return patterns_recursion(arr,r-1,0)
arr=[4,2,3,1]
print(patterns_recursion(arr,len(arr)-1,0) )   