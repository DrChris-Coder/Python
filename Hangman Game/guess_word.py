import random
import os

# Game variables
word_to_guess = ""
string_to_display = ""
length_of_word_to_guess = 0
letters_to_guess = []
letters_guessed = []
new_letter = ""
nb_attempts = 1
max_nb_attempts = 5
stay_in_loop = True
word_list_path = "Hangman Game\hangman_words.txt"
def load_words_from_file(path):
    if not os.path.exists(path):
        print(f"❌ Word file not found at {path}")
        return ["PYTHON"]  # fallback word
    with open(path, "r") as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return words if words else ["PYTHON"]

def init_game():
    global word_to_guess, string_to_display, length_of_word_to_guess
    global letters_to_guess, letters_guessed, new_letter, nb_attempts, stay_in_loop

    words = load_words_from_file(word_list_path)
    word_to_guess = random.choice(words)
    length_of_word_to_guess = len(word_to_guess)
    letters_to_guess = list(word_to_guess)
    letters_guessed = [False] * length_of_word_to_guess
    string_to_display = "?" * length_of_word_to_guess
    nb_attempts = 1
    stay_in_loop = True
    print("\n🎮 New game started!\n")

def game_loop():
    global stay_in_loop
    while stay_in_loop:
        display_letters()
        check_keyboard()

def display_letters():
    print("\nWord to guess:", string_to_display)

def check_keyboard():
    global string_to_display, letters_guessed, new_letter
    global nb_attempts, stay_in_loop

    new_letter = input(f"Attempt {nb_attempts}/{max_nb_attempts} > ").upper()

    if not new_letter.isalpha() or len(new_letter) != 1:
        print("❌ Please enter a single valid letter.")
        return

    found = False
    for i in range(length_of_word_to_guess):
        if not letters_guessed[i] and letters_to_guess[i] == new_letter:
            letters_guessed[i] = True
            string_to_display = replace_char_at_index(string_to_display, new_letter, i)
            found = True

    if not found:
        print("❌ Letter not in word.")
        nb_attempts += 1

    if nb_attempts > max_nb_attempts:
        print(f"\n😞 You lost! The word was: {word_to_guess}")
        stay_in_loop = False
        return

    if all(letters_guessed):
        print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
        stay_in_loop = False

def replace_char_at_index(string, new_char, index):
    return string[:index] + new_char + string[index + 1:]

def main_menu():
    while True:
        print("\n======================")
        print("🎲 HANGMAN GAME MENU 🎲")
        print("======================")
        print("1. Start New Game")
        print("2. Quit")
        choice = input("Choose an option (1 or 2): ")

        if choice == "1":
            init_game()
            game_loop()
            prompt_return_to_menu()
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

def prompt_return_to_menu():
    while True:
        response = input("\n🔁 Return to main menu? (y/n): ").strip().lower()
        if response == "y":
            return
        elif response == "n":
            print("👋 Thanks for playing!")
            exit()
        else:
            print("❌ Please enter 'y' or 'n'.")

# Start the game
main_menu()