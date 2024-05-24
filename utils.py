import numpy as np

def load_array(filename):
    return np.load(filename)

def save_results(filename, results):
    with open(filename, 'w') as f:
        for result in results:
            f.write(f"{result}\n")

def log_time(filename, label, time):
    with open(filename, 'a') as f:
        f.write(f"{label}: {time} seconds\n")
