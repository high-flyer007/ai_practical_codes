
# Water Jug Problem using DFS

# Jug capacities
JUG_A = 4
JUG_B = 3

# Required quantity
TARGET = 2


def get_next_states(state):

    x, y = state

    next_states = []

    # 1. Fill Jug A
    next_states.append(((JUG_A, y), "Fill Jug A"))

    # 2. Fill Jug B
    next_states.append(((x, JUG_B), "Fill Jug B"))

    # 3. Empty Jug A
    next_states.append(((0, y), "Empty Jug A"))

    # 4. Empty Jug B
    next_states.append(((x, 0), "Empty Jug B"))

    # 5. Pour Jug A into Jug B
    pour = min(x, JUG_B - y)
    next_states.append(((x - pour, y + pour),
                        "Pour A into B"))

    # 6. Pour Jug B into Jug A
    pour = min(y, JUG_A - x)
    next_states.append(((x + pour, y - pour),
                        "Pour B into A"))

    return next_states


# DFS Algorithm
def dfs(state, visited, path):

    # Check goal condition
    if state[0] == TARGET or state[1] == TARGET:
        return True

    # Mark current state visited
    visited.add(state)

    # Explore next states
    for next_state, action in get_next_states(state):

        if next_state not in visited:

            path.append((next_state, action))

            # Recursive DFS call
            if dfs(next_state, visited, path):
                return True

            # Backtracking
            path.pop()

    return False


# Main Program
if __name__ == "__main__":

    initial_state = (0, 0)

    visited = set()

    path = []

    print("WATER JUG PROBLEM")
    print("Jug A Capacity:", JUG_A)
    print("Jug B Capacity:", JUG_B)
    print("Target Quantity:", TARGET)

    if dfs(initial_state, visited, path):

        print("\nSOLUTION FOUND!")

        print("Initial State:", initial_state)

        for i, (state, action) in enumerate(path, 1):

            print("Step", i, ":", action)
            print("State:", state)

        print("\nGoal Reached!")

    else:

        print("No solution found.")
