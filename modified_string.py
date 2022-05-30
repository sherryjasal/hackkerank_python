## Task 
##Read a given string, change the character at a given index and then print the modified string. 
##Function Description
##Complete the mutate_string function in the editor below.
##mutate_string has the following parameters:
##string string: the string to change
##int position: the index to insert the character at
##string character: the character to insert

def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]     
    return new_string
  
 ##lessons learnt: use slicing
