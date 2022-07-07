print('''
    _m_   
  /\___\    
  |_|""|    Jalindre Bhavan
_/______\____________________________________________________________________
''')
print('''  
           ****Find the right way to Jalindre bhavan!!****
         ***You are currently in PVGCOET AKA Muktangan :)***

     ''')
print('''
         To walk straight press *S*
         To take a Right Turn press *R*
         To take a Left Turn press *L*
         
                  ''')
start = input("To start Press Y : ")
if start == 'Y':
    print("You have successfully started the game and you are currently standing at the Main Gate of PVGCOET!")
else:
    print("Byee") 

one = input("Enter your choice : ")
if one == 'S':
    print("It's a correct choice, you are heading towards Renuse Premacha Chaha!")
else:
    print("Game over, go back to college and attend lectures XD")

two = input("Enter your choice : ")
if two == 'L':
    print("It's a correct choice")
else:
    print("Game over")

three = input("Enter your choice : ")
if three == 'L':
    print("It's a correct choice")
else:
    print("Game over")

four = input("Enter your choice : ")
if four == 'R':
    print("It's a correct choice")
    print("You have successfully completed the game and reached jalindre bhavan!!")
else:
    print("Game over")


