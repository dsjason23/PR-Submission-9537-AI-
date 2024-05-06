import random

def conflicts(board, row, col):
   
    count = 0
    for i in range(len(board)):
        if i != row:
            if board[i] == col or abs(i - row) == abs(board[i] - col):
                count += 1
    return count

def evaluate(board):
    
    total_conflicts = 0
    for row in range(len(board)):
        total_conflicts += conflicts(board, row, board[row])
    return total_conflicts

def random_board(size):
    
    return [random.randint(0, size-1) for _ in range(size)]

def local_search(size, max_iter=1000):
   
    board = random_board(size)
    for _ in range(max_iter):
        current_conflicts = evaluate(board)
        if current_conflicts == 0:
            return board  
        row = random.randint(0, size-1)
        col = board[row]
        current_conflicts -= conflicts(board, row, col)
        min_conflicts = float('inf')
        best_move = col
        for new_col in range(size):
            if new_col != col:
                new_conflicts = conflicts(board, row, new_col)
                if new_conflicts < min_conflicts:
                    min_conflicts = new_conflicts
                    best_move = new_col
        if min_conflicts < current_conflicts:
            board[row] = best_move
    return None  # No solution found within max_iter


size = 8  
solution = local_search(size)
if solution:
    print("Solution found:")
    for row in solution:
        print(" . " * row + " Q " + " . " * (size - row - 1))
else:
    print("No solution found within maximum iterations.")