def permutations(p,up,count):
    if up == "":
        print(p)
        count+=1
        print(count)
    ch=up[0]
    for i in range(len(p)+1):
        f,end=p[0:i],p[i:]
        permutations(f+ch+end,up[1:],count)

permutations("","abc",0)