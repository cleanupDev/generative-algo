import random

def initial_population(population_size: int, pop_size: int) -> list[list[int]]:
    population: list[list[int]] = []
    for _ in range(population_size):
        population.append([random.getrandbits(1) for _ in range(pop_size)])
        
    return population