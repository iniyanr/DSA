# def fibonnaci_numbers(n):
#     if n<2:
#         return n
#     return fibonnaci_numbers(n-1)+fibonnaci_numbers(n-2)

# print(fibonnaci_numbers(2))

# def recursion_till_n(n):
#     if n==0:
#         return
    
#     recursion_till_n(n-1)
#     print(n)
# recursion_till_n(5)
# def recursion_from_1_to_n(n,i=1):
#     print(n)
#     if n==1:
#         return 0
    
#     return recursion_from_1_to_n(n-1,i+1)

# def reverse_number(n,sum):
#     tmp=n%10
#     sum=sum*10+tmp
#     if tmp==n:
#         return sum
#     return reverse_number(n//10,sum)

# print(reverse_number(234,0))

# def check_palindrome(num,n):
#     tmp=num%10
#     n=n*10+tmp
#     print("n 1 : ",n,"num 1: ",num)
#     if num%10==num:
#         return n
#     print("n : ",n,"num : ",num)
#     return check_palindrome(num//10,n)
# print(10 == check_palindrome(101,0))

# def count_no_of_zeroes(n,count):
#     print("n1 : ",n,"count : ",count)
#     if n<10:
#         return count
#     print("n2 : ",n,"count : ",count)
#     if n%10 == 0:
#         count+=1
#     print("n3 : ",n,"count : ",count)
#     return count_no_of_zeroes(n//10,count)
# print(count_no_of_zeroes(-500,0))

# def rotated_binary_search(arr,target,low,high):
#     mid=(low+high)//2
#     if low>high:
#         return -1
#     if target==arr[mid]:
#         return mid
#     if arr[low]<=arr[mid]:
#         if target>=arr[low] and target<=arr[mid]:
#             return rotated_binary_search(arr,target,low,mid-1)
#         else:
#             return rotated_binary_search(arr,target,mid+1,high)
#     if target>=arr[mid] and target<=arr[high]:
#         return rotated_binary_search(arr,target,mid-1,high)
    