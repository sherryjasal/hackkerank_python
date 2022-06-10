##Consider a list (list = []). You can perform the following commands:
##insert i e: Insert integer i at position e.
##print: Print the list.
##remove e: Delete the first occurrence of integer .
##append e: Insert integer  at the end of the list.
##sort: Sort the list.
##pop: Pop the last element from the list.
##reverse: Reverse the list.
##Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(0,N):
        ip = input().split()
        if ip[0] == "print":
            print (list1)
        elif ip[0] == "insert":
            list1.insert(int(ip[1]), int(ip[2]))
        elif ip[0] == "remove":
            list1.remove(int(ip[1]))
        elif ip[0] == "append":
            list1.append(int(ip[1]))
        elif ip[0] == "pop":
            list1.pop()
        elif ip[0] == "sort":
            list1.sort()
        else:
            list1.reverse()
            
 ## lessons learnt: split - it splits by separator(), insert - insert value at specific index, remove - elt from specific index, append - inserts elements at
## specific index(if specified) else at the end, pop - deletes the element () from last
