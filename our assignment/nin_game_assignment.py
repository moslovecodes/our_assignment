
player=1



state=21 
print("The number of object is now ",state)

while True:


    print("player ",player)
    move= int(input("What is your move? "))
    if move <= 3 and move < state :
        state = state - move
        print(state)
        if player == 1 :
            player = 2
        else:
            player = 1
            

    elif state==1:
        print("Player ", player,"wins!")
        break
    else:
      print('kosise')