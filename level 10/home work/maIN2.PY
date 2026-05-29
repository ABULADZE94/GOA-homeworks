# Bonus:
# 5) გააკეთეთ რეგისტრაციის და ავტორიზაციის შესახებ CLI (Command Line Interface):
# როდესაც პროგრამა გაეშვება მომხმარებელს უნდა გამოუვიდეს მსგავსი რაღაცა:
# 1. Registration
# 2. Login
# 3. Stop Programm
# როდესაც მომხმარებელი აირჩევს რეგისტრაციას:
# მოსთხოვეთ მისი user name, email და password, შემდგომ ეს ინფორმაცია შეინახეთ user სიაში ან 
# შექმენით შესაბამისი ცვლადები და გამოუტანეთ შეტყობინება "Registration successfully!", ასევე გადაიყვანეთ მომხმარებელი საწყის menu - ში ანუ  ისევ გამოუტანეთ:
# 1. Registration
# 2. Login
# 3. Stop Programm
# როდესაც მომხმარებელი აირჩევს ლოგინს:
# მოსთხოვეთ მისი email - ი და password - ი, თუ არასწორი იქნება რაიმე გამოუტანეთ შესაბამისი შეტყობინება, თუ სწორია იქნება ინფორმაცია მაშინ გამოუტანეთ "Login successfully!" და გათიშეთ პროგრამა.
# თუ აირჩია Stop Programm მაშინ გათიშეთ პროგრამა.
# როდესაც გააკეთებთ დავალებას აუცილებლად ახსენით მთლიანი კოდი კომენტარებით.
saved_username = ""
saved_email = ""
saved_password = ""
while True:
    print("registartion")
    print("login")
    print("stop program")

    choice = input("airchie ert erti:")

    if choice == "registartion":
        username = input("enter username:")
        email = input("enter your email")
        password = input("enter your password")

        saved_username =  username
        saved_email = email
        saved_password = password
        print("Registration successfully!")

    elif choice =="login":
        login_email = input("enter your email")
        login_password = input("enter your password")
        if login_email == saved_email:
            login_password == saved_password:
            print("login successfully")
        else:
            print("incorect email or password")
            
    elif choice == "stop program":
     print("you stoped program")
      #თავიდან რო გვიწერია saved_username, saved_email, saved_password, ეგ გვჭირდება იმისთვის რო შევინახოთ username,email,paasword. 
     #if ფუნქციის დახმარებით ჩვენ მომხმარებელს ვეუბნებით რომ შემოიყვანოს username,email,password. და შემდგომ ამ მონაცემებს ვინახავთ saved_username, saved_email, saved_password ში
     #elif ფუნქციის დახმარებით მომხმარებელს შემოვაყვანინებთ თავის email,password და შემდგომ if ფუნქციის გამოყენებით თუ მომხმარებლის მიერ შემოყვანილი email,password უდრის უკვე შენახულ ემაილს,პაროლს გამოიტანს login sueccesfully
      #else ფუნქციით უბრალოდ მომხმარებელს ვეუბნებით რომ შემოიყვანოს სწორი ემაილი და პაროლი,
     # else ფუნქციით უბრალოდ  მომხმარებელი ასტოპებს პროგრამას