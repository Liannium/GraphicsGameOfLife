from board import Board

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
board = Board(rows, columns)
board.generate_random()
user_input = ''
while user_input != 'q':
    print(board)
    board.update()
    user_input = str(input("Press enter to continue or q to quit"))
