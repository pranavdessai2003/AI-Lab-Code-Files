from collections import deque

def water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited_states = set()
    initial_state = (0, 0, [])
    stack = deque([(0, 0, [])])
    
    while stack:
        current_state = stack.pop()
        jug1, jug2, steps = current_state
        
       
        if (jug1, jug2) == target:
            return steps  
        
        visited_states.add((jug1, jug2))
        
        next_state = (capacity_jug1, jug2, steps + [f'Fill jug1'])
        if next_state[:2] not in visited_states:
            stack.append(next_state)
        

        next_state = (jug1, capacity_jug2, steps + [f'Fill jug2'])
        if next_state[:2] not in visited_states:
            stack.append(next_state)
        
        
        next_state = (max(0, jug1 - (capacity_jug2 - jug2)),
                      min(capacity_jug2, jug1 + jug2),
                      steps + [f'Pour jug1 to jug2'])
        if next_state[:2] not in visited_states:
            stack.append(next_state)
        
       
        next_state = (min(capacity_jug1, jug1 + jug2),
                      max(0, jug2 - (capacity_jug1 - jug1)),
                      steps + [f'Pour jug2 to jug1'])
        if next_state[:2] not in visited_states:
            stack.append(next_state)
        
        
        next_state = (0, jug2, steps + [f'Empty jug1'])
        if next_state[:2] not in visited_states:
            stack.append(next_state)
        
       
        next_state = (jug1, 0, steps + [f'Empty jug2'])
        if next_state[:2] not in visited_states:
            stack.append(next_state)
    
    return None  


jug1_capacity = 4
jug2_capacity = 3
target_amount = (2,0)
steps = water_jug_problem(jug1_capacity,jug2_capacity,target_amount)

if steps:
    print(f"Steps to measure {target_amount} with the given jugs:")
    for step in steps:
        print(f" - {step}")
else:
    print(f"You cannot measure {target_amount} with the given jugs.")