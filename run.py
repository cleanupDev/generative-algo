from knapsack import knapsack_algo, read_data, final_values, generate_data

# GENERATE DATA WITH generate_data.py FIRST!

POPULATION_SIZE = 10
GENERATIONS = 100000
MUTATION_RATE = 0.00025
DATA = read_data("data/data.json")
MAX_BUDGET = 15000
MAX_WEIGHT = 1500
EARLY_STOP = 5000

if __name__ == "__main__":
    result, result_fitness = knapsack_algo(
        POPULATION_SIZE, GENERATIONS, MUTATION_RATE, DATA, MAX_BUDGET, MAX_WEIGHT
    )
    final_values = final_values(result[0], DATA)
    print(f"Fitness: {result_fitness}")
    print(f"Budget: {final_values[0]} of {MAX_BUDGET}")
    print(f"Weight: {final_values[1]} of {MAX_WEIGHT}")
    print(f"Usage: {final_values[2]}")