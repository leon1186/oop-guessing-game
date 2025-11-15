import random
# Define your GuessingGame class here...
class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
    def guess(self, user_guess):
        if (user_guess > self.answer):
          return(f"Your answer is too high")
        elif (user_guess < self.answer):
          return(f"Your answer is too low")
        else:
           print(f"You guessed the correct answer")
    def solved(self, user_guess):
       if (user_guess == self.answer):
          return True
       else:
          return False
# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,100))
user_guess  = None
last_result = None
#counter = 1
#this part takes a user name and input
print('Welcome to the Guessing Game')
user_input = input("What is your name?: ")
print(f'Welcome {user_input}! Lets play!')
print(user_input)
user_guess = int(input("Pick a number"))
print(user_guess)
while game.solved(user_guess) == False:
  if (last_result is not None):
    print(f"Oops! {user_input} Your last guess ({user_guess}) was {last_result}.")
    #print(f"Youve guessed {counter} amount of times..")
    #counter += 1
  user_guess = int(input("Enter your guess: "))
  last_result = game.guess(user_guess)
  print("")
print(f"{user_guess} was correct!")