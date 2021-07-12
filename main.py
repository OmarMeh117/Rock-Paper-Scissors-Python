# Omar Mehmood Rock Paper Scissors 7/12/2021
import random

print("Welcome to Rock Paper Scissors")
print("1) Rock\n2) Paper\n3) Scissors")
player_choice = int(input("What do you choose: "))

computer = random.randint(1, 3)

# if the player and the computer get a tie
if player_choice == 1 and computer == 1:
    print("you both chose rock!")
    print('''
/\                    /\-
\ \                  / /
 \ \                / /
  \.\              /./
   \.\            /./
    \.\          /./
     \.\        ///
      \.\      /./
       \.\    /./
        \.\__/./
       _/)))(((\_
       \|)\##/(|/
       _|)/##\(|_
       \|)))(((|/
        /o/  \o\-
       /o/    \o\-
      /_/      \_\-         ITS A TIE! 
    ''')
elif player_choice == 2 and computer == 2:
    print("Its a tie! you both chose paper!")
    print('''
/\                    /\-
\ \                  / /
 \ \                / /
  \.\              /./
   \.\            /./
    \.\          /./
     \.\        ///
      \.\      /./
       \.\    /./
        \.\__/./
       _/)))(((\_
       \|)\##/(|/
       _|)/##\(|_
       \|)))(((|/
        /o/  \o\-
       /o/    \o\-
      /_/      \_\-         ITS A TIE! 
    ''')
elif player_choice == 3 and computer == 3:
    print("Its a tie! you both chose scissors!")
    print('''
/\                    /\-
\ \                  / /
 \ \                / /
  \.\              /./
   \.\            /./
    \.\          /./
     \.\        ///
      \.\      /./
       \.\    /./
        \.\__/./
       _/)))(((\_
       \|)\##/(|/
       _|)/##\(|_
       \|)))(((|/
        /o/  \o\-
       /o/    \o\-
      /_/      \_\-         ITS A TIE! 
    ''')
# if the player wins
if player_choice == 1 and computer == 3:
    print("You picked rock, the computer picked scissors")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)         YOU WON!
    """)
elif player_choice == 2 and computer == 1:
    print("You picked paper, the computer picked rock")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)         YOU WON!
    """)
elif player_choice == 3 and computer == 2:
    print("You picked scissors, the computer picked paper")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)         YOU WON!
    """)
# if the player loses
if player_choice == 3 and computer == 1:
    print("You picked scissors, the computer rock")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)         YOU LOST!
    """)

elif player_choice == 1 and computer == 2:
    print("You picked rock, the computer picked paper")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)         YOU LOST!
    """)
elif player_choice == 2 and computer == 3:
    print("You picked paper, the computer picked scissors")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)         YOU LOST!
    """)
