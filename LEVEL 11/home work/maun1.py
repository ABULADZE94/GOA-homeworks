# 1) შექმენი ცვლადი secret  რომელიც უდრის რაღაც რიცხვს და ასევე num უდრის 0 და while loop უნდა 
# იმუშავოს მაქამდე სანამ num != secret და while შიგნით num უნდა უდრიდეს input რომ მომხმარებელმა შეიყვანოს რიცხვი 
# და თუ გამოიცნობს მაშინ გამოიტანოს "you win".
secret = 777
num = 0
while num != secret:
    num = int(input("enter your number"))
    if num == secret:
        print("you win")
# 2) შექმენი  2 ცვლადი a = 0 და b = 20 და ცარიელი სია nums და დაამატე რიცხვები 1 დან 20მდე while loop გამოყენებით.
a = 0
b = 20
nums = []
while a < b:
    a+=1
    nums.append(a)
# 3) შექმენი ცვლადი age = 0 და while loop იმუშავოს სანამ age < 18 და while შიგნით age = input მომხმარებელმა რომ შეიყვანოს თავისი ასაკი და 
# სანამ ასაკი ნაკლები იქნება 18 მაქამდე შეეკითხოს, და თუ 18-ზე მეტია მაშინ გამოიტანოს "თქვენ სრულწლოვანი ხართ".
age = 0
while age < 18:
    age = int(input("enter your age"))
    print("თქვენ სრულწლოვანი ხართ")
# 4) while loop გამოყენებით გამოიტანეთ მხოლოდ ლუწი რიცხვები. 
num = 0
while num <=100:
    print(num)
    num += 2

# 5) while lopp გამოყენებით გამოიტანეთ მხოლოდ კენტი რიცხვები.
num = 1
while num <=100:
    print(num)
    num += 2
# 6) ახსენი რა არის Flowchart.
# flowchart არის პროგრამირების მუშაობის სქემა და გვეხმარება დავინახოთ კოდი უფრო მარტივად 
# 7) ახსენი sequence, selection, iteration.
# sequence კოდი მიმდევრობით selection არის მაგალითად ორი პირობა და გადადის ერთზე ანუ აირჩევს interation არის კოდის გამეორება მაგაითად foor loopის დახმარებით ხდება interation