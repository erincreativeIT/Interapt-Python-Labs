# Let's play craps!
# Rules:
#   Player rolls dice
#   If player rolls 7 or 11 on first roll, game over, player wins
#   If player rolls 2, 3, or 12 on first roll, player loses
#   If player rolls 4-10, what they roll is the POINT
#   Player continues to roll until:
#       they roll the POINT - they win
#       they roll a seven, they lose
from random import randint

def roll_dice_return_results():
   _ = input("Enter anything to roll the dice the first time ==>")
   return randint(1,6), randint(1,6)
  

#Loop, asking if u wanna play again
while input("Wanna play again? (Y/N) ==> ").upper() == "Y":
  both_dice = roll_dice_return_results()
  dice_1, dice_2 = roll_dice_return_results()

  if dice_1 + dice_2 in (7,11):
    print(f"You WIN on first roll by rolling a {dice_1 + dice_2}!!!!!")
    # If player rolls 2, 3 or 12 on first roll, player loses
  elif dice_1 + dice_2 in (2,3, 12):
    print(f"You crapped out by rolling a {dice_1 + dice_2}!!!!!")
  else:
    point = dice_1 + dice_2
    print(f'You rolled a {point}. Roll until you match {point} or roll a 7')

    while True:
      # If we get here, a player rolls until they get a 7 (lose) or make
      # POINT (they win)
      dice_1, dice_2 = roll_dice_return_results()

      print(f'You rolled a {dice_1 + dice_2}')

      if dice_1 + dice_2 == point:
        print(f"You WIN by matching POINT {point}!!!!!")
        break
      if dice_1 + dice_2 == 7:
        print("You LOSE by rolling a 7!!!!!")
        break
  
  
  # Could do randint(2,12) but using two dice allows for further expansion of craps
  # roll = randint(2,12) 
  # If player rolls 7 or 11 on first roll, game over, player wins......
  #original_point = dice_1 + dice_2 
  #if original_point in (7,11):
   # print(f"You WIN on first roll by rolling a {original_point}!!!!!")

    # If player rolls 2, 3 or 12 on first roll, game over, player loses
  #elif original_point in (2,3, 12):
   # print(f"You WIN on first roll by rolling a {original_point}!!!!!")
    # If player rolls 4-10, what they roll is the POINT
    # Player continues to roll until:
    # they roll the POINT - they win
    # they roll a seven, they lose
  #else:
    #print(f'You rolled a {original_point} on the first roll\Keep rolling until you match{original_point}')
    
   # while True:
        #dice_1, dice_2 = roll_dice_return_results()
        #roll_result = dice_1 + dice_2
       # print(f'You rolled a {dice_1 + dice_2}')

       # if roll_result == 7:
        #  print(f"You LOSE by rolling a {roll_result}!!!!!")
         # break
        #if original_point == roll_result:
        #  print(f"You WIN by making the {original_point}!!!!! ")
        #break
        
            
            







    # If player rolls 2, 3 or 12 on first roll, player loses

       # Could do randint(2, 12) but using two dice allows for further expansion of craps

