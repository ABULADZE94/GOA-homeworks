#15) შექმენით ლისტი რიცხვებით. for ციკლის გამოყენებით დაითვალეთ რამდენი დადებითი და რამდენი უარყოფითი რიცხვია ლისტში.,
list = [1, -2, -66, 77, -55, 67]
positive = 0
negative = 0
for i in list:
    if i > 0:
        postive += 1
    elif i < 0:
        negative += 1

print(positive)
print(negative)