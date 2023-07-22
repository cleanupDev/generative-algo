def _normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)


def fitness(
    pop: list[int],
    max_budget: float,
    max_weight: float,
    data: list[dict],
    item_data: dict,
) -> float:
    '''Calculate the fitness of a pop.
    
    Args:
        pop (list[int]): The pop to calculate the fitness of.
        max_budget (float): The max budget.
        max_weight (float): The max weight.
        data (list[dict]): The data to use.
        item_data (dict): The item data to use.

    Returns:
        score (float): The fitness score of the pop.
    '''
    
    # Gets the data for the selected items from the pop
    selected_items = [data[i] for i, item in enumerate(pop) if item == 1]

    if not selected_items:
        return 0

    total_price = sum(item["price"] for item in selected_items)
    total_weight = sum(item["weight"] for item in selected_items)
    total_usage = sum(item["usage"] for item in selected_items)

    normalized_price = _normalize(
        total_price, item_data["min_price"], item_data["max_price"]
    )
    normalized_weight = _normalize(
        total_weight, item_data["min_weight"], item_data["max_weight"]
    )
    normalized_usage = _normalize(
        total_usage, item_data["min_usage"], item_data["max_usage"]
    )

    price_weight = 0.7
    weight_weight = 0.7
    usage_weight = 1.3

    score = (
        (price_weight * normalized_price)
        + (weight_weight * normalized_weight)
        + (usage_weight * normalized_usage)
    )

    budget_diff = max(total_price - max_budget, 0)
    weight_diff = max(total_weight - max_weight, 0)
    constraint_penalty = budget_diff + weight_diff
    score -= constraint_penalty

    return score


def final_values(pop, data):
    values = [
        (data[i]["price"], data[i]["weight"], data[i]["usage"])
        for i, item in enumerate(pop)
        if item == 1
    ]
    sum_values = [sum(x) for x in zip(*values)]
    return sum_values
