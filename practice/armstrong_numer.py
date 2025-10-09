def armstrong_number(n):
    count=0
    digits=[]
    temp=n
    while(temp>0):
        digits.append(temp%10)
        temp=temp//10
        count+=1
    sum=0
    for i in digits:
        sum+=pow(i,count)
    return sum==n
n=int(input())
print(armstrong_number(n))