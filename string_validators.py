## Task
##You are given a string . 
##Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
##Input Format
##A single line containing a string .
##Constraints 0 < len(s) < 1000

##Output Format
##In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
##In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
##In the third line, print True if  has any digits. Otherwise, print False. 
##In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
##In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

def alnum(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
            break;
    return False

def alpha(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
            break;
    return False

def digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
            break;
    return False

def lower(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
            break;
    return False

def upper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
            break;
    return False

if __name__ == '__main__':
    s = input()
    alphanum_func = alnum(s)
    alpha_func = alpha(s)
    digit_func = digit(s)
    lower_func = lower(s)
    upper_func = upper(s)
    print(alphanum_func)
    print(alpha_func)
    print(digit_func)
    print(lower_func)
    print(upper_func)
