def makeFrequencyTable(str):
    #initializing the table with 26 character for hashing
    table = [0]*26
    for i in range(0, len(str)):
        index = ord(str[i])
        if(index>=ord('a') and index<=ord('z')):
            table[index-ord('a')] +=1
    return table

#calculating the numbe of odd number for determining the palindrom
def maxOdd(table):
    odd = 0
    for i in table:
        if (i%2 == 1):
            odd+=1
    if(odd>1):
        return False
    return True

def isPalindrome(str):
    table = makeFrequencyTable(str)
    return maxOdd(table)

print(isPalindrome('taco cat'))
