try:
    user_name = (input("Enter your Name :"))
    password = (input("Enter your password :"))
    age = float(input("Enter your age :"))

    if len(user_name) < 5 or len(password) < 8 or age < 18 :
        print(f"Acess denied")

        if len (user_name) < 5:
            print("Username must be 5 chars")
        if len (password) < 8 :
            print("Password must be 8 chars")
        if age < 18 :
            print("Age must be over 18")
    else :
        print(f"Access granted")

except ValueError :
    print("Error : Please enter valid age")