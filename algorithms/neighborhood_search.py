import time
import random

def neighborhood_search(arr):
    start_time = time.time()

    def get_neighbors(solution):
        neighbors = []
        for i in range(len(solution)):
            neighbor = solution[:]
            neighbor[i] = not neighbor[i]
            neighbors.append(neighbor)
        return neighbors

    def subset_sum(solution):
        return sum(arr[i] for i in range(len(arr)) if solution[i])

    current_solution = [random.choice([True, False]) for _ in range(len(arr))]
    best_solution = current_solution[:]
    best_sum = subset_sum(current_solution)

    for _ in range(1000):  # Number of iterations
        neighbors = get_neighbors(current_solution)
        for neighbor in neighbors:
            current_sum = subset_sum(neighbor)
            if abs(current_sum) < abs(best_sum):
                best_solution = neighbor[:]
                best_sum = current_sum

    time_taken = time.time() - start_time
    return best_solution, time_taken
