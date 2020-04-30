is_running = False
inn = ""
while True:
    inn = input(">").upper()
    if inn == "HELP":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif inn == "START":
        if is_running:
            print("Car is already running.")
        else:
            is_running = True
            print("Car started... Ready to go!")
    elif inn == "STOP":
        if not is_running:
            print("Car is not on.")
        else:
            is_running = False
            print("Car stopped.")
    elif inn == "quit":
        break
    else:
        print("I don't understand that")
print("Bye Bye")