
from queue import PriorityQueue

# Initial and Goal States
INITIAL = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = GOAL.index(tile)

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Check whether the puzzle is solvable
def is_solvable(state):
    goal_order = {
        tile: i for i, tile in enumerate(GOAL) if tile != 0
    }

    tiles = [goal_order[tile] for tile in state if tile != 0]

    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


# Display the puzzle board
def display(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


# Generate all possible next states
def get_neighbors(state):
    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Possible movements of blank space
    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with adjacent tile
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank]
            )

            neighbors.append((tuple(new_state), move))

    return neighbors


# A* Search Algorithm
def a_star(initial, goal):

    # Priority Queue: (f, g, state)
    open_list = PriorityQueue()

    # Initial state
    open_list.put((heuristic(initial), 0, initial))

    # Store the best cost to reach each state
    g_cost = {initial: 0}

    # Store parent and movement information
    parent = {}

    while not open_list.empty():

        f, g, current = open_list.get()

        # Ignore outdated queue entries
        if g != g_cost.get(current):
            continue

        # Check goal state
        if current == goal:

            path = []
            moves = []

            temp = current

            while temp != initial:
                previous, move = parent[temp]

                path.append(temp)
                moves.append(move)

                temp = previous

            path.append(initial)

            path.reverse()
            moves.reverse()

            return path, moves

        # Generate successor states
        for neighbor, move in get_neighbors(current):

            new_g = g + 1

            # Check whether this is a better path
            if new_g < g_cost.get(neighbor, float("inf")):

                g_cost[neighbor] = new_g

                h = heuristic(neighbor)

                new_f = new_g + h

                parent[neighbor] = (current, move)

                open_list.put((new_f, new_g, neighbor))

    return None, None


# Main Program
if __name__ == "__main__":

    print("INITIAL STATE:")
    display(INITIAL)

    print("GOAL STATE:")
    display(GOAL)

    if not is_solvable(INITIAL):
        print("The puzzle is not solvable.")
    else:

        print("Starting A* Search...\n")

        path, moves = a_star(INITIAL, GOAL)

        if path:

            print("SOLUTION FOUND!")
            print("Total Moves:", len(moves))
            print("Total States:", len(path))

            for i, state in enumerate(path):

                if i == 0:
                    print("\nInitial State:")
                else:
                    print("Move", i, ":", moves[i - 1])

                display(state)

            print("Goal State Reached Successfully!")

        else:
            print("No solution found.")
