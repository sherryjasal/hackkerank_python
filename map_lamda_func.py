##  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
## A list on a single line containing the cubes of the first N fibonacci numbers.

##The first  fibonacci numbers are [1,1,2,3] , and their cubes are [0, 1, 1, 8, 27]

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n): 
    list1 = [0,1]
    for i in range(2,n):
        list1.append(list1[i-1]+list1[i-2])
    return list1[0:n]

    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
## lessons learnt for fibonacci - keep 0, 1 as same in list and then use expression [i-1] + [i-2]
