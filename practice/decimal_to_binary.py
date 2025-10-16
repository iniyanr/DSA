def decimal_to_binary(n):
    arr=[]
    while n!=0:
        if n%2==0:
            arr.append(str(0))
        else:
            arr.append(str(1))
        n=n//2
    return "".join(arr[::-1])
n=int(input("Enter the number : "))
print("binary rep : ",decimal_to_binary(n))
