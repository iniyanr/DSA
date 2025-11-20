def merge(left,right):
    sorted_arr=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    while(i<len(left)):
        sorted_arr.append(left[i])
        i+=1
    while(j<len(right)):
        sorted_arr.append(right[j])
        j+=1
    print(sorted_arr)
    return sorted_arr
def merge_sort(arr,start,end):
    if (end-start) == 1:
        return arr
    mid=(start+end)//2
    left=merge_sort(arr,start,mid)
    right=merge_sort(arr,mid,end)
    return merge(left,right)

print(merge_sort([2,1,4,22,34,12,99,0]))