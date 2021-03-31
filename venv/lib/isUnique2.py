def isUniqueChars(str):
    checker = 0
    for i in range(0,len(str)):
        val = ord (str[i])-ord ('a')
        """
        00000000000000000000000000000001 a 2^0
           
        00000000000000000000000000000010 b 2^1

        00000000000000000000000000000100 c 2^2

        00000000000000000000000000001000 d 2^3
        """
        if((checker & (1 << val)) > 0):
            return False
        checker |= (1 << val)

    return True

print(isUniqueChars("shovon"))