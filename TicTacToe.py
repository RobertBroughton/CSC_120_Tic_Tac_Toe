board = [["-","-","-"],["-","-","-"],["-","-","-"]]
player_id = 0
def printBoard():
    for x in board:
        print(x)

def getRow():
    return int(input("Enter Row (0-2)"))

def getCol():
    return int(input("Enter Column (0-2)"))

def checkMark(row,col):
    if board[row][col] == "-":
        return True
    else:
        return False;

def addMark(plrid):
    player = ""
    if plrid == 0:
        player = "O"
    else:
        player = "X"
    row = getRow()
    col = getCol()
    if checkMark(row,col) == True:
        board[row][col] = player
        return True
    else:
        return False

def checkWinHorizontal(plrid):
    player = ""
    if plrid == 0:
        player = "O";
    else:
        player = "X";
    for i in range(0,3):
            win = True
            for j in range(0,3):
                if board[i][j] != player:
                    win = False
            if win:
                return True
    return False

def checkWinVertical(plrid):
    player = ""
    if plrid == 0:
        player = "O";
    else:
        player = "X";
    for i in range(0,3):
            win = True
            for j in range(0,3):
                if board[j][i] != player:
                    win = False
            if win:
                return True
    return False
def checkWinDiagnalOne(plrid):
    player = ""
    if plrid == 0:
        player = "O";
    else:
        player = "X";
    for i in range(0,3):
        if board[i][i] != player:
            return False
    return True
def checkWinDiagnalTwo(plrid):
    player = ""
    if plrid == 0:
        player = "O";
    else:
        player = "X";
    for i in range(2,-1,-1):
        if board[i][i] != player:
            return False
    return True

def checkWin(plrid):
    if checkWinHorizontal(plrid):
        return True
    elif checkWinVertical(plrid):
        return True
    elif checkWinDiagnalOne(plrid):
        return True
    elif checkWinDiagnalTwo(plrid):
        return True
    else:
        return False

def switchPlayer(plrid):
    if plrid == 0:
        return 1
    else:
        return 0

def main():
    player_id = 0;
    printBoard()
    NoWinYet = True
    while NoWinYet:
        invalid = True
        while (invalid):
            if addMark(player_id) == False:
                print("Error Invalid Spot")
                valid = False
            else:
                printBoard()
            if checkWin(player_id):
                print("Player ", player_id+1, " Has Won")
                NoWinYet = False
            player_id = switchPlayer(player_id)
        

main()
