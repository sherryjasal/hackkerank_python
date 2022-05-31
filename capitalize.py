##You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
##For example, alison heck should be capitalised correctly as Alison Heck.

def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
 
##lessons learnt - if we use title() it will do same job but it will not consider alphanumeric (for which one of the test case was failing)
##using split() - replace and capitalize will help passes all the test cases
