### word Radier Game
import random
import time

def slow_print(text, delay=0.03):
 for char in text:
   print(char, end='', flush=True)
   time.sleep(delay)
 print()  # for newline after the text is printed

GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"


with open("word_bank.txt", "r") as file:
  random_five_letter_words = file.read().splitlines()

with open("word_bank_six_letter_words.txt", 'r') as file:
   six_letter_words_list = file.read().splitlines()

with open("seven_letter_word_bank.txt", 'r') as file:
    seven_letter_words_list = file.read().splitlines()



def five_letter_words():
  slow_print("Welcome to our game!")
  slow_print("You will try to guess a five letter word and if you guess right you win!")
  random_word = random.choice(random_five_letter_words)
  slow_print(f"You random word is: {random_word}")  # For testing purposes; remove in production
  for attempt in range(6):
    guess = input("Enter a five letter word:").lower()
    if len(guess) != 5 or not guess.isalpha():
      slow_print("Invalid input. Please enter a five letter word.")
      continue
    if guess == random_word:
      slow_print("Congratulations! You've guessed the word correctly!")
      break
    else:
      feedback = []
      for i in range(5):
        if guess[i] == random_word[i]:
            feedback.append(f"[{GREEN}{guess[i].upper()}{RESET}]")  # Correct letter and position
        elif guess[i] in random_word:
            feedback.append(f"({YELLOW}{guess[i].upper()}{RESET})")  # Correct letter, wrong position
        else:
            feedback.append(f"{GRAY}{guess[i].upper()}{RESET}" )  # Incorrect letter
      slow_print("Feedback: " + " ".join(feedback))

def six_letter_words():
   slow_print("Welcome to the six letter word game!")
   slow_print("You will try to guess a six letter word and if you guess right you win!")
   random_six_letter_word = random.choice(six_letter_words_list)
   slow_print(f"Your random six letter word is: {random_six_letter_word}")  # For testing purposes; remove in production
   for attempt in range(6):
      guess = input("Enter a six letter word:").lower()
      if len(guess) != 6 or not guess.isalpha():
        slow_print("Invalid input. Please enter a six letter word.")
        continue
      if guess == random_six_letter_word:
         slow_print("Congratulations! You've guessed the word correctly!")
         break
      else:
         feedback = []
         for i in range(6):
            if guess[i] == random_six_letter_word[i]:
               feedback.append(f"[{GREEN}{guess[i].upper()}{RESET}]")  # Correct letter and position
            elif guess[i] in random_six_letter_word:
               feedback.append(f"({YELLOW}{guess[i].upper()}{RESET})")  # Correct letter, wrong position
            else:
                feedback.append(f"{GRAY}{guess[i].upper()}{RESET}")  # Incorrect letter
         slow_print("Feedback: " + " ".join(feedback))
   
def seven_letter_words():
   slow_print("Welcome to the seven letter word game!")
   slow_print("You will try to guess a seven letter word and if you guess right you win!")
   random_seven_letter_word = random.choice(seven_letter_words_list)
   slow_print(f"Your random seven letter word is: {random_seven_letter_word}")  # For testing purposes; remove in production
   for attempt in range(6):
      guess = input("Enter a seven letter word:").lower()
      if len(guess) != 7 or not guess.isalpha():
         slow_print("Invalid input. Please enter a seven letter word.")
         continue
      if guess == random_seven_letter_word:
         slow_print("Congratulations! You've guessed the word correctly!")
         break
      else:
         feedback = []
         for i in range(7):
            if guess[i] == random_seven_letter_word[i]:
               feedback.append(f"[{GREEN}{guess[i].upper()}{RESET}]")  # Correct letter and position
            elif guess[i] in random_seven_letter_word:
               feedback.append(f"({YELLOW}{guess[i].upper()}{RESET})")  # Correct letter, wrong position
            else:
                feedback.append(f"{GRAY}{guess[i].upper()}{RESET}")  # Incorrect letter
         slow_print("Feedback: " + " ".join(feedback))

def menu():
   slow_print("Welcome to Word Raider!")
   slow_print("Choose a game mode:")
   slow_print("1. Five letter words")
   slow_print("2. Six letter words") 
   slow_print("3. Seven letter words")
   user_input = input("Enter 1, 2, or 3:")
   if user_input == "1":
     five_letter_words()
   elif user_input == "2":
    six_letter_words()
   elif user_input == "3":
    seven_letter_words()
   else:
    slow_print("Invalid input. Please enter 1, 2, or 3.")


menu()


