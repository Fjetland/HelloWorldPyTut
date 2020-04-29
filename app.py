secretNumber = 9
guessCount = 0
maxGuesses = 5
while guessCount < maxGuesses:
    guess = int(input("Guess a number: "))
    guessCount+=1
    if secretNumber == guess:
        print("Yey you won!")
        break
    else:
        print("Looser, try again!")
        if guess < secretNumber:
            print("Guess higher")
        else:
            print("Guess lower")
else:
    print("You lost the simple game!")
print("Awsome game has exited the building")