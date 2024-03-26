def is_valid_state(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat_position = state
    if missionaries_left < 0 or cannibals_left < 0 or missionaries_right < 0 or cannibals_right < 0:
        return False
    if missionaries_left > 3 or cannibals_left > 3 or missionaries_right > 3 or cannibals_right > 3:
        return False
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

def generate_successors(state):
    successors = []
    missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat_position = state
    if boat_position == 'left':
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries_left - m, cannibals_left - c, missionaries_right + m, cannibals_right + c, 'right')
                    if is_valid_state(new_state):
                        successors.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries_left + m, cannibals_left + c, missionaries_right - m, cannibals_right - c, 'left')
                    if is_valid_state(new_state):
                        successors.append(new_state)
    return successors

def bfs_search(initial_state, goal_state):
    visited_states = set()
    queue = [(initial_state, [])]
    front = 0

    while front < len(queue):
        current_state, path = queue[front]
        front += 1
        
        if current_state == goal_state:
            return path + [current_state]
        
        visited_states.add(current_state)
        
        for successor in generate_successors(current_state):
            if successor not in visited_states:
                queue.append((successor, path + [current_state]))
                visited_states.add(successor)
    
    return None

def main():
    initial_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')
    
    solution_path = bfs_search(initial_state, goal_state)
    if solution_path:
        print("Solution path:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
