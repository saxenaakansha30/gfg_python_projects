import random

print("Enter the lower bond of the range")
lower = int(input());
print("Enter the higher bound of the range")
higher = int(input());

if lower > higher:
  print("Please select the lower as smaller than higher")
no = random.randrange(lower, higher, 1)

print("Rules: You have unlimited tries, play it and guess the number. The game will help you with every wrong guess by narrowing the search space. Try you rbest to guess with least tries. Good luck!!")

tries = 0

while True:
  tries += 1
  print("Guess the number: ")
  user_guess = int(input())

  if user_guess == no:
    print("Excellent work!! you have guessed it right in tries: " + str(tries))
    break
  elif user_guess < no:
    lower = user_guess + 1
    print("Too low!!")
  else:
    higher = user_guess - 1
    print("To high")

  print("Let me help you and narrow down the search range from " + str(lower) + " to " + str(higher))
  print("Try again.")
