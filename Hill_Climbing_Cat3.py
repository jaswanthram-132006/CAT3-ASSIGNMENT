import random

N = 8

def random_board():
    return [random.randint(0, N - 1) for _ in range(N)]

def count_conflicts(board):
    conflicts = 0
    for col1 in range(N):
        for col2 in range(col1 + 1, N):
            row1, row2 = board[col1], board[col2]
            if row1 == row2 or abs(row1 - row2) == abs(col1 - col2):
                conflicts += 1
    return conflicts

def get_best_neighbor(board):
    best_boards = []
    best_cost = count_conflicts(board)

    for col in range(N):
        original_row = board[col]
        for row in range(N):
            if row == original_row:
                continue
            new_board = board.copy()
            new_board[col] = row
            cost = count_conflicts(new_board)

            if cost < best_cost:
                best_cost = cost
                best_boards = [new_board]
            elif cost == best_cost:
                best_boards.append(new_board)

    if not best_boards:
        return board, best_cost
    return random.choice(best_boards), best_cost

def hill_climbing():
    current = random_board()
    current_cost = count_conflicts(current)

    while True:
        neighbor, neighbor_cost = get_best_neighbor(current)
        if neighbor_cost >= current_cost:
            return current, current_cost
        current, current_cost = neighbor, neighbor_cost

def solve_with_restarts(max_restarts=1000):
    for attempt in range(1, max_restarts + 1):
        board, cost = hill_climbing()
        if cost == 0:
            return board, attempt
    return None, max_restarts

def print_board(board):
    for row in range(N):
        line = ""
        for col in range(N):
            line += " Q " if board[col] == row else " . "
        print(line)

if __name__ == "__main__":
    solution, attempts = solve_with_restarts()
    if solution:
        print(f"Solved in {attempts} attempt(s).")
        print(solution)
        print_board(solution)
    else:
        print("No solution found within the restart limit.")
