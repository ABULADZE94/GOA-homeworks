person1 = {
    "name":"bekss",
    "age":16,
    "DOB":13
}

person2 = {
    "name":"ani",
    "age":11,
    "DOB":4
}

for i in person1.values():
    print(i)

for i in person2.values():
    print(i)



    stuff = {
    'apples': 32,
    "peaches": 25,
    "bananas": 74,
    "oranges": 5,
}

stuff["apples"] = 21
stuff["oranges"] = 0
for i in stuff.values():
    print(i)



    prices = {
    "FirstItem" : 22,
    "SecondItem" : 13,
    "ThirdItem" : 16
}

for key, value in prices.items():
    print(key," costs ", value)