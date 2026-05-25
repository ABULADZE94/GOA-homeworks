#4) შექმენით ცარიელი ლისტი. მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინეთ სიტყვა და თითოეული append() ფუნქციის გამოყენებით დაამატეთ ლისტში. ბოლოს for ციკლით დაბეჭდეთ ყველა ელემენტი.,
words = []
for i in range(5):
    x = input("enter your fav word")
    words.append(x)

for i in words:
    print(i)
