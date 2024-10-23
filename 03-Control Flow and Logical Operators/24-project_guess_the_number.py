import random 

def game_is_on():
    number_to_guess = random.randint(1,20)
    limit_of_attempts = 6

    print("Welcome to the 'Guess the Number'game! 🎲")
    print("...", end="\n")
    print("🤖 I have chosen a number between 1 and 20.")
    print(".\n.\n.")
    print(f"You have {limit_of_attempts} attempts to guess it. 🥵")
    print("...", end="\n")

    for attempt in range(1, limit_of_attempts + 1):
        if limit_of_attempts <= 6:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        else:
            print("Game over!🚫")
            print(f"Sorry, you've used all your attempts. The correct number was: {number_to_guess}")
            exit()

        if guess < 1 or guess > 20:
                print("Your guess is out of bounds! Please guess a number between 1 and 20.⚠️")
                continue
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
            break
game_is_on()