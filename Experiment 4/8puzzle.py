
initial_state = (1, 2, 3, 4, 6, 5, 0, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

moves = {
    "UP": -3,
    "DOWN": 3,
    "LEFT": -1,
    "RIGHT": 1,
}

movement_constraints = {
    0: ["DOWN", "RIGHT"],
    1: ["DOWN", "RIGHT", "LEFT"],
    2: ["DOWN", "LEFT"],
    3: ["UP", "DOWN", "RIGHT"],
    4: ["UP", "DOWN", "RIGHT", "LEFT"],
    5: ["UP", "DOWN", "LEFT"],
    6: ["UP", "RIGHT"],
    7: ["UP", "RIGHT", "LEFT"],
    8: ["UP", "LEFT"],
}

def apply_move(state, move):
    empty_index = state.index(0)
    new_index = empty_index + moves[move]

    if move not in movement_constraints[empty_index]:
        return None
    
    state = list(state)
    state[empty_index], state[new_index] = state[new_index], state[empty_index]
    return tuple(state)

def heuristic(state):
    return sum(1 for i in range(9) if state[i] != goal_state[i] and state[i] != 0)

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()

def hill_climbing(initial_state):
    current_state = initial_state
    path = []
    
    while True:
        print("Current state:")
        print_puzzle(current_state)
        print("heuristic Value: ")
        print(heuristic(current_state))

        if current_state == goal_state:
            print("Reached the goal state.")
            return path
        
        neighbors = []
        for move in movement_constraints[current_state.index(0)]:
            new_state = apply_move(current_state, move)
            if new_state:
                neighbors.append((new_state, move))
        
        if not neighbors:
            return None
        
        neighbors.sort(key=lambda x: heuristic(x[0]))
        
        next_state, move = neighbors[0]
        
        if heuristic(next_state) >= heuristic(current_state):
            print("Next state:")
            print_puzzle(next_state)
            print("heuristic Value: ")
            print(heuristic(next_state))
            return None
        
        
        current_state = next_state
        path.append(move)

def main():
    solution_path = hill_climbing(initial_state)
    if solution_path:
        print("Solution found! Moves:", solution_path)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

