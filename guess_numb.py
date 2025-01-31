
def guess_numb():
    from random import randint
    print(f"You have to guess a number between 1 and 100.")
    random_number = randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if user_guess < random_number:
                print(f"Your guess is too low.")
            elif user_guess > random_number:
                    print(f"Your guess is too high.")
            else:
                if user_guess == random_number:
                    print(f"Congrats! You guessed the number in {attempts} try.")
                    guessed = True
        except:
            print("Please enter a valid number.")

guess_numb()