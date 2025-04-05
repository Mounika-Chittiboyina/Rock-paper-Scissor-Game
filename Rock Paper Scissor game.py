rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choice = input(("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)
else:
    print("Wrong Choice.")

print("Computer Chose:")

options = [rock, paper, scissors]
num_index = random.randint(0,2)
print(options[num_index])

if choice == "0" and num_index == 0 :
    print("It's a draw")
elif choice == "0" and num_index == 1 :
    print("You Lose")
elif choice == "0" and num_index == 2 :
    print("You win")
elif choice == "1" and num_index == 0 :
    print("You Win")
elif choice == "1" and num_index == 1 :
    print("It's a Draw")
elif choice == "1" and num_index == 2 :
    print("You Lose")
elif choice == "2" and num_index == 0 :
    print("You Lose")
elif choice == "2" and num_index == 1 :
    print("You Win")
elif choice == "2" and num_index == 2 :
    print("It's a Draw")
else:
    print("Wrong Choice")
