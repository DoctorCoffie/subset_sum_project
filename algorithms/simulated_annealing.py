import time
import random
import math

def time_simulated_annealing(arr, initial_temp, temp_length, cooling_ratio):
    start_time = time.time()

    def subset_sum(solution):
        return sum(arr[i] for i in range(len(arr)) if solution[i])

    current_solution = [random.choice([True, False]) for _ in range(len(arr))]
    best_solution = current_solution[:]
    best_sum = subset_sum(current_solution)
    temperature = initial_temp

    while temperature > 1:
        for _ in range(temp_length):
            new_solution = current_solution[:]
            index = random.randint(0, len(arr) - 1)
            new_solution[index] = not new_solution[index]

            current_sum = subset_sum(current_solution)
            new_sum = subset_sum(new_solution)
            delta = new_sum - current_sum

            if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature):
                current_solution = new_solution[:]
                current_sum = new_sum

            if abs(current_sum) < abs(best_sum):
                best_solution = current_solution[:]
                best_sum = current_sum

        temperature *= cooling_ratio

    time_taken = time.time() - start_time
    return best_solution, time_taken
