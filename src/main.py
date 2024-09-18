
class Main:
    def __init__(self):
        from board import Board
        self.board = Board(9, 9, 10)

    def run(self):
        while not self.board.is_game_over():
            print(self.board.display_board())
            command = input("Enter command (reveal or flag) and coordinates (x, y): ").split()
            action, x, y = command[0], int(command[1]), int(command[2])

            if action == 'reveal':
                self.board.reveal_tile(x, y)
            elif action == 'flag':
                self.board.flag_tile(x, y)

        if self.board.is_game_won():
            print("Congratulations, you have won!")
        else:
            print("Game over. Better luck next time.")
