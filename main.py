
#Fibonacci Sequence

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(4))


# Palindrome Checker

def isPalinedrome(s):
    def simpleChar(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(simpleChar(s))

print(isPalinedrome("!level#"))