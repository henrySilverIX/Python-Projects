import random
import hangman_art
import hangman_words_en
import hangman_words_pt

print(hangman_art.logo)
print("Welcome to Hangman!!")
#Declare a list of the underscores symbols. It's the game's display
blanks = []

chosen_lg = input("Do you wanna play this game in English or Portuguese?\n").lower()
#A random word in the list of words will be chosen and stored
if chosen_lg == "english":
    chosen_word = random.choice(hangman_words_en.word_list)
else:
    chosen_word = random.choice(hangman_words_pt.lista_de_palavras)


#Number of player lives
lives = 6



#Put underscores in the blanks list. The number of underscore is equal to the number of letters
for blank in range(0, len(chosen_word)):
    blanks.append('_')


end_of_game = False
guessed_letter = ''
chosen_letters = []
correct_chosen_letters = []
chosen_letters_incorrect = []


print(blanks)
print("---------------------------")

while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()
    chosen_letters.append(guessed_letter)
    print("#######################")


    if guessed_letter in blanks:
        print("You've already chosen this letter")
        print(hangman_art.stages[lives])
        print(blanks)
        print("#####################")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

#Check if the letter is in the chosen word
        if letter == guessed_letter:
            blanks[position] = letter
            print(blanks)


#Print both the correct letters and the incorrect letters for the player
            correct_chosen_letters.append(letter)
            print("Correct letters: ", end="")
            print(correct_chosen_letters)

            print("Incorrect letters: ", end="")
            print(chosen_letters_incorrect)

#Print the chosen letters for the player
            print("Chosen letters: ", end="")
            print(chosen_letters)
            print("#####################")

#Check if the letter is not in the chosen word
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"You've chosen an incorrect letter {chosen_letters}")
        print(hangman_art.stages[lives])
        print(blanks)
        chosen_letters_incorrect.append(guessed_letter)

#Print both the correct letters and the incorrect letters for the player
        print("Correct letters: ", end="")
        print(correct_chosen_letters)

        print("Incorrect letters: ", end="")
        print(chosen_letters_incorrect)

#Print the chosen letters for the player
        print("Chosen letters: ", end="")
        print(chosen_letters)
        print("#####################")

#Finish the game when the number of lives reach to zero. In this case, you lose
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"Answer: {chosen_word}")

#Finish the game when the number of blanks reach to zero. In this case, you win
    if "_" not in blanks:
        end_of_game = True
        print("Congratulation! You won!")


print(blanks)
