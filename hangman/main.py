import random

word_list = ['bola', 'camaleao', 'paralelepipedo', 'praia', 'condominio']
chosen_word = random.choice(word_list)

placeholder = ""

for position in range(1, len(chosen_word)):
    placeholder += "_"

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
