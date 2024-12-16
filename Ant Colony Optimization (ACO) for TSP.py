import numpy as np

# Define cities
num_cities = 5
cities = np.random.rand(num_cities, 2)
distances = np.linalg.norm(cities[:, None] - cities[None, :], axis=2)

# Parameters
num_ants = 10
alpha, beta, rho = 1, 2, 0.5
num_iterations = 50
pheromones = np.ones((num_cities, num_cities))

# ACO Algorithm
for _ in range(num_iterations):
    solutions = []
    for ant in range(num_ants):
        visited = [np.random.randint(num_cities)]
        for _ in range(num_cities - 1):
            unvisited = list(set(range(num_cities)) - set(visited))
            probabilities = [
                (pheromones[visited[-1], j] ** alpha) * (1 / distances[visited[-1], j] ** beta)
                for j in unvisited
            ]
            next_city = np.random.choice(unvisited, p=np.array(probabilities) / sum(probabilities))
            visited.append(next_city)
        solutions.append((visited, sum(distances[visited[i], visited[i + 1]] for i in range(-1, num_cities - 1))))

    # Update pheromones
    for path, length in solutions:
        for i in range(num_cities):
            pheromones[path[i], path[(i + 1) % num_cities]] += 1 / length
    pheromones *= (1 - rho)

best_solution = min(solutions, key=lambda x: x[1])
print(f"Best Solution (ACO): Path = {best_solution[0]}, Length = {best_solution[1]}")
