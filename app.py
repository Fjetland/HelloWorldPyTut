def greetUser(firstname ="NoFirst", lastname = ""):
    print(f"Hi {firstname} {lastname}!")
    print("Welcome aboard")


print("Start")
greetUser("Andreas", "Fjetland")
greetUser(lastname="Ødegård", firstname="Christine")
greetUser()
print("Finish")