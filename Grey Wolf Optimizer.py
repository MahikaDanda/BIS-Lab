# Define the function to optimize
def fitness_function(x):
    return x ** 2

# Initialize parameters
num_wolves = 20
iterations = 50
lower_bound, upper_bound = -10, 10

# Initialize wolves
wolves = np.random.uniform(lower_bound, upper_bound, num_wolves)
alpha, beta, delta = None, None, None

# GWO Algorithm
for _ in range(iterations):
    wolves = sorted(wolves, key=fitness_function, reverse=True)
    alpha, beta, delta = wolves[:3]

    for i in range(num_wolves):
        a = 2 - (2 * _ / iterations)
        r1, r2 = np.random.random(), np.random.random()
        A1, C1 = 2 * a * r1 - a, 2 * r2
        D_alpha = abs(C1 * alpha - wolves[i])
        X1 = alpha - A1 * D_alpha

        r1, r2 = np.random.random(), np.random.random()
        A2, C2 = 2 * a * r1 - a, 2 * r2
        D_beta = abs(C2 * beta - wolves[i])
        X2 = beta - A2 * D_beta

        r1, r2 = np.random.random(), np.random.random()
        A3, C3 = 2 * a * r1 - a, 2 * r2
        D_delta = abs(C3 * delta - wolves[i])
        X3 = delta - A3 * D_delta

        wolves[i] = (X1 + X2 + X3) / 3

best_solution = max(wolves, key=fitness_function)
print(f"Best Solution (GWO): x = {best_solution}, f(x) = {fitness_function(best_solution)}")
