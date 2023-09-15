import random

def generate_random_number():
    return str(random.randint(1000, 9999))

def count_cows_and_bulls(secret_number, user_guess):
    cows = 0
    bulls = 0

    for i in range(4):
        if user_guess[i] == secret_number[i]:
            cows += 1
        elif user_guess[i] in secret_number:
            bulls += 1

    return cows, bulls

def main():
    secret_number = generate_random_number()
    num_guesses = 0

    print("Welcome to the Cows and Bulls Game!")

    while True:
        user_guess = input("Enter a 4-digit number: ")

        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        num_guesses += 1
        cows, bulls = count_cows_and_bulls(secret_number, user_guess)

        print(f"{cows} cows, {bulls} bulls")

        if cows == 4:
            print(f"Congratulations! You guessed the correct number {secret_number} in {num_guesses} guesses.")
            break

if __name__ == "__main__":
    main()