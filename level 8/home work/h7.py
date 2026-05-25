#7) შექმენით ლისტი: ["apple", "banana", "orange", "kiwi"]. for ციკლის გამოყენებით მოძებნეთ "banana" და remove() ფუნქციით წაშალეთ, შემდეგ for ციკლით დაბეჭდეთ დარჩენილი ელემენტები.,
fruits = ["apple", "banana", "orange", "kiwi"]
for i in fruits:
    if i == "banana":
        fruits.remove(i)

for i in fruits:
    print(i)
