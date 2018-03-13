ASCII_SIZE = 256
def getMaxOccuringChar(str):
    count = [0] * ASCII_SIZE
    max = -1
    c = ''
    for a in str:
        count[ord(a)]+=1;
    for a in str:
        if max < count[ord(a)]:
            max = count[ord(a)]
            c = a
    return c
str =input().split(' ')
print(" ".join(getMaxOccuringChar(s) for s in str))
