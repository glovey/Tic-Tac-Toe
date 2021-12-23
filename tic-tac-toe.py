
positions = [1,2,3,4,5,6,7,8,9]
game_on = False
player_1 ="t"
player_2 = "t"
win = False


def choose_piece(player_1):  
  while player_1 not in ["X","O"]:
    player_1 = (input("player 1, do you want to be X or O?")).upper()
    
    if player_1  not in ["X","O"]:
      print ("Sorry I don't understand, please enter X or O")
  return player_1  

def p2_symbol(player_1,player_2):  
  if player_1 == "X":
    player_2 = "O"  
  else:
    player_2 ="X" 
  return player_2  
      
  
def display_board(positions):
  print ("{} | {} | {}".format(positions[0],positions[1], positions[2]))
  print ("------------")
  print ("{} | {} | {}".format(positions[3],positions[4], positions[5]))
  print ("------------")
  print ("{} | {} | {}".format(positions[6],positions[7], positions[8]))
  print ("\n")


def p1_input(positions):
  place1 = ""
  while place1 not in range(1,10):    
    place1 = input(f"Player 1, choose a position to place an {player_1} (choose 1-9)")
    if not place1.isdigit():      
      print ("sorry that is not valid")
    elif int(place1) not in range(1,10):
      print ("sorry that is not valid")
    elif positions[int(place1)-1] in ["X","O"]:
      print ("Oi, that spots taken")     
    else:
      place1 = int(place1)  
  positions[place1-1] = player_1
  return positions


def p2_input(positions):
  place2 = ""
  while place2 not in range(1,10):    
    place2 = input(f"Player 2, choose a position to place an {player_2} (choose 1-9)")
    if not place2.isdigit():      
      print ("sorry that is not valid")
    elif int(place2) not in range(1,10):
      print ("sorry that is not valid")
    elif positions[int(place2)-1] in ["X","O"]:
      print ("Oi, that spots taken")
    else:
      place2 = int(place2) 
  positions[place2-1] = player_2
  return positions


#def tie_game(positions, tie):
  #for x in positions:
   # if x in range(1-9):
   #   tie = False
  #    break
 #   else:
#      tie = True

def winner(positions, win):
  # check for win
  if positions[0] == positions[1] and positions[0] == positions[2]:
    win = True
    print ("well done, you win!")
  elif positions[3] == positions[4] and positions[3] == positions[5]:
    win = True 
    print ("well done, you win!") 
  elif positions[6] == positions[7] and positions[6] == positions[8]:
    win = True 
    print ("well done, you win!") 
  elif positions[0] == positions[3] and positions[0] == positions[6]:
    win = True 
    print ("well done, you win!") 
  elif positions[1] == positions[4] and positions[1] == positions[7]:
    win = True 
    print ("well done, you win!")
  elif positions[2] == positions[5] and positions[2] == positions[8]:
    win = True 
    print ("well done, you win!")  
  elif positions[0] == positions[4] and positions[0] == positions[8]:
    win = True 
    print ("well done, you win!")
  elif positions[2] == positions[4] and positions[2] == positions[6]:
    win = True 
    print ("well done, you win!")
  elif positions[0] == positions[4] and positions[0] == positions[8]:
    win = True 
    print ("well done, you win!")
  else:
    win = False   
  
#check for tie:
  nums = []
  if win == False:
    for x in positions:
      if type(x) == int:
        nums.append(x)
        print (len(nums))
    if len(nums) == 0:
      print (len(nums))
      print ("It's a draw, game over!")
      win = True
      
    else:
      win = False 
      print("tie false") 
    
  return win


def clear_output():
  print ("\n"*200)

def play_game(game_on):
  choice = ""
  while choice not in ["Y","N"]:
    choice = (input("do you want to play tic-tac-toe? Enter Y or N")).upper()
    if choice not in ["Y","N"]:
      print ("sorry that's not valid")
  if choice == "Y":
    game_on = True
    return game_on
  else:
    print ("ok, no worries, bye!") 
    

def play_again(game_on):
  choice = ""
  while choice not in ["Y","N"]:
    choice = (input("do you want to play again? Enter Y or N")).upper()
    if choice not in ["Y","N"]:
      print ("sorry that's not valid")
  if choice == "Y":
    game_on = True
    return game_on
  else:
    game_on = False
    print ("ok, no worries, bye!")  
    return game_on


game_on = play_game(game_on)
while game_on == True:

  player_1 = choose_piece(player_1)
  player_2 = p2_symbol(player_1,player_2)
  clear_output()
  print (f"OK, lets go, player 1 is {player_1}, player 2 is {player_2}"+"\n")
  while win == False:
    display_board(positions)
    positions = p1_input(positions)
    win = winner(positions,win) 
    if win == True:
      break
       
    clear_output()
    
    display_board(positions)
    positions = p2_input(positions)
    win = winner(positions,win)
    if win == True:
      break 
    clear_output()
  
  positions = [1,2,3,4,5,6,7,8,9]
  game_on = False
  player_1 ="t"
  player_2 = "t"
  win = False

  game_on= play_again(game_on)
