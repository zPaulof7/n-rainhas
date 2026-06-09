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
    board_heuristic = calculate_heuristic(board)
    if board_heuristic == 0:
        return board
    
    new_board = climb(board)
    new_board_heuristic = calculate_heuristic(new_board)

    if new_board_heuristic >= board_heuristic:
        new_board = generate_random_board()
    
    return hill_climbing(new_board)

def solve():
    board = generate_random_board()
    solution = hill_climbing(board)
    return solution

def draw_board(board):
    n = len(board)
    print("   " + "   ".join([str(i) for i in range(n)]))
    print("  " + "-" * (n * 4 + 1))
    
    for row in range(n):
        line = f"{row} |"
        
        for col in range(n):
            if board[col] == row:
                line += " ♛ |"
            else:
                line += "   |"
                    
        print(line)
        print("  " + "-" * (n * 4 + 1))
    print("\n")

if __name__ == "__main__":
    solution = solve()
    draw_board(solution)