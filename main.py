import os
from utils import load_array, save_results, log_time
from algorithms.backtracking import time_backtracking
from algorithms.neighborhood_search import neighborhood_search
from algorithms.simulated_annealing import time_simulated_annealing
from algorithms.genetic_algorithm import time_genetic_algorithm

def main():
    if not os.path.exists("results"):
        os.makedirs("results")
    if not os.path.exists("results/graphs"):
        os.makedirs("results/graphs")
        
    array_files = ["IA8.npy", "IA10.npy", "IA50.npy", "IA100.npy"]
    results = []

    for array_file in array_files:
        arr = load_array(f"data/{array_file}")
        
        # Backtracking (only for IA8 and IA10)
        if array_file in ["IA8.npy", "IA10.npy"]:
            solution, time_taken = time_backtracking(arr)
            results.append((f"SB-{len(arr)}", solution))
            log_time("results/times.txt", f"TB-{len(arr)}", time_taken)
        
        # Neighborhood Search
        solution, time_taken = neighborhood_search(arr)
        results.append((f"SNS-{len(arr)}", solution))
        log_time("results/times.txt", f"TNS-{len(arr)}", time_taken)
        
        # Simulated Annealing
        sa_parameters = [(1500, 500, 0.9), (15000, 1500, 0.99)]
        for i, (initial_temp, temp_length, cooling_ratio) in enumerate(sa_parameters):
            solution, time_taken = time_simulated_annealing(arr, initial_temp, temp_length, cooling_ratio)
            results.append((f"S{i}SA-{len(arr)}", solution))
            log_time("results/times.txt", f"T{i}SA-{len(arr)}", time_taken)
        
        # Genetic Algorithm
        ga_parameters = [(1000, 50, 0.8, 0.15, 0.05), (50, 1000, 0.6, 0.3, 0.1)]
        for i, (pop_size, iterations, crossover_rate, mutation_rate, cloning_rate) in enumerate(ga_parameters):
            solution, time_taken = time_genetic_algorithm(arr, pop_size, iterations, crossover_rate, mutation_rate, cloning_rate)
            results.append((f"S{i}GA-{len(arr)}", solution))
            log_time("results/times.txt", f"T{i}GA-{len(arr)}", time_taken)
        
        # Save intermediate results
        save_results("results/solutions.txt", results)
        

    print("All operations completed successfully.")


if __name__ == "__main__":
    main()
