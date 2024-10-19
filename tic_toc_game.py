board=["_","_","_"
       "_","_","_"
       "_","_","_"]

CurrentPlayer="X"
Winner=None
GameRunning=True

def  checkWinner(board):
    print(board[0] + "|" +  board[1] + "|" +  board[2])
    print(board[3] + "|" +  board[4] + "|" +  board[5])
    print(board[6] + "|" +  board[7] + "|" + board[8])
checkWinner(board)
    
