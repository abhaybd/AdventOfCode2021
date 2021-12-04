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

def get_board_nums(board):
    nums = set()
    for row in board:
        for x in row:
            nums.add(x)
    return nums

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
    board_nums = list(map(get_board_nums, boards))
    last_board_score = None
    already_won = set()
    for num in nums:
        for i, board in enumerate(boards):
            if i not in already_won and num in board_nums[i]:
                mark_board(board, num)
                if has_board_won(board):
                    already_won.add(i)
                    last_board_score = num * score_board(board)
    print(last_board_score)

main()
