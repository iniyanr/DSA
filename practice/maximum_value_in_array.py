def maximum_number(arr):
    max_num=None
    for i in arr:
        if max_num==None:
            max_num=i
            continue
        if i>max_num:
            max_num=i
    return max_num

def max_range(arr,a,b):
    max_num=None
    for i in range(a,b):
        if max_num==None:
            max_num=arr[i]
            continue
        if arr[i]>max_num:
            max_num=arr[i]
    return max_num
arr=list(map(int,input("Enter the array : ").split())) 
print("Maximum Number : ",maximum_number(arr))       
a=int(input("Enter the starting range : "))
b=int(input("Enter the ending range : "))
print("Maimum Number : ",max_range(arr,a,b))