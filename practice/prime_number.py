def prime_number(n):
    flag=0

    for i in range(2,n//2):
        if n%i == 0 :
            flag=1
            continue
    if flag == 1 :
        return False
    return True

n=int(input())
if n <= 1 :
    print("neither prime nor co-prime")
print(prime_number(n))