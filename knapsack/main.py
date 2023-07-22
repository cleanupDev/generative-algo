import random
import json
import tqdm
from .initial_population import initial_population
from .fitness import fitness
from .crossover import crossover


def read_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(
            "File not found. Please run generate_data.py to generate the data file."
        )


def knapsack_algo(
    population_size: int,
    generations: int,
    mutation_rate: float,
    data: list[dict],
    max_budget: int,
    max_weight: int,
    early_stop: int = 5000,
):
    """Main logic for the knapsack algo.

    Args:
        population_size (int): The size of the population.
        generations (int): The number of generations to run.
        mutation_rate (float): The mutation rate.
        data (list[dict]): The data to use.
        max_budget (int): The max budget.
        max_weight (int): The max weight.
        early_stop (int, optional): The number of generations to run before early stopping. Defaults to 5000.

    Returns:
        population[0] (list): The best pop from the final generation.
        fitness (float): The fitness score of the best pop.
    """

    # Get the min and max values for the data to later normalize the pop values
    min_item_price = min(item["price"] for item in data)
    max_item_price = max(item["price"] for item in data)
    min_item_weight = min(item["weight"] for item in data)
    max_item_weight = max(item["weight"] for item in data)
    min_item_usage = min(item["usage"] for item in data)
    max_item_usage = max(item["usage"] for item in data)

    # Create a dict of the min and max values for the data for the fitness function
    item_data = {
        "min_price": min_item_price,
        "max_price": max_item_price,
        "min_weight": min_item_weight,
        "max_weight": max_item_weight,
        "min_usage": min_item_usage,
        "max_usage": max_item_usage,
    }

    # Create and sort the initial population by fitness
    population = initial_population(population_size, len(data))
    population = sorted(
        population,
        key=lambda x: fitness(x, max_budget, max_weight, data, item_data),
        reverse=True,
    )

    # Get the top 20% of the population for the next generation
    top_range = int(len(population) * 0.2)

    top_pops = population[:top_range]
    early_stop_count = 0

    for gen in tqdm.tqdm(range(generations), colour="red"):
        if gen % 100 == 0:
            tqdm.tqdm.write(
                f"Generation: {gen} Fitness: {fitness(population[0], max_budget, max_weight, data, item_data):.2f}"
            )
        next_population = top_pops.copy()

        # top pop from the previous generation to check for early stopping
        top_pop_this_gen = next_population[0]

        # Filling the rest of the new generation
        # Parents are selected from the top 80% of the population
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

        # Check for early stopping
        if top_pop_this_gen == population[0]:
            early_stop_count += 1
        else:
            early_stop_count = 0

        if early_stop_count == early_stop:
            return population, fitness(
                population[0], max_budget, max_weight, data, item_data
            )

        top_pops = population[:top_range]

    return population[0], fitness(
        population[0], max_budget, max_weight, data, item_data
    )
