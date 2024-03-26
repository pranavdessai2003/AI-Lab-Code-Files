def is_valid(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right, _ = state
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    if missionaries_left < 0 or cannibals_left < 0 or missionaries_right < 0 or cannibals_right < 0:
        return False
    if missionaries_left > 3 or cannibals_left > 3 or missionaries_right > 3 or cannibals_right > 3:
        return False
    return True

def successors(state):
    successors = []
    missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat = state
    if boat == 'left':
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries_left - m, cannibals_left - c, missionaries_right + m, cannibals_right + c, 'right')
                    if is_valid(new_state):
                        successors.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries_left + m, cannibals_left + c, missionaries_right - m, cannibals_right - c, 'left')
                    if is_valid(new_state):
                        successors.append(new_state)
    return successors

def dfs(node, goal, visited):
    if node == goal:
        return [node]
    visited.add(node)
    for child in successors(node):
        if child not in visited:
            path = dfs(child, goal, visited)
            if path:
                return [node] + path
    return None

def main():
    initial_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')
    visited = set()
    solution = dfs(initial_state, goal_state, visited)
    if solution:
        print("Solution path:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
