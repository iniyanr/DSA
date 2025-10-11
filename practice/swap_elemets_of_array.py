def swap_array(arr,a,b):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp
arr=list(map(int,input("Enter the array : ").split(" ")))
a=int(input("Enter the 1st index to be swapped :"))
b=int(input("Enter the 2nd index to be swapped : "))
swap_array(arr,a,b)
print(f"Swapped array : {arr}")
    