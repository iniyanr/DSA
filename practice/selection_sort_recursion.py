def select_receursion(arr,r,c,max):
    if r==0:
        return arr
    if c<r:
        if arr[c]>arr[max]:
            return select_receursion(arr,r,c+1,c)