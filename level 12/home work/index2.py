def minimum(a):
    min = a[0]
    for i in a:
        if i<min:
            min=i
    return min

list = [67,686341,232329752,6109]

print(minimum(list))