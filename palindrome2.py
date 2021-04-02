def isPalindrome(str):
    #for the bit vector
    count = 0
    for i in range(0,len(str)):
        #calculating index for the bit vector manipulation
        index = ord(str[i])-ord('a')
        # removing every other characters except 'a-z'
        if(index>=0):
            mask = 1 << index
            # if the character already seen
            if ((count & mask) > 0):
                count &= ~mask
            # if the character is not seen then add it in the bit vector
            else:
                count |= mask

    if((count & (count - 1)) == 0):
        return True
    return False

print(isPalindrome("atco cta"))
