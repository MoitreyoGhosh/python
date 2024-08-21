def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    board = ['X' if xState[i] else ('O' if zState[i] else str(i)) for i in range(9)]
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X has won the match!")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O has won the match!")
            return 0
    return -1

def isDraw(xState, zState):
    return all(xState[i] or zState[i] for i in range(9))

def resetBoard():
    return [0] * 9, [0] * 9

if __name__ == "__main__":
    print("Welcome to TicTacToe Game")
    
    while True:
        xState, zState = resetBoard()
        turn = 1  # 1 for X and 0 for O
        
        while True:
            printBoard(xState, zState)
            if turn == 1:
                print("X's turn")
            else:
                print("O's turn")
            
            value = int(input("Please enter a value (or -1 to quit): "))
            
            if value == -1:
                print("Thanks for playing!")
                exit()
            
            if xState[value] or zState[value]:
                print("Invalid move! The cell is already taken. Try again.")
                continue
            
            if turn == 1:
                xState[value] = 1
            else:
                zState[value] = 1
            
            result = checkWin(xState, zState)
            if result != -1:
                printBoard(xState, zState)
                print("Match Over")
                break
            
            if isDraw(xState, zState):
                printBoard(xState, zState)
                print("It's a draw!")
                break
            
            turn = 1 - turn
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
