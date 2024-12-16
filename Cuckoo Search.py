import numpy as np

# Define the function to optimize
def fitness_function(x):
    return x ** 2

# Lévy flight step
def levy_flight(Lambda):
    return np.random.normal(0, 1) / (abs(np.random.normal(0, 1)) ** (1 / Lambda))

# Initialize parameters
num_nests = 15
iterations = 50
discovery_rate = 0.25
lower_bound, upper_bound = -10, 10

# Initialize nests
nests = np.random.uniform(lower_bound, upper_bound, num_nests)

# Cuckoo Search Algorithm
for _ in range(iterations):
    new_nests = nests.copy()
    for i in range(num_nests):
        step_size = levy_flight(1.5)
        new_nests[i] += step_size
        if fitness_function(new_nests[i]) > fitness_function(nests[i]):
            nests[i] = new_nests[i]

    # Abandon a fraction of the worst nests
    worst_indices = np.argsort([fitness_function(x) for x in nests])[:int(discovery_rate * num_nests)]
    for idx in worst_indices:
        nests[idx] = np.random.uniform(lower_bound, upper_bound)

best_solution = max(nests, key=fitness_function)
print(f"Best Solution (CS): x = {best_solution}, f(x) = {fitness_function(best_solution)}")
