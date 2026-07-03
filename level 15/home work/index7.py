set1 = set()

set1.add(2)
set1.add(3)
set1.add(4)
set1.add(5)
set1.add(6)
print(set1)




set = {1,2,3,4,5,5,5,6,7,"python"}
set.add("hello")
set.remove("python")


set ={1,2,3,4,5,6,7,8,9,10}
list = []
for i in set:
    if i%2 == 0:
        list.append(i)
print(list)


set1 = set()
for i in range(1,20):
    set1.add(i)

print(set1)



set1 = set()
for i in range(1,101, 2):
    set1.add(i)

print(set1)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {"python","hello","world"}

set3 = set1 | set2
print(set3)



set1 = set()
list = [1,251,2329213,220]
set1.update(list)
print(set1)