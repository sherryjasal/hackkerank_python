##Print the list of integers from  through  as a string, without spaces.
##Example 
##n=5
##Print the string 12345 

    n = int(input())
    for i in range(1, n+1):
        print(i, end='')
