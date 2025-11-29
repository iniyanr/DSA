def subset(proc,unproc):
    if not unproc:
        return [proc]
    char=unproc[0]
    left=subset(proc+char,unproc[1:])
    right =  subset(proc,unproc[1:])
    return left+right

def subseq(arr):
    subs=[""]
    for i in arr:
        new_sub=[]
        for j in subs:
            new_sub.append(j+i)
        subs.extend(new_sub)
    return subs

def subseq_int(nums):
    arr=[[]]
    for i in range(len(nums)):
        new_arr=[]
        for j in range(len(arr)):
            new_arr.append(arr[j]+[nums[i]])
        arr.extend(new_arr)
        print(arr)
    return arr
def subseq_sum(arr,k):
    for i in arr:
        if sum(i)==k:
            print(i)
# print(subset("","abc"))
subseq_sum(subseq_int([1,2,3]),3)