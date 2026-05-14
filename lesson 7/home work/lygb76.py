# 1. ვქმნით შერეულ სიას სხვადასხვა მონაცემთა ტიპით
mixed_list = ["Python", 25, 3.14, True, "AI"]

print(f"საწყისი სია: {mixed_list}")

# 2. მომხმარებელს ვთხოვთ შემოიტანოს წასაშლელი ელემენტი
choice = input("რომელი ელემენტის წაშლა გსურთ? (ჩაწერეთ ზუსტი მნიშვნელობა): ")

# 3. ვცდილობთ წაშლას. 
# რადგან input-ით შემოსული მონაცემი ყოველთვის ტექსტია, 
# შევამოწმოთ არის თუ არა ის სიაში პირდაპირ, ან როგორც ციფრი.

if choice in mixed_list:
    mixed_list.remove(choice)
    print(f"ელემენტი წაშლილია. განახლებული სია: {mixed_list}")

# ვამოწმებთ, იქნებ მომხმარებელმა რიცხვი ჩაწერა
elif choice.isdigit() and int(choice) in mixed_list:
    mixed_list.remove(int(choice))
    print(f"რიცხვი წაშლილია. განახლებული სია: {mixed_list}")

# თუ ელემენტი საერთოდ არ მოიძებნა
else:
    print("Invalid Choice")