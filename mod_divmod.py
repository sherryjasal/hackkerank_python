## Read in two integers, a and b, and print three lines. 
## The second line is the result of the modulo operator:a%b . 
## The third line prints the divmod of a and b .



a = int(input())
b = int(input())

res1 = a//b
res2 = a%b
print (res1)
print (res2)
print ((res1, res2))
