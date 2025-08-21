# name of who asks and what the qestion is
name = "Gage"

question = "Does my mom love me?"



# checks for question
if not question:
  print("You forgot to ask first, dumby!")
else:

  #option 1:

  #import random number generation
  import random

  # which side the 9 sided dice lands on after being shaken
  side = random.randint(1, 9)

  # what answer it gives depending on what side
  print(name , "asks: \n" + question, "\n")

  print("Magic 8-Ball's answer: ")

  if side == 1:
    print("Yes - definitely")
  elif side == 2:
    print("It is decidedly so")
  elif side == 3:
    print("Without a doubt")
  elif side == 4:
    print("Reply hazy, try again")
  elif side == 5:
    print("Ask again later")
  elif side == 6:
    print("Better not tell you now")
  elif side == 7:
    print("My sources say no")
  elif side == 8:
    print("Outlook not so good")
  elif side ==9:
    print("Very doubtful")
  else:
    print("Error")
# option 2

# import random answer generater

# "import random" (place holder)

  #answer list
  answer_list = ["Yes - definitely","It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now",  "My sources say no", "Outlook not so good"]

  # chooses randomly from list
  answer = random.choice(answer_list)

  # prints answer
  print("\n.....................................\n")
  print(name , "asks: \n" + question, "\n")

  print("Magic 8-Ball's answer: ")
  print(answer)




