from grid import grid, start, goal
from algorithms import greedy_best_first_search, a_star_search
import time

if __name__ == "__main__":
    # Greedy Best-First Search
    start_time = time.time()
    path_greedy = greedy_best_first_search(grid, start, goal)
    time_greedy = time.time() - start_time
    print("Greedy Best-First Search:")
    print("Path found:", path_greedy)
    print("Time taken: {:.6f} seconds".format(time_greedy))

    # A* Search
    start_time = time.time()
    path_a_star = a_star_search(grid, start, goal)
    time_a_star = time.time() - start_time
    print("\nA* Search:")
    print("Path found:", path_a_star)
    print("Time taken: {:.6f} seconds".format(time_a_star))

    # Efficiency Comparison
    print("\nEfficiency Comparison:")
    print("Greedy Best-First Search took {:.6f} seconds".format(time_greedy))
    print("A* Search took {:.6f} seconds".format(time_a_star))

    # Path Quality Comparison
    print("\nPath Quality Comparison:")
    print("Length of path found by Greedy:", len(path_greedy) if path_greedy else "No path found")
    print("Length of path found by A*:", len(path_a_star) if path_a_star else "No path found")
