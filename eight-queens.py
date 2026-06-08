import random

def generate_random_board():
    return [random.randint(0, 7) for i in range(8)]

def calculate_heuristic(board):
    attacks = 0

    for i in range(8):
        for j in range(i+1, 8):
            #checks if both queens are on the same line
            if board[i] == board[j]:
                attacks += 1
            
            #checks if both queens are on the same diagonal
            elif abs(board[i]-board[j]) == abs(i-j):
                attacks += 1

    return attacks

def climb(board):
    best_board = list(board)
    best_heuristic = calculate_heuristic(best_board)

    new_board = list(board)

    for j in range(8):
        original_row = board[j]
        for i in range(8):
            if i == original_row:
                continue

            new_board[j] = i
            new_heuristic = calculate_heuristic(new_board)

            if new_heuristic < best_heuristic:
                best_board = list(new_board)
                best_heuristic = new_heuristic

        new_board[j] = original_row

    return best_board

def hill_climbing(board):
    #to do
    return 

def solve():
    #to do
    return


