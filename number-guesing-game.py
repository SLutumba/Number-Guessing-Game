import random
def main():
    print("This is a number guessing game. Enter a range and you will have 3 tries to guess it.")
    low_range = validate_input("Enter the lower limit of your range (non-inclusive): ")
    high_range = validate_input("Enter the upper limit of your range (non-inclusive): ")
    while not verify_inputs(low_range, high_range):
        print("Upper limit and lower limit cannot be the same value.\n")
        low_range = validate_input("Enter the lower limit of your range (inclusive): ")
        high_range = validate_input("Enter the upper limit of your range (inclusive): ")
    generated_number = generate_random(low_range, high_range)
    guessing_game(generated_number)

def validate_input(prompt_text) -> int:
    error_flag = False
    user_input = int
    while not error_flag:
        try:
            user_input = input(prompt_text)
            user_input = int(user_input)
            error_flag = True
        except ValueError:
            print("Value entered must be a number.")
            error_flag = False
    return user_input

def verify_inputs(low, high):
    if low == high:
        return False
    return True

def generate_random(low, high) -> int:
    random_number = random.randint(low, high)
    return random_number

def guessing_game(gen_number):
    lives = 3
    while lives > 0:
        guessed = validate_input("Guess the number generated: ")
        if guessed == gen_number:
            print(f"Congrats, you won with {lives} live(s) remaining.")
        elif guessed < gen_number:
            print(f"Too low. Aim higher. {lives-1} lives remaining.")
            lives -= 1
        elif guessed > gen_number:
            print(f"Too high. Aim Lower. {lives-1} lives remaining.")
            lives -= 1
    if lives == 0:
        print(f"Game over. You lose. The number was {gen_number}.")


if __name__ == "__main__":
    main()