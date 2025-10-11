def reverse_array(arr):
    start,end=0,len(arr)-1
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=list(map(int,input("Enter the array : ").split()))
reverse_array(arr)
print(f"Reversed Array : {arr}")