def greetUser(firstName ="NoFirst", lastName =""):
    """
    One awesome greeting function
    :type firstName: str
    :type lastName: str
    """
    print(f"Hi {firstName} {lastName}!")
    print("Welcome aboard")


def square(number):
    return number * number


print("Start")
greetUser("Andreas", "Fjetland")
greetUser("Christine", lastName="Ødegård")
greetUser()
print("Finish")

print("Square function example")
print(square(3))