import random

words = ['Sun', 'Moon', 'Earth', 'Planet', 'Galaxy', 'Star', 'Cosmos', 'Stellar', 'Astro']  #Astronomy themed words
word = random.choice(words)

lowercase_word = word.lower()   #converts all letters to lowercase for easier comparison with user input

list_word = list(word)

for letter_count in range(len(list_word)):
    list_word[letter_count] = '_'   #converts all letters in the chosen word to underscores equal to the number of letters in the word


def list_to_str(my_list):   #converts strings to lists, I did this because strings are immmutable in Python, but I'm sure there's a better way to do this
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
    check_letter = input("\nGuess a letter: ").lower()  #Again, converting everything to lowercase for easier comparison
    if check_letter == '':
        print("Character not entered. Try again.")
    elif check_letter in lowercase_word:
        print("You guessed a correct letter!")
        list_word = list(word)
        for letter_count in range(len(list_word)):
            if list_word[letter_count].lower() == check_letter or list_word[letter_count] in guessed_letters:
                continue
            list_word[letter_count] = '_'   #This loop replaces every letter other than what was just guessed or has been already guessed in previous iterations by an underscore

        updated_unknown_word = list_to_str(list_word)   #this variable represents the updated list, with some underscores and some guessed letters to show progress
        print(updated_unknown_word

        for i in range(len(updated_unknown_word)):
            if updated_unknown_word[i] != '_':
                guessed_letters += updated_unknown_word[i]  #adds the letter which was just guessed to the list of already guessed letters

        if '_' not in updated_unknown_word:
            break   #exits the loop if no unknown letters remaning

    else:
        print("Oops! Wrong guess! You lose one life.")
        life -= 1
        print("Remaining lives:", life)

if life == 0:
    print("Game over! You lose all lives.")
else:
    print("You win!")
