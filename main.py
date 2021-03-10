
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

# BISECTION SEARCH Example

l = 0
h = 100
c = False

print("Please think of a number between 0 and 100!")
while c == False:
    m = (l+h) // 2

    print("Is your secret number", str(m),"?")
    test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if test == "l":
        l = m
        m = (l + h) // 2
    elif test == "h":
        h = m
        m = (l + h) // 2
    elif test == "c":
        c = True
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was:", str(m))