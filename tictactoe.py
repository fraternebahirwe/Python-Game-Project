class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                self.print_board()
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return False
        else:
            print("This move is not allowed. Try again.")
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)


# Example usage
if __name__ == "__main__":
    game = TicTacToe()
    game_over = False
    
    while not game_over:
        game.print_board()
        row = int(input(f"Player {game.current_player}, enter your move row (0-2): "))
        col = int(input(f"Player {game.current_player}, enter your move column (0-2): "))
        if game.make_move(row, col):
            game_over = True
        if game.is_draw():
            print("It's a draw!")
            game.print_board()
            break
