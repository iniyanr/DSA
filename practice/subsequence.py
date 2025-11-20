
def subsequence(proc,unproc):
    if unproc == "":
        print(f"{proc}")
        return
    char=unproc[0]
    subsequence(proc+char,unproc[1:])
    subsequence(proc,unproc[1:])
subsequence("","abc")
