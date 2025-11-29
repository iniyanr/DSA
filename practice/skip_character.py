def skip_character(word,new_word,char):
    if not word:
        return new_word
    if word[0]!=char:
        new_word=new_word+word[0]
    return skip_character(word[1:],new_word,char)

print(skip_character("datastructures","","a"))
