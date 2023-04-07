import random
from hangman_words import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# print logo from hangman_art
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check if you enter the already guessed letter
    if guess in display:
      print(f"you already guessed the letter {guess}. Try again")
  
    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      print("oops that letter is not in the word . you lose life")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
      end_of_game = True
      print("You win.")
      
print(stages[lives])

