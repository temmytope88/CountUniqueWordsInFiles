import random

def game():
  print("This is a rock, scissors and paper game\n")
  print("Enter P for PAPER, S for SCISSORS or R for ROCK\n")
  b = input("input r for rock, p for paper and s for scissors\n")
  while b not in ["P", "p", "R", "r", "S", "s"]:
    print("INALID INPUT: Enter P, R or S\n")
    b = input("input r for rock, p for paper and s for scissors\n")
  
  myList = ["rock", "paper", "scissors"]

  a = random.choice(myList)
  
  if b == "r":
    if a == "rock":
      print("Player(Rock) : CPU(Rock)\n")
      print("YOU DRAW\n")
      game()
    elif a == "paper":
      print("Player(Rock) : CPU(Paper)\n")
      print("Paper cover Rock YOU LOSE\n")
    else:
      print("Player(Rock) : CPU(Scissors)\n")
      print("Rock blunt Scissors YOU WIN\n")
  elif b == "p":
    if a == "rock":
      print("Player(Paper) : CPU(Rock)\n")
      print("Paper cover Rock YOU WIN\n")
    elif a == "paper":
      print("Player(Paper) : CPU(Paper)\n")
      print("YOU DRAW\n")
      game()
    else:
      print("Player(Paper) : CPU(Scissors)\n")
      print("Scissors cut Paper YOU LOSE")
  else:
    if a == "rock":
      print("Player(Scissors) : CPU'(Rock)\n")
      print("Rock blunt Scissors YOU LOSE")
    elif a == "paper":
      print("Player(Scissors) : CPU(Paper)\n")
      print("Scissors cut Paper YOU WIN")
    else:
      print("Player(Scissors) : CPU(Scissors)\n")
      print("computer choose scissors, YOU DRAW\n")
      game()
  repeatProgarm()
  
      
def repeatProgarm():
  again = input("\nDo you want to play again? enter Y for YES and N for NO\n")
  while again not in ["Y", "y", "N", "n"]:
   print("INALID INPUT: Enter Y or N\n")
   again = input("Do you want to play again? enter Y for YES and N for NO\n")
   
  if again == "Y" or again == "y":
      print("Restarting game...\n")
      game()
  elif again == "N" or "n":
      print("Exiting the game...\n")
      return 1
game()

    