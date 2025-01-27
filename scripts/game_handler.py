import tictactoe

board = tictactoe.TTT_Board()

board.disp_board()
while (board.determine_win()):
    print("Player ", board.curr_player, " is up")
    coor = input()
    x = int(coor[0])
    y = int(coor[2])
    board.place_tile(x,y)