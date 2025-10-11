def linear_search(arr,n):
    for i in range(len(arr)):
        if n == arr[i]:
            return i 
    return -1

def search_strings(word,letter):
    for index,char in enumerate(word):
        if char==letter:
            return index
    return -1 

def search_in_2d_array(arr,n):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == n:
                return i,j
    return -1

# arr=list(map(int,input("Enter the array : ").split()))
# n=int(input("Enter the number to searched : "))
# print("Element found in index : ",linear_search(arr,n))
# word=input("Enter the word : ")
# letter=input("Enter the letter to be searched : ")
# print("Letter found in : ",search_strings(word,letter))

rows=int(input("Enter the number of rows : "))
arr = []
for i in range(rows):
    row=list(map(int,input(f"Enter the {i} row : ").split()))
    arr.append(row)
n=int(input("Enter the element to be searched : "))
print("Element found in : ",search_in_2d_array(arr,n))