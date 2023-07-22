import random
import json
import tqdm
from knapsack.initial_population import initial_population
from knapsack.fitness import final_values, fitness
from knapsack.crossover import crossover


def read_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


POPULATION_SIZE = 10
GENERATIONS = 100000
MUTATION_RATE = 0.00025
DATA = read_data("data/data.json")
MAX_BUDGET = 15000
MAX_WEIGHT = 1500
EARLY_STOP = 5000


def main(
    population_size: int,
    generations: int,
    mutation_rate: float,
    data: list[dict],
    max_budget: int,
    max_weight: int,
    early_stop: int = EARLY_STOP,
):
    min_item_price = min(item["price"] for item in data)
    max_item_price = max(item["price"] for item in data)
    min_item_weight = min(item["weight"] for item in data)
    max_item_weight = max(item["weight"] for item in data)
    min_item_usage = min(item["usage"] for item in data)
    max_item_usage = max(item["usage"] for item in data)

    item_data = {
        "min_price": min_item_price,
        "max_price": max_item_price,
        "min_weight": min_item_weight,
        "max_weight": max_item_weight,
        "min_usage": min_item_usage,
        "max_usage": max_item_usage,
    }

    population = initial_population(population_size, len(data))
    population = sorted(
        population,
        key=lambda x: fitness(x, max_budget, max_weight, data, item_data),
        reverse=True,
    )

    top_range = int(len(population) * 0.2)

    top_pops = population[:top_range]
    early_stop_count = 0

    for gen in tqdm.tqdm(range(generations)):
        tqdm.tqdm.write(
            f"Generation: {gen} Fitness: {fitness(population[0], max_budget, max_weight, data, item_data):.2f}"
        )
        next_population = top_pops.copy()
        top_pop_this_gen = next_population[0]

        while len(next_population) < len(population):
            parent1, parent2 = random.choices(
                population[: (len(population) - top_range)], k=2
            )
            next_population.append(crossover(parent1, parent2, mutation_rate))

        population = sorted(
            next_population,
            key=lambda x: fitness(x, max_budget, max_weight, data, item_data),
            reverse=True,
        )
        if top_pop_this_gen == population[0]:
            early_stop_count += 1
        else:
            early_stop_count = 0

        if early_stop_count == early_stop:
            return population, fitness(
                population[0], max_budget, max_weight, data, item_data
            )

        top_pops = population[:top_range]

    return population, fitness(population[0], max_budget, max_weight, data, item_data)


if __name__ == "__main__":
    result, result_fitness = main(
        POPULATION_SIZE, GENERATIONS, MUTATION_RATE, DATA, MAX_BUDGET, MAX_WEIGHT
    )
    final_values = final_values(result[0], DATA)
    print(f"Fitness: {result_fitness}")
    print(f"Budget: {final_values[0]} of {MAX_BUDGET}")
    print(f"Weight: {final_values[1]} of {MAX_WEIGHT}")
    print(f"Usage: {final_values[2]}")
