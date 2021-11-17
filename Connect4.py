"""
Add a description of the module.
Also mention your name and student id.
"""
from copy import deepcopy # you may use this for copying a board

def NewGame(player1, player2):
    game = {
             'player1' : player1,
             'player2' : player2,
             'who' : 1,
             'board' : [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
    }
     
    return game

def MakeMove(board,move, who):
    
    for row in range(5, -1, -1):
        if board[row][move] == 0 and who == 1:
            board[row][move] = 1
            return board
        if board[row][move] == 0 and who == 2:
            board[row][move] = 2

            return board
def PrintBoard(board):
    s = '|1|2|3|4|5|6|7|' + '\n' + '+-+-+-+-+-+-+-+'
    print(s)
    s = ''
    for row in board:
        s += '|'
        for i in row:
            if i == 0:
                s += ' ' +'|'
            if i == 1:
                s += 'X' +'|'
            if i == 2:
                s += 'O' +'|'
        s += '\n'
    print(s)
def GetValidMoves(board):
    validmoves = []
    for row in board:
        for i in range(len(row)):
            if row[i] == 0:
                validmoves.append(i)
        break
                
    return validmoves

def HasWon(board,who):
    vertical = 0
    horizontal = 0

    for row in board:
        for i in range(len(row)):
            if row[i] == who:
                horizontal += 1
            if row[i] != who:
                horizontal = 0
            if horizontal >= 4:
    
                return True
    for i in range(6):
        for column in board:
            if column[i] == who:
                vertical += 1
            if column[i] != who:
                vertical = 0
            if vertical >= 4:
    
                return True
    
    for row in range(len(board)):
        
        for counter in range(len(board[row])):
            win = 0
            if board[row][counter] == who:
                win += 1
               
                row_test = row +1
                column_test = counter +1
                column_2tst = counter - 1
                if counter <= 3 and row <= 2:
                    if board[row_test][column_test] == who:
                        row_test += 1
                        column_test += 1
                        win += 1
                        print(win)
                        if board[row_test][column_test] == who:
                            row_test += 1
                            column_test += 1 
                            win += 1
                            if board[row_test][column_test] == who:
                                win += 1
                                
                    if win >= 4:
                   
                       return True 
                win = 1
                row_test = row +1
                if counter >= 3 and row <= 2:
                    if board[row_test][column_2tst] == who:
                        row_test += 1
                        column_2tst -= 1
                        win += 1
                        if board[row_test][column_2tst] == who:
                            row_test += 1
                            column_2tst -= 1 
                            win += 1
                            if board[row_test][column_2tst] == who:
                                win += 1
                                print(row_test)
                                print(column_2tst)
                    if win >= 4:
                       
                           return True 
            
                    
    return False
def SuggestMove1(board,who):
    if who == 1:
        other = 2
    if who == 2:
        other = 1

    for j in range(7):
    
        testboard = deepcopy(board)
        testedboard = MakeMove(testboard, j, who)
        if HasWon(testedboard,who):
            
            return j

    for y in range(7):

        testboard = deepcopy(board)
        testedboard = MakeMove(testboard, y, other)
        if HasWon(testedboard, other):

            return y
    movelist = GetValidMoves(board)

    return movelist[0]
def SaveGame(game, filename = 'game'):
    player1 = str(game['player1'])
    player2 = str(game['player2'])
    who = int(game['who'])
    board = game['board']
    try:
        
        with open("{}.txt".format(filename), mode = 'wt' , encoding = 'utf8') as f:
            f.write(player1)
            f.write('\n')
            f.write(player2)
            f.write('\n')
            f.write(str(who))
            f.write('\n')
            for row in board:
                for element in range(len(row)):
                    f.write(str(row[element]))
                    if element != 6:
                        f.write(',')
                f.write('\n')
    except:
        
        print('there was an issue saving')
    return
def LoadGame(filename = 'game'):
    try:
        with open(filename, mode = 'rt', encoding = 'utf8') as connect:
            game = {}
            lst = []
            key = ['player1','player2','who','board']
            for k in range(3):
                line = connect.readline()
                line = line.replace('\n','')
                lst.append(line)
            lst[2] = int(lst[2])
            board = []
            for k in range(6):
                line = connect.readline()
                line = line.replace('\n','')
                line = line.split(',') 
                line = [int(i) for i in line]
                board.append(line)
            if len(board) != 6:
                raise ValueError('save file in incorrect format')
            else:
                lst.append(board)
                for i in range(4): 
                    game[key[i]] = lst[i]
    except FileNotFoundError:
        raise FileNotFoundError('No save file found')
    return game
def SuggestMove2(board,who):
    if who == 1:
        other = 2
    if who == 2:
        other = 1

    for j in range(7):
    
        testboard = deepcopy(board)
        testedboard = MakeMove(testboard, j, who)
        if HasWon(testedboard,who):
            
            return j

    for y in range(7):

        testboard = deepcopy(board)
        testedboard = MakeMove(testboard, y, other)
        if HasWon(testedboard, other):

            return y
    if board[5][3] == 0:
        return 3
    
    availablemoves = GetValidMoves(board)
    priority = []
    ndpriority = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == who:
                if board[i-1][j] == who:
                    ndpriority.append(j)
                if j-2 in availablemoves:
                    if board[i][j -1] == who and board[i][j-2] == 0:
                        priority.append(j-2)
                if j+2 in availablemoves:
                    if board[i][j+1] == who and board[i][j+2] == 0:
                        priority.append(j + 2)
                if j+1 in availablemoves:
                    ndpriority.append(j+1)
                if j-1 in availablemoves:
                    ndpriority.append(j-1)
    if priority == []:
        if ndpriority == []:
            lastresort = availablemoves[0]
            return lastresort
        else:
            return ndpriority[0]
    else:
        return priority[0]
# TODO: All the other functions of Tasks 2-11 go here.
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!
# ------------------- Main function --------------------
def play():
    """
    TODO in Task 7. Make sure to write meaningful docstrings!
    """
    print("*"*55)
    print("***"+" "*8+"WELCOME TO MyName'S CONNECT FOUR!"+" "*8+"***")
    print("*"*55,"\n")
    print("Enter the players' names, or type 'C' or 'L'.\n")
    while True:
        
            player1 = input('Who is player1?')
            
            if player1 == 'L':
                filename = input('what is the title of the game?')
                try:
                    game = LoadGame(filename)
                    board = game['board']
                    player1 = game['player1']
                    player2 = game['player2']
                    who = game['who']
                    PrintBoard(board)
                    break
                except:
                    print('Nofilefound')
                    continue
            
            else:
                player2 = input('Who is player2?')
                game = NewGame(player1,player2)
                board = game['board']
                player1 = game['player1']
                player2 = game['player2']
                who = game['who']
                PrintBoard(board)
                break
        
    while True:
        if who == 1:    
            if player1 == 'C':
                move = SuggestMove1(board,who)
                MakeMove(board,move,who)
                print('C will now move (X)')
                PrintBoard(board)

            else:
                availablemoves = GetValidMoves(board)
                move = input('where will you place {}?'.format(player1))
                if move == 'S':
                    filename = input('enter filename')
                    SaveGame(game, filename)
                    break
                
                    
                else:
                    try:
                        move = int(move)
                    except ValueError:
                        print('invalid move')
                while True:
                    if move in availablemoves:
                        board = MakeMove(board, move, who)
                        
                        PrintBoard(board)
                        break
                    else:
                        continue
            if HasWon(board,who):
                print('{}(X) has won the game'.format(player1))
                break
            else:
                who = 2
        if GetValidMoves(board) == []:
            print('The game is a draw')
            break
               
        else:
            if player2 == 'C':
                
                move = SuggestMove2(board,who)
                MakeMove(board,move,who)
                print('C will now move (O)')
                PrintBoard(board)

            else:
                availablemoves = GetValidMoves(board)
                move = input('where will you place {}(O)?'.format(player2))
                if move == 'S':
                    filename = input('enter a filename')
                    SaveGame(game, filename)
                    break
                
                else:
                    try:
                        move = int(move)
                    except ValueError:
                        print('invalid move')
                while True:
                    if move in availablemoves:
                        board = MakeMove(board, move, who)
                        
                        PrintBoard(board)
                        break
                    else:
                        continue
            if HasWon(board,who):
                print('{}(O) has won the game'.format(player2))
                break
            else:
                who = 1
        if GetValidMoves(board) == []:
            print('The game is a draw')
            break

# TODO: Game flow control starts here
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
 play()

def LoadGame():
    try:
        with open('game.txt', mode = 'rt', encoding = 'utf8') as connect:
            game = {}
            lst = []
            key = ['player1','player2','who','board']
            for k in range(3):
                line = connect.readline()
                line = line.replace('\n','')
                lst.append(line)
            lst[2] = int(lst[2])
            board = []
            for k in range(6):
                line = connect.readline()
                line = line.replace('\n','')
                line = line.split(',') 
                line = [int(i) for i in line]
                board.append(line)
            if len(board) != 6:
                raise ValueError('save file in incorrect format')
            else:
                lst.append(board)
                for i in range(4): 
                    game[key[i]] = lst[i]
    except FileNotFoundError:
        raise FileNotFoundError('No save file found')
    return game
