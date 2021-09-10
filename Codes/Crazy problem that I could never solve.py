import random

bunny_words = ["perfect", "coder", "psychotomimetic", "omphaloskepsis", "bewilderment", "meandering", "brainstorming",
               "technology"]

naina_words = ["repfetc", "ocder", "cypstohctiemimo", "opaokpimhlsess", "redliwbetnem", "neeigmadrn", "naibrmrotmnig",
               "yglochetno"]



def elusive_generator(word):
    """Input: one strings
    Generates all possible elusive words of a given word
    Output: Returns a list of elusive words"""

    list_elusive = []

    for rand_index in range(len(bunny_word)):
        sub_str1 = bunny_word[0:rand_index + 1]
        sub_str2 = bunny_word[rand_index + 1:len(bunny_word)]

        boolean = random.choice([True, False])

        if boolean:
            elusive_word = sub_str1 + sub_str2
        else:
            elusive_word = sub_str2 + sub_str1

        elusive_generator(sub_str1)
        elusive_generator(sub_str2)

        string_adder(sub_str1, sub_str2)

        list_elusive += elusive_word

    return list_elusive

print(elusive_generator("perfect"))

def sub_string_generator(string, index, bool):
    str1 = word[0:index + 1]
    str2 = word[index + 1:len(word)]

    if bool:
        return str1
    else:
        return str2


def string_adder(str1, str2, bool):
    if bool:
        return str1 + str2
    else:
        return str2 + str1


def separator(word, index, bool):
    str1 = word[0:index + 1]
    str2 = word[index + 1:len(word)]

    if bool:
        return str1 + str2
    else:
        return str2 + str1

str1 = sub_string_generator("perfect", 3, True)
str2 = sub_string_generator("perfect", 3, False)

string = string_adder(str1, str2, True)

while len(str1) > 1 and len(str2) > 1:
    str1 = sub_string_generator(str1, 3, True)
    str2 = sub_string_generator(str2, 3, True)
