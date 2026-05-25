#0) შექმენით პროგრამა, რომელიც მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინებს სახელს, დაამატებს ლისტში და შემდეგ for ციკლით ყველა სახელს დაბეჭდავს.,
namess = []

for i in range(5):
    names1 = int(input("enter name"))
    namess.append(names1)
for i in namess:
    print(i)