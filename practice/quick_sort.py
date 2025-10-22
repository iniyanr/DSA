
def quick_sort(nums,low,high):
    if low>=high:
        return
    
    start,end=low,high
    mid=(start+end)//2
    pivot=nums[mid]

    while start<=end:
        while nums[start]<pivot:
            start+=1
        while nums[end]>pivot:
            end-=1
        if start<=end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1

    quick_sort(nums,low,end)
    quick_sort(nums,start,high)
    
arr=[5,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(f"Sorted array : {arr}")