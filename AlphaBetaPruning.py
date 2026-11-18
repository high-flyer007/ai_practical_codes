
# Minimax Algorithm with Alpha-Beta Pruning

import math

# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Calculate maximum depth of game tree
depth = int(math.log2(len(values)))

# Count evaluated leaf nodes
nodes_evaluated = 0


# Minimax Algorithm
def minimax(depth, node_index, max_player):

    global nodes_evaluated

    # Terminal node condition
    if depth == 3:
        nodes_evaluated += 1
        return values[node_index]

    if max_player:

        left = minimax(depth + 1,
                       node_index * 2,
                       False)

        right = minimax(depth + 1,
                        node_index * 2 + 1,
                        False)

        return max(left, right)

    else:

        left = minimax(depth + 1,
                       node_index * 2,
                       True)

        right = minimax(depth + 1,
                        node_index * 2 + 1,
                        True)

        return min(left, right)


# Alpha-Beta Pruning Algorithm
def alphabeta(depth, node_index, max_player, alpha, beta):

    global nodes_evaluated

    # Terminal node condition
    if depth == 3:
        nodes_evaluated += 1
        return values[node_index]

    if max_player:

        best = -math.inf

        # Explore left child
        left = alphabeta(depth + 1,
                         node_index * 2,
                         False,
                         alpha,
                         beta)

        best = max(best, left)

        # Update Alpha
        alpha = max(alpha, best)

        # Explore right child only if pruning is not possible
        if beta > alpha:

            right = alphabeta(depth + 1,
                              node_index * 2 + 1,
                              False,
                              alpha,
                              beta)

            best = max(best, right)

        else:
            print("Pruned branch at MAX node:", node_index)

        return best

    else:

        best = math.inf

        # Explore left child
        left = alphabeta(depth + 1,
                         node_index * 2,
                         True,
                         alpha,
                         beta)

        best = min(best, left)

        # Update Beta
        beta = min(beta, best)

        # Explore right child only if pruning is not possible
        if beta > alpha:

            right = alphabeta(depth + 1,
                              node_index * 2 + 1,
                              True,
                              alpha,
                              beta)

            best = min(best, right)

        else:
            print("Pruned branch at MIN node:", node_index)

        return best


# Main Program
if __name__ == "__main__":

    print("MINIMAX ALGORITHM")

    nodes_evaluated = 0

    minimax_result = minimax(0, 0, True)

    print("Optimal Value:", minimax_result)
    print("Nodes Evaluated:", nodes_evaluated)

    print("\nALPHA-BETA PRUNING")

    nodes_evaluated = 0

    result = alphabeta(
        0,
        0,
        True,
        -math.inf,
        math.inf
    )

    print("\nOptimal Value:", result)
    print("Nodes Evaluated:", nodes_evaluated)

    print("\nAlpha-Beta Pruning Completed!")
