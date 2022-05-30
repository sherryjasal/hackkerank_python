##You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
##Www.HackerRank.com → wWW.hACKERrANK.COM
##Pythonist 2 → pYTHONIST 2 

def swap_case(s):
    count1 = 0
    count2 = 0  
    new_string = ''
    for a in s:
        if (a.isupper()) == True:
            count1 += 1
            new_string += (a.lower())
        elif (a.islower()) == True:
            count2 += 1
            new_string += (a.upper())   
        else:
            new_string += a 
    return new_string
  
  ## lessons learnt : isupper(), is lower() - bool if True then - iterate and update new_string using viceversa method.
  ## For other spaces or chars, just keep it same
