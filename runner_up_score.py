##second_largest elt in array

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_set = set(arr)
    new_list = list(new_set)
    final_list = sorted(new_list)
    second_largest_elt = final_list[-2]
    print(second_largest_elt)
    
    ## use set cuz it removes duplicates from list and stoe it in list and then use sorted to access the elt
