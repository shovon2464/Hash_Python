def doURLify(str, trueLength):
    #converting the string into the list

    str =  list(str)
    #calculate the number of spaces
    spaceCount = 0
    for i in range(0,trueLength):
        if(str[i] == ' '):
            spaceCount +=1

    #move the cursor to the end
    index  = trueLength + spaceCount*2

    #mentioning the end of the string
    if(trueLength<len(str)):
        str[trueLength] = '\0'

    #traversing from the back of the array to insert those characters

    for i in range(trueLength-1,-1,-1):
        if(str[i] == ' '):
            str[index-1] = '0'
            str[index-2] = '2'
            str[index-3] = '%'
            index -=3
        else:
            str[index-1] = str[i]
            index -= 1


    return str

print(doURLify('Mr John Smith    ',13))