def floor_of_a_number(letters,target):
    low=0
    high=len(letters)-1
    if target<letters[0]:
        return -1
    while low<=high:
        mid=(low+high)//2
        if letters[mid] == target:
            return letters[mid]
        elif letters[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return letters[low-1]

letters=list(map(int,input("Enter the lettersay : ").split()))
n=int(input("Enter the number for which floor number should be found : "))
print(f"Flooe number : {floor_of_a_number(letters,n)}")
        
        