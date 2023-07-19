def count_array(arry):
    count_array=0
    maximum=float("-inf")
    for i in arry:
        if i > maximum:
            maximum=i
    for i in arr:
        if i == maximum:
            count_array+=1
    return len(arry)-count_array
print(count_array(list(map(int,input().split()))))
