# საწყისი სია
products = ["apple", "banana", "milk"]

# ეკრანზე გამოსატანი მენიუ
print(f"{products}")
print("1. პროდუქტის დამატება.")
print("2. პროდუქტის წაშლა.")
print("3. პროდუქტების რაოდენობის გაგება.")

# მომხმარებლის არჩევანი
choice = input("\nაირჩიეთ მოქმედება: ")

if choice == "1":
    # პროდუქტის დამატება
    new_product = input("შემოიტანეთ პროდუქტი: ")
    products.append(new_product)
    print(products)

elif choice == "2":
    # პროდუქტის წაშლა
    remove_product = input("შემოიტანეთ პროდუქტი წასაშლელად: ")
    # აქაც, რომ არ "დაიქრაშოს" პროგრამა, ჯობია შევამოწმოთ არსებობს თუ არა
    if remove_product in products:
        products.remove(remove_product)
        print(products)
    else:
        print("Invalid Choice")

elif choice == "3":
    # რაოდენობის გაგება
    print(len(products))

else:
    # თუ სხვა რამეს შეიყვანს
    print("Invalid Choice")