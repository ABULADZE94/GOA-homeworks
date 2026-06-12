def maximum(a):
    max = a[0]
    for i in a:
        if i>max:
            max = i
    return max

list = [7464551,2354415,124537347644,232]
print(maximum(list))