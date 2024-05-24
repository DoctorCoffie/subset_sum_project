import time

def time_backtracking(arr):
    start_time = time.time()
    best_solution = []
    best_sum = float('inf')

    def backtrack(start, curr_subset):
        nonlocal best_solution, best_sum
        curr_sum = sum(curr_subset)
        if abs(curr_sum) < abs(best_sum):
            best_solution = curr_subset[:]
            best_sum = curr_sum
        for i in range(start, len(arr)):
            curr_subset.append(arr[i])
            backtrack(i + 1, curr_subset)
            curr_subset.pop()

    backtrack(0, [])
    time_taken = time.time() - start_time
    return best_solution, time_taken
