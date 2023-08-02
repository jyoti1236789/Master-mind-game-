import random

def get_secret_number():
    # Generates a random 4-digit number as the secret number for Player 1
    return ''.join(random.sample('0123456789', 4))

def get_bulls_and_cows(secret_number, guess):
    # Calculates the number of bulls and cows for a given guess
    bulls = 0
    cows = 0
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def player1_guess(secret_number):
    # Player 1's turn to guess the number set by Player 2
    attempts = 0
    while True:
        attempts += 1
        guess = input("Player 1, enter your guess: ")
        
        if guess == secret_number:
            print(f"Congratulations! Player 1 guessed the number {secret_number} in {attempts} attempts.")
            return attempts
        else:
            bulls, cows = get_bulls_and_cows(secret_number, guess)
            print(f"Bulls: {bulls}, Cows: {cows}")

def player2_guess():
    # Player 2's turn to set the secret number
    secret_number = input("Player 2, enter a 4-digit number as the secret number: ")
    return secret_number

def main():
    print("Welcome to the Mastermind game!")

    # Player 2 sets the secret number
    secret_number = player2_guess()

    # Player 1 guesses the number set by Player 2
    player1_attempts = player1_guess(secret_number)

    # Player 2's turn to guess the number set by Player 1
    secret_number = get_secret_number()

    # Player 2 guesses the number set by Player 1
    player2_attempts = 1
    while True:
        guess = input("Player 2, enter your guess: ")
        
        if guess == secret_number:
            print(f"Congratulations! Player 2 guessed the number {secret_number} in {player2_attempts} attempt.")
            break
        else:
            player2_attempts += 1
            bulls, cows = get_bulls_and_cows(secret_number, guess)
            print(f"Bulls: {bulls}, Cows: {cows}")

    # Compare the number of attempts by both players to determine the winner
    if player1_attempts < player2_attempts:
        print("Player 1 wins! Congratulations, Player 1, you are crowned Mastermind!")
    elif player1_attempts > player2_attempts:
        print("Player 2 wins! Congratulations, Player 2, you are crowned Mastermind!")
    else:
        print("It's a tie! Both players are Masterminds!")

if __name__ == "__main__":
    main()
