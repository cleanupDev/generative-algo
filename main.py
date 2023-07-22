import random
import json
from knapsack.initial_population import initial_population
from knapsack.fitness import fitness
from knapsack.crossover import crossover

    
def read_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


data = read_data("data.json")


def main(population_size, generations, mutation_rate, data, max_budget, max_weight):
    population = initial_population(population_size, len(data))
    population = sorted(population, key=lambda x: fitness(x, max_budget, max_weight, data), reverse=True)
    
    top_range = int(len(population) * 0.2)
    
    top_pops = population[:top_range]
    
    for i in range(generations):
        next_population = top_pops.copy()
        
        while len(next_population) < len(population):
            parent1, parent2 = random.choices(population, k=2)
            next_population.append(crossover(parent1, parent2, mutation_rate))
            
        population = sorted(next_population, key=lambda x: fitness(x, max_budget, max_weight, data), reverse=True)

        top_pops = population[:top_range]
        
    return population[0]
        
        
