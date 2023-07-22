def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)


def fitness(
    pop: list[int],
    max_budget: float,
    max_weight: float,
    data: list[dict],
    item_data: dict,
) -> float:
    selected_items = [data[i] for i, item in enumerate(pop) if item == 1]

    if not selected_items:
        return 0

    # Calculate the total price, weight, and usage
    total_price = sum(item["price"] for item in selected_items)
    total_weight = sum(item["weight"] for item in selected_items)
    total_usage = sum(item["usage"] for item in selected_items)

    # Normalize the values (min-max normalization)
    normalized_price = normalize(
        total_price, item_data["min_price"], item_data["max_price"]
    )
    normalized_weight = normalize(
        total_weight, item_data["min_weight"], item_data["max_weight"]
    )
    normalized_usage = normalize(
        total_usage, item_data["min_usage"], item_data["max_usage"]
    )

    # Apply weights to the normalized components
    price_weight = 1.0
    weight_weight = 1.0
    usage_weight = 1.0

    # Calculate the weighted sum fitness score
    score = (
        (price_weight * normalized_price)
        + (weight_weight * normalized_weight)
        + (usage_weight * normalized_usage)
    )

    # Apply constraint penalty
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
