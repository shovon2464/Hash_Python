def isUniqueChars(str):
    if(len(str)>128):
        return False
    char_set = [False]*128

    for i in range(0,len(str)):
        char_pos = ord(str[i])
        if(char_set[char_pos] == True):
            return False
        else:
            char_set[char_pos] = True
    return True

print(isUniqueChars('shovon'))