import random

name = input ('What is your name? ')
question = input ("Enter your question? ")
answer = ""
random_number = random.randint(1, 13)
print(random_number)

if len(name) == "":
  print("Question: " + question)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hacy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Lets pop the champagne"
elif random_number == 11:
  answer = "You lucky bastard"
elif random_number == 12:
  answer = "It will blow your mind"
elif random_number == 13:
  answer = "You can't handle the trouth"
else:
  answer = "Error"
print(name + " asks: " + question)
print("Magic 8-Balls's answer: " + answer)
