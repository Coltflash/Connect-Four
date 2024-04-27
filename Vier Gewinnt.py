import os, time, random, time

os.system("cls")


board = [[],[],[],[],[],[]]

for hRow in board:
    for i in range(7):
        hRow.append("⚪")



def printBoard():
    print(f"+-----+-----+-----+-----+-----+-----+-----+")
    for lists in board:
        chipList = []
        for e in lists: chipList.append(e)
        print(f"| {chipList[0]}  | {chipList[1]}  | {chipList[2]}  | {chipList[3]}  | {chipList[4]}  | {chipList[5]}  | {chipList[6]}  |")
        print(f"+-----+-----+-----+-----+-----+-----+-----+")


def player_move():
    while True:
        player_move = input("Move (1-7): >>")
        if player_move.isdigit():
            player_move = int(player_move)-1
            if player_move >= 0 and player_move <7:

                os.system("cls")
                break
        else:
            print("Please enter a valid number.")
            time.sleep(1)
            
    return player_move 


def checkWin():
    
    reversedBoard = list(reversed(board))

    xCounter = 0
    oCounter = 0

    for index, hRows in enumerate(board): #checks horizontal rows
        xCounter = 0
        oCounter = 0   
        for element in hRows:
            if oCounter == 4 or xCounter == 4: return True

            if element == "🔴":
                xCounter +=1
                oCounter = 0
                
            elif element == "⚫":
                oCounter +=1
                xCounter = 0

            else:
                oCounter = 0
                xCounter = 0
            if oCounter == 4 or xCounter == 4: return True
        
    for y in range(7):    #checks vertical rows
        xCounter = 0
        oCounter = 0
        for i in range(6):
            if oCounter == 4 or xCounter == 4: return True
            if board[i][y] == "🔴":
                xCounter +=1
                oCounter = 0

            elif board[i][y] == "⚫":
                oCounter +=1
                xCounter = 0

            else:
                oCounter = 0
                xCounter = 0
            if oCounter == 4 or xCounter == 4: return True

    indexs = [5,0, 5,1, 5,2, 5,3, 4,0, 3,0]     #diagonal starting indexes

    for id in range(len(indexs)):        #checks diagonal rows
        oCounter = 0
        xCounter = 0
        for i in range(6):
            try:
                if oCounter == 4 or xCounter == 4: return True
                if indexs[id]-i >=0:
                    if board[indexs[id]-i][indexs[id+1]+i] == "🔴":
                        xCounter +=1
                        oCounter = 0
                    
                    elif board[indexs[id]-i][indexs[id+1]+i] == "⚫":
                        oCounter +=1
                        xCounter = 0
                    else:
                        oCounter = 0
                        xCounter = 0
                    if oCounter == 4 or xCounter == 4: return True
            except IndexError: pass

    indexs = [5,6, 5,5, 5,4, 5,3, 4,6, 4,6] #other diagonal starting indexes

    for id in range(len(indexs)):   #checks other diagonal rows
        oCounter = 0
        xCounter = 0        
        for i in range(6):
            try:
                if oCounter == 4 or xCounter == 4: return True
                if indexs[id]-i >=0:
                    if board[indexs[id]-i][indexs[id+1]-i] == "🔴":
                        xCounter +=1
                        oCounter = 0
                    
                    elif board[indexs[id]-i][indexs[id+1]-i] == "⚫":
                        oCounter +=1
                        xCounter = 0
                    else:
                        oCounter = 0
                        xCounter = 0
                if oCounter == 4 or xCounter == 4: return True
            except IndexError: pass   


    
def main(mode):
    if mode == 3:
        while True:
            tps = input("Turns per second: ")
            if tps.isdigit():
                tps = 1/float(tps)
                break
    os.system("cls")
    for i in range(len(board) * len(board[0])):
        
        if checkWin():
            printBoard()
            print(f"\nPlayer {player} wins!")
            break

        if i % 2 == 0:
            player = 1
            chip = "🔴"
        else:
            player = 2
            chip = "⚫"

        while True:
            printBoard()
            print(f"Player {player}")
            
            if mode == 1:
                index = player_move()

            elif mode == 2:
                if player == 1: index = player_move()
                if player == 2: 
                    time.sleep(0.4)
                    index = random.randint(0,6)

            elif mode == 3:
                time.sleep(tps)
                index = random.randint(0,6)  
                
            # else: 
            #     print("Error")
            #     time.sleep(2)
            os.system("cls")
            move_played = False

            for i, hRow in enumerate(reversed(board)):
                
                if hRow[index] == "⚪":
                    hRow[index] = chip
                    move_played = True
                    break

            if move_played == False:
                print("Row is full.")
                # time.sleep(1)
                os.system("cls")
                continue

            else: break

print("Welcome to Connect Four!")
print("\nChoose a Mode: (1: PvP; 2: PvE; 3: Auto)")
while True:
    
    mode = input(">>")
    if mode.isdigit():
        mode = int(mode)
        if mode >0 and mode <4: break
    
        

main(mode)



