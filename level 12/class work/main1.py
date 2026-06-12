def len_manual(data):
    count = 0
    for i in data:
        count+=1
    return count

def is_positive(num):
    if num >0:
        return True
    else:
        return False

print(len_manual("yes"))