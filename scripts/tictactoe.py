class TTT_Board:

    def __init__(self):
        self.board = [['_','_','_'],
                ['_','_','_'],
                ['_','_','_']]
        self.curr_player = 0
            
    def disp_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def determine_win(self):
        if self.board[0][0] != '_':
            if self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]:
                print("Player ",self.curr_player, " Wins!")
                return False
            if self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][1]:
                print("Player ",self.curr_player, " Wins!")
                return False
            
        if self.board[2][2] != '_':
            if self.board[2][2] == self.board[2][1] and self.board[2][2] == self.board[2][0]:
                print("Player ",self.curr_player, " Wins!")
                return False
            if self.board[2][2] == self.board[1][2] and self.board[2][2] == self.board[0][2]:
                print("Player ",self.curr_player, " Wins!")
                return False
        
        if self.board[1][1] != '_':
            if self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2]:
                print("Player ",self.curr_player, " Wins!")
                return False
            if self.board[1][1] == self.board[2][0] and self.board[1][1] == self.board[0][2]:
                print("Player ",self.curr_player, " Wins!")
                return False
        return True


    def place_tile(self,x,y):
        if self.board[y][x] == '_':
            if self.curr_player == 0:
                self.board[y][x] = 'X'
                self.disp_board()
                print("----------")
                self.determine_win()
                self.curr_player = 1
                return True
            else:
                self.board[y][x] = 'O'
                self.disp_board()
                print("----------")
                self.determine_win()
                self.curr_player = 0
                return True
        else:
            print("Place a piece on an empty tile!")
            return False      