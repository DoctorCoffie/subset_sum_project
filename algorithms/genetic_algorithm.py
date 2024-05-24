import time
import random
import numpy as np

def time_genetic_algorithm(arr, pop_size, iterations, crossover_rate, mutation_rate, cloning_rate):
    start_time = time.time()

    def subset_sum(solution):
        return sum(arr[i] for i in range(len(arr)) if solution[i])

    def generate_initial_population(size, length):
        return [[random.choice([True, False]) for _ in range(length)] for _ in range(size)]

    def select_parents(population):
        selected = sorted(population, key=subset_sum)[:int(len(population) * crossover_rate)]
        return selected

    def crossover(parents):
        offspring = []
        for _ in range(len(parents) // 2):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            cut = np.random.randint(1, len(parent1))
            child1 = parent1[:cut] + parent2[cut:]
            child2 = parent2[:cut] + parent1[cut:]
            offspring.extend([child1, child2])
        return offspring

    def mutate(individual):
        for i in range(len(individual)):
            if random.uniform(0, 1) < mutation_rate:
                individual[i] = not individual[i]
        return individual

    def create_new_population(parents, offspring):
        population = parents + offspring
        for i in range(int(len(population) * cloning_rate)):
            population.append(random.choice(parents))
        return population[:pop_size]

    population = generate_initial_population(pop_size, len(arr))
    best_solution = min(population, key=subset_sum)

    for _ in range(iterations):
        parents = select_parents(population)
        offspring = crossover(parents)
        offspring = [mutate(child) for child in offspring]
        population = create_new_population(parents, offspring)
        current_best = min(population, key=subset_sum)
        if abs(subset_sum(current_best)) < abs(subset_sum(best_solution)):
            best_solution = current_best

    time_taken = time.time() - start_time
    return best_solution, time_taken
