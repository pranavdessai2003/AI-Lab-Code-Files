import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # cost from start node to current node
        self.h = h  # heuristic estimate of the cost from current node to goal node
        self.f = self.g + self.h  # total estimated cost

    def __lt__(self, other):
        return self.f < other.f

def astar_search(start_state, goal_state, heuristic_func, successors_func):
    start_node = Node(start_state)
    goal_node = Node(goal_state)

    open_list = [start_node]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_node.state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.state)

        for successor_state, cost in successors_func(current_node.state):
            if successor_state in closed_list:
                continue

            g = current_node.g + cost
            h = heuristic_func(successor_state, goal_node.state)
            f = g + h

            successor_node = Node(successor_state, current_node, g, h)

            if successor_node not in open_list:
                heapq.heappush(open_list, successor_node)

    return None

# Example usage:
def heuristic(state, goal_state):
    return abs(state - goal_state)

def successors(state):
    return [(state+1, 1), (state-1, 1)]

start_state = 5
goal_state = 20
path = astar_search(start_state, goal_state, heuristic, successors)
print("A* path:", path)
