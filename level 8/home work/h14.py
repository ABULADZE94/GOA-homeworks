#14) შექმენით პროგრამა, სადაც მომხმარებელი შეიყვანს რამდენი რიცხვის დამატება უნდა ლისტში. for ციკლით იმდენჯერ შემოატანინეთ რიცხვი, დაამატეთ append() ფუნქციით და ბოლოს for ციკლით დაბეჭდეთ ყველა ელემენტი და len() ფუნქციით ლისტის სიგრძე.,
numbs = []
fav_num = int(input("how many numbers... "))
for i in range(fav_num):
    num3 = int(input("enter ur number"))
    numbs.append(num3)
for i in numbs:
    print(i)

print(len(numbs))
