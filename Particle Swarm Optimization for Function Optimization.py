import random

# Define the function to optimize
def fitness_function(x):
    return x ** 2

# Initialize parameters
num_particles = 30
iterations = 50
w, c1, c2 = 0.5, 1.5, 1.5  # Inertia, cognitive, and social coefficients
lower_bound, upper_bound = -10, 10

# Initialize particles
positions = [random.uniform(lower_bound, upper_bound) for _ in range(num_particles)]
velocities = [random.uniform(-1, 1) for _ in range(num_particles)]
personal_best_positions = positions[:]
global_best_position = max(personal_best_positions, key=fitness_function)

# PSO Algorithm
for _ in range(iterations):
    for i in range(num_particles):
        fitness = fitness_function(positions[i])
        if fitness > fitness_function(personal_best_positions[i]):
            personal_best_positions[i] = positions[i]
        if fitness > fitness_function(global_best_position):
            global_best_position = positions[i]

        velocities[i] = (w * velocities[i] +
                         c1 * random.random() * (personal_best_positions[i] - positions[i]) +
                         c2 * random.random() * (global_best_position - positions[i]))
        positions[i] += velocities[i]

print(f"Best Solution (PSO): x = {global_best_position}, f(x) = {fitness_function(global_best_position)}")
