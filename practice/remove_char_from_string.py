# def remove_char(s, char):
#     result = ""
#     for c in s:
#         if c != char:
#             result += c
#     return result
# print(remove_char("Hello World",'l'))

# using recursion

def remove_char(s,char,result,i):
    if i==len(s):
        return result
    if s[i]!=char:
        result+=s[i]
    return remove_char(s,char,result,i+1)
print(remove_char('Hello World','l',"",0))    
