# მომხმარებელს ვთხოვთ ორი რიცხვის შემოყვანას
number = int(input("შემოიყვანეთ გასაყოფი რიცხვი: "))
divisor = int(input("შემოიყვანეთ გამყოფი რიცხვი: "))

# თავიდანვე უნდა შევამოწმოთ, რომ გამყოფი არ იყოს 0, რადგან ნულზე გაყოფა შეუძლებელია
if divisor == 0:
    print("შეცდომა: ნულზე გაყოფა შეუძლებელია!")
else:
    # ვამოწმებთ გაყოფადობას
    if number % divisor == 0:
        print(f"დიახ, {number} იყოფა {divisor}-ზე უნაშთოდ.")
    else:
        remainder = number % divisor
        print(f"არა, {number} არ იყოფა {divisor}-ზე უნაშთოდ. ნაშთია: {remainder}")