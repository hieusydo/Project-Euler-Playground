##def isPalindrome(s):

##    def toChars(s):
##        s = s.lower()
##        ans = ''
##        for c in s:
##            if c in 'abcdefghijklmnopqrstuvwxyz':
##                ans = ans + c
##        return ans

def isPal(s):
    toStr = str(s)
    if len(toStr) <= 1:
        return True
    else:
        return toStr[0] == toStr[-1] and isPal(toStr[1:-1])

    return isPal(s)
##    return isPal(toChars(s))

def findLPal():
    largest = 0
    for x1 in range(100,1000,1):
        for x2 in range(100,1000,1):
            if isPal(x1*x2) == True:
                if largest < x1*x2:
                    largest = x1*x2

    return largest


