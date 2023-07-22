def fitness(pop: list[int], max_budget: float, max_weight: float , data: list[dict]) -> float:
    values = [(data[i]['price'],data[i]['weight'], data[i]['usage']) for i, item in enumerate(pop) if item == 1]
    sum_values = [sum(x) for x in zip(*values)]
    
    if sum_values == []:
        score = 0
    elif sum_values[0] > max_budget or sum_values[1] > max_weight:
       score = (max_budget - sum_values[0]) + (max_weight - sum_values[1])
    elif sum_values[0] > max_budget:
       score = max_budget - sum_values[0]
    elif sum_values[1] > max_weight:
       score = max_weight - sum_values[1]
    else:
        score = sum_values[2] << 1
    
    return score