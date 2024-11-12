import random

def main():
    print("This is a number guessing game. Enter a range and you will have a number of tries to guess it.\n"
          "The tries are determined by the range entered. (Enter a wider range for more tries but it will be more difficult)")
    redo = "y"
    while redo == "y":
        low_range = validate_input("Enter the lower limit of your range (non-inclusive): ")
        high_range = validate_input("Enter the upper limit of your range (non-inclusive): ")
        if validate_range(low_range, high_range):
            generated_number = generate_random(low_range, high_range)
            lives = determine_lives(low_range, high_range)
            print(f"You have {lives} lives.")
            guessing_game(generated_number, lives)
        else:
            print("Lower limit must be smaller than upper limit and cannot be equal.\n")
        redo = input("Enter any character to end or y to play again: ")


def validate_input(prompt_text) -> int:
    error_flag = False
    user_input = int
    while not error_flag:
        try:
            user_input = int(input(prompt_text))
            error_flag = True
        except ValueError:
            print("Value entered must be a number.")
            error_flag = False
    return user_input

def generate_random(low, high) -> int:
    random_number = random.randint(low, high)
    return random_number

def guessing_game(gen_number, lives):
    while lives > 0:
        guessed = validate_input("Guess the number generated: ")
        if guessed == gen_number:
            print(f"Congrats, you won with {lives} live(s) remaining.")
            break
        elif guessed < gen_number:
            print(f"Too low. Aim higher. {lives-1} lives remaining.")
            lives -= 1
        elif guessed > gen_number:
            print(f"Too high. Aim Lower. {lives-1} lives remaining.")
            lives -= 1
    if lives == 0:
        print(f"Game over. You lose. The number was {gen_number}.")

def determine_lives(low, high):
    num_range = high - low
    if 0 < num_range < 25:
       return 3
    elif 25 < num_range < 50:
        return 5
    elif 50 < num_range < 75:
        return 7
    elif num_range > 75:
        return 10
    else:
        return 0

def validate_range(low, high):
    if low >= high:
       return False
    return True

if __name__ == "__main__":
    main()