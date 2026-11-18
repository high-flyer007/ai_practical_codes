
import random
import math

# Coordinates of cities
cities = {
    'A': (0, 0),
    'B': (2, 6),
    'C': (5, 3),
    'D': (6, 7),
    'E': (8, 2)
}

# Parameters
K = 3
ITERATIONS = 100

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Calculate total route distance
def route_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])

    # Return to starting city
    total += distance(route[-1], route[0])

    return total


# Generate neighboring routes by swapping cities
def get_neighbors(route):
    neighbors = []

    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = list(route)

            new_route[i], new_route[j] = (
                new_route[j], new_route[i]
            )

            neighbors.append(tuple(new_route))

    return neighbors


# Local Beam Search algorithm
def local_beam_search():
    start_city = 'A'

    # Other cities whose order will be changed
    other_cities = [city for city in cities if city != start_city]

    # Generate K random initial routes
    beam = set()

    while len(beam) < K:
        route = [start_city] + random.sample(
            other_cities, len(other_cities)
        )
        beam.add(tuple(route))

    print("Initial Routes:")
    for route in beam:
        print(route, "Distance:", round(route_distance(route), 2))

    # Repeat for a fixed number of iterations
    for iteration in range(ITERATIONS):

        all_candidates = set()

        # Generate neighbors of every current route
        for route in beam:
            all_candidates.update(get_neighbors(route))

        # Select the best K routes
        beam = set(sorted(
            all_candidates,
            key=route_distance
        )[:K])

    # Find the best route among the final candidates
    best_route = min(beam, key=route_distance)

    return best_route, route_distance(best_route)


# Main program
random.seed(42)

best_route, best_distance = local_beam_search()

print("\nBest Route Found:")
print(" -> ".join(best_route + (best_route[0],)))

print("Total Distance:", round(best_distance, 2))
print("\nLocal Beam Search Completed!")
