import random
import numpy as np

# Define the function to optimize
def fitness_function(x):
    return x ** 2

# Initialize parameters
population_size = 10
generations = 50
mutation_rate = 0.1
crossover_rate = 0.8
lower_bound, upper_bound = -10, 10

# Create initial population
population = [random.uniform(lower_bound, upper_bound) for _ in range(population_size)]

# Evaluate fitness
def evaluate_population(pop):
    return [fitness_function(ind) for ind in pop]

# Selection
def select_parents(pop, fitness):
    selected = np.random.choice(pop, size=2, p=fitness/np.sum(fitness))
    return selected

# Crossover
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        point = random.uniform(0, 1)
        child1 = point * parent1 + (1 - point) * parent2
        child2 = point * parent2 + (1 - point) * parent1
        return child1, child2
    return parent1, parent2

# Mutation
def mutate(individual):
    if random.random() < mutation_rate:
        return individual + random.uniform(-1, 1)
    return individual

# Genetic Algorithm
for generation in range(generations):
    fitness = evaluate_population(population)
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = select_parents(population, fitness)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    population = new_population

# Output the best solution
best_individual = max(population, key=fitness_function)
print(f"Best Solution (GA): x = {best_individual}, f(x) = {fitness_function(best_individual)}")
