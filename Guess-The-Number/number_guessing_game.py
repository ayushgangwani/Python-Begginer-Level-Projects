import random

print("WELCOME TO NUMBER GUESSING GAME !!")
print("I HAVE SELECTED A NUMBER BETWEEN 1 TO 100. TRY TO GUESS IT !!")

while True:
    computerGuess = random.randint(1,100)
    count = 0
    while True:
        try:
            userGuess = int(input("Guess the number between 1 to 100 : "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if userGuess==computerGuess:
            count += 1
            print("Congratulations !!!!!")
            print("You guessed correct in " + str(count) + " attempt") 
            break
        elif userGuess > computerGuess:
            count += 1
            print("Too high")
        elif userGuess < computerGuess:
            count += 1
            print("Too low") 
    user = input("Wanna Play Again (yes/no) ?")
    if user == "no" or user == "No" or user == "NO":
        break

    