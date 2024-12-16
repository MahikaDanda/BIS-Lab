# Define the function to optimize
def fitness_function(x):
    return x ** 2

# Initialize parameters
population_size = 10
num_generations = 50
num_genes = 5
mutation_rate = 0.1
crossover_rate = 0.8
lower_bound, upper_bound = -10, 10

# Initialize population
population = [np.random.uniform(lower_bound, upper_bound, num_genes) for _ in range(population_size)]

# Gene Expression Algorithm
for _ in range(num_generations):
    fitness = [sum(map(fitness_function, individual)) for individual in population]
    new_population = []

    # Selection
    for _ in range(population_size // 2):
        parents = np.random.choice(population, size=2, p=np.array(fitness) / sum(fitness))
        
        # Crossover
        if random.random() < crossover_rate:
            point = random.randint(1, num_genes - 1)
            child1 = np.concatenate((parents[0][:point], parents[1][point:]))
            child2 = np.concatenate((parents[1][:point], parents[0][point:]))
        else:
            child1, child2 = parents

        # Mutation
        for child in (child1, child2):
            for gene in range(num_genes):
                if random.random() < mutation_rate:
                    child[gene] += random.uniform(-1, 1)
            new_population.append(child)

    population = new_population

# Output the best solution
best_individual = max(population, key=lambda x: sum(map(fitness_function, x)))
print(f"Best Solution (GEA): x = {best_individual}, f(x) = {sum(map(fitness_function, best_individual))}")
