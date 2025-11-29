def permutation(proc,unproc):
    if not unproc:
        print(proc)
        return
    char=unproc[0]
    for i in range(len(proc)+1):
        new_proc=proc[:i]+char+proc[i:]
        permutation(new_proc,unproc[1:])
       
permutation("","abc")