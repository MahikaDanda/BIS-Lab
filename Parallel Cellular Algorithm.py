# Define the function to optimize
def fitness_function(x):
    return x ** 2

# Initialize parameters
grid_size = 5
iterations = 50
lower_bound, upper_bound = -10, 10

# Initialize grid of cells
grid = np.random.uniform(lower_bound, upper_bound, (grid_size, grid_size))

# Parallel Cellular Algorithm
for _ in range(iterations):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = [
                grid[i2 % grid_size, j2 % grid_size]
                for i2 in range(i - 1, i + 2)
                for j2 in range(j - 1, j + 2)
                if (i2, j2) != (i, j)
            ]
            best_neighbor = max(neighbors, key=fitness_function)
            new_grid[i, j] = (grid[i, j] + best_neighbor) / 2

    grid = new_grid

best_solution = max(grid.flatten(), key=fitness_function)
print(f"Best Solution (Parallel Cellular): x = {best_solution}, f(x) = {fitness_function(best_solution)}")
