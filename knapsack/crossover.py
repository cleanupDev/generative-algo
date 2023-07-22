import random

def crossover(parent1: list[int], parent2: list[int], mutation_rate: float):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    
    for i, item in enumerate(child):
        if random.random() < mutation_rate:
            child[i] = 1 if item == 0 else 0
            
    return child