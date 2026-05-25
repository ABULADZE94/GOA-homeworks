#1) შექმენით ლისტი 5 რიცხვით. for ციკლის გამოყენებით იპოვეთ ყველაზე დიდი რიცხვი.,
numbers2 = [12,44,99,66,88,]
max = numbers2[0]
for i in numbers2:
    if i > max:
        max = i
print(max)