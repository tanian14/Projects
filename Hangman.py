import random

word_file = open("RealWordlist.txt")
word_file_list = []
for line in word_file.readlines():
    word_file_list.append(line.strip())

random_word = random.choice(word_file_list)
split_random_word_list = [char for char in random_word]

'''
split_tandom_word_list = []
for char in random_word:
    split_tandom_word_list.append(char)
'''

print(len(random_word), "letter in word")
turns = 10
mlist = ["?"] * len(random_word)
guess_list = []

while turns > 0:
    guess = input('Enter a letter: ').lower()
    if guess == "":
        print("You didn't type anything you dummy")
        continue
    if guess in split_random_word_list:
        repetition = split_random_word_list.count(guess)
        idx = 0
        for x in range(0, repetition):
          position = split_random_word_list.index(guess, idx)
          mlist[position] = guess
          idx = position + 1

    if guess not in guess_list:
        guess_list.append(guess)
        guess_list.sort()
        print("Guessed letters:", guess_list)
        
    else:
        print("You already guessed this letter dummy")
        print("Guessed letters:", guess_list)
        print()
        continue
    
    for x in mlist:
        print(x, end = " ")
    print()
    if "?" not in mlist:
        print("Congrats! You guessed the word! The man lives another day.")
        break
            
    if guess not in split_random_word_list:
        turns -= 1
        print("Wrong letter, try again")
        print("You have ", + turns, "guesses left")
        print()
        if turns == 0:
            print(random_word)
            print("YOU LOSE! There's a dead man's blood on your hands.")
            
    else:
        print("Correct! Would you like to guess the word? If you don't want to guess enter: no")
        print()
        word_guess = input("Guess the word: ")
        print()

        if word_guess == random_word:
            print("Congrats! You guessed the word! The man lives another day.")
            break

        elif len(word_guess) <= 2:
            print("Guess again")

        else:
            print("Uh Oh! That wasn't the correct word!")
            turns -= 1
            print("You have ", + turns, "guesses left")
