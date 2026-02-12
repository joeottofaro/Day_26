# Using pandas, list comprehension and dictionary comprehension
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def code():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_code = [new_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        code()
    else:
        print(phonetic_code)


code()
