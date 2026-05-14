# მომხმარებელს ვთხოვთ ასაკისა და წონის შეყვანას
age = int(input("შემოიყვანეთ თქვენი ასაკი: "))
weight = float(input("შემოიყვანეთ თქვენი წონა (კგ): "))

# 1. ჯგუფი: ასაკი < 10
if age < 10:
    if weight < 20:
        print("წონა დაბალია")
    elif 20 <= weight <= 40:
        print("წონა ნორმალურია")
    else: # ანუ weight > 40
        print("წონა მაღალია")

# 2. ჯგუფი: ასაკი 10-17
elif 10 <= age <= 17:
    if weight < 40:
        print("წონა დაბალია")
    elif 40 <= weight <= 65:
        print("წონა ნორმალურია")
    else: # ანუ weight > 65
        print("წონა მაღალია")

# 3. ჯგუფი: ასაკი 18 ან მეტი
else:
    if weight < 50:
        print("წონა დაბალია")
    elif 50 <= weight <= 90:
        print("წონა ნორმალურია")
    else: # ანუ weight > 90
        print("წონა მაღალია")
        