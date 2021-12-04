import re

def read_data():
    with open("input.txt") as f:
        nums = list(map(int, f.readline().split(",")))
        lines = f.read().split("\n")
        i = 0
        boards = []
        while i < len(lines):
            board = []
            for j in range(5):
                board.append(list(map(int, re.split(r"\s+", lines[i+j+1].strip()))))
            boards.append(board)
            i += 6
    return nums, boards

def complete_row(board, row):
    return all(x is None for x in board[row])

def complete_col(board, col):
    return all(board[r][col] is None for r in range(len(board)))

def mark_board(board, num):
    for row in board:
        for i in range(len(row)):
            if row[i] == num:
                row[i] = None

def has_board_won(board):
    return any(complete_row(board,row) for row in range(5)) or any(complete_col(board, col) for col in range(5))

def score_board(board):
    score = 0
    for row in board:
        score += sum(x for x in row if x)
    return score

def main():
    nums, boards = read_data()
    for num in nums:
        for i, board in enumerate(boards):
            mark_board(board, num)
            if has_board_won(board):
                print(num * score_board(board))
                return

main()
