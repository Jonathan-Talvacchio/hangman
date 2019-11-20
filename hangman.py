import os
import re
import sys
from sys import platform


def clear_term():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def set_word(deafult_word):
    secret_word = deafult_word

    return secret_word.lower()


def secret_display(secret_list, tries, used_letters):
    rebuilt_list = "".join(secret_list)
    rebuilt_used = ",".join(used_letters)
    display = f"{rebuilt_list.upper()}\n\nTries: {tries}\nLetters tried: {rebuilt_used.upper()}\n"

    print(display)
    return display


def game_main(default_word="mississippi"):
    # --init game--
    clear_term()
    currect_count = 0
    tries = 0
    secret_word = set_word(default_word)
    secret_list = list()
    used_letters = list()

    # --create secret word display--
    for letter in secret_word:
        if re.search("[^a-zA-Z-]", letter):
            secret_list.append(letter)
            currect_count += 1
        elif letter == "-":
            # --special case for - character--
            secret_list.append("(-)")
            currect_count += 1
        else:
            secret_list.append("-")

    secret_display(secret_list, tries, used_letters)

    while True:
        # --game loop start--
        usr_input = input("Type a letter: ")
        usr_input = usr_input.lower()
        usr_input = usr_input.replace(" ", "")

        # --check for win--
        if usr_input == secret_word:
            secret_list = usr_input

        # --check user input--
        # --if user input contains anything but a-z & A-Z--
        elif re.search("[^a-zA-Z]", usr_input) or len(usr_input) > 1:
            clear_term()
            secret_display(secret_list, tries, used_letters)
            print("Only single letter inputs")
            continue  # end loop here

        if usr_input == "":
            clear_term()
            secret_display(secret_list, tries, used_letters)
            print("No input found")
            continue  # end loop here

        # --if letter NOT already entered--
        if usr_input not in used_letters:
            # --if letter is NOT part of secret word--
            if usr_input not in secret_word:
                used_letters.append(usr_input)
                tries += 1
            else:
                letter_index = 0
                for letter in secret_word:
                    # --if user input matches secret word letter--
                    if usr_input == letter:
                        # --if secret word is more then one character--
                        if len(secret_word) > 1:
                            secret_list[letter_index] = letter
                        else:
                            secret_list = letter
                        currect_count += 1
                        # used_letters.append(usr_input)

                    letter_index += 1

            clear_term()
            secret_display(secret_list, tries, used_letters)
        else:
            clear_term()
            secret_display(secret_list, tries, used_letters)
            print(f"{usr_input.upper()}: was already entered")

        # --game win--
        if "".join(secret_list) == secret_word:
            clear_term()
            print("YOU WIN!!")
            _secret_display = secret_word.upper()
            print(f"{_secret_display}: was the secret word or phrase")
            print(f"It only took you {tries} tries!")

            # --game restart--
            usr_input = input("\nPlay again? [Y/n]: ")
            usr_input = usr_input.lower()
            if re.search("[n]", usr_input):
                clear_term()
                print("Quitting Hangman...")
                break
            else:
                clear_term()
                default_word = input("New secret word or phrase: ")
                game_main(default_word)


if __name__ == "__main__":
    clear_term()
    default_word = input("New secret word or phrase: ")
    game_main(default_word)
