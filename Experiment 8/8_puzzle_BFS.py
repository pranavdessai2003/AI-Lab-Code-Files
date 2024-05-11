from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_next_states(state):
    states = []
    blank_i, blank_j = get_blank_position(state)

    # Move blank tile left
    if blank_j > 0:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]
        states.append(new_state)

    # Move blank tile right
    if blank_j < 2:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]
        states.append(new_state)

    # Move blank tile up
    if blank_i > 0:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
        states.append(new_state)

    # Move blank tile down
    if blank_i < 2:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
        states.append(new_state)

    return states

def calculate_heuristic(state, goal_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

def best_first_search(initial_state, goal_state):
    open_list = PriorityQueue()
    closed_set = set()
    initial_node = Node(initial_state)
    initial_node.cost = calculate_heuristic(initial_state, goal_state)
    open_list.put(initial_node)

    while not open_list.empty():
        current_node = open_list.get()
        closed_set.add(current_node)

        if current_node.state == goal_state:
            return current_node

        next_states = get_next_states(current_node.state)

        for next_state in next_states:
            child_node = Node(next_state, parent=current_node, move=None)
            child_node.cost = calculate_heuristic(next_state, goal_state)
            child_node.depth = current_node.depth + 1

            if child_node not in closed_set:
                open_list.put(child_node)

    return None

def get_solution_path(node):
    path = []
    current_node = node
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    return path[::-1]

def display_steps(path):
    print("Steps to reach the goal:")
    for i, state in enumerate(path):
        print(f"Step {i + 1}:")
        for row in state:
            print(row)
        print()

# Define the initial and goal states
initial_state = [
    [2, 5, 3],
    [1, 0, 6],
    [4, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution_node = best_first_search(initial_state, goal_state)

if solution_node:
    print("Goal state reached!")
    solution_path = get_solution_path(solution_node)
    display_steps(solution_path)
else:
    print("No solution found.")
