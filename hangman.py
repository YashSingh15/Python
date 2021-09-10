import random

words = ['Sun', 'Moon', 'Earth', 'Planet', 'Galaxy', 'Star', 'Cosmos', 'Stellar', 'Astro']  #Astronomy themed words
word = random.choice(words)

lowercase_word = word.lower()

list_word = list(word)

for letter_count in range(len(list_word)):
    list_word[letter_count] = '_'


def list_to_str(my_list):
    string = ""
    for letter in my_list:
        string += letter

    return string


unknown_word = list_to_str(list_word)

print(unknown_word, f"({len(word)})")

starting_life = 5

life = starting_life

guessed_letters = []

while life > 0:
    check_letter = input("\nGuess a letter: ").lower()
    if check_letter == '':
        print("Character not entered. Try again.")
    elif check_letter in lowercase_word:
        print("You guessed a correct letter!")
        list_word = list(word)
        for letter_count in range(len(list_word)):
            if list_word[letter_count].lower() == check_letter or list_word[letter_count] in guessed_letters:
                continue
            list_word[letter_count] = '_'

        updated_unknown_word = list_to_str(list_word)
        print(updated_unknown_word)

        for i in range(len(updated_unknown_word)):
            if updated_unknown_word[i] != '_':
                guessed_letters += updated_unknown_word[i]

        if '_' not in updated_unknown_word:
            break

    else:
        print("Oops! Wrong guess! You lose one life.")
        life -= 1
        print("Remaining lives:", life)

if life == 0:
    print("Game over! You lose all lives.")
else:
    print("You win!")
