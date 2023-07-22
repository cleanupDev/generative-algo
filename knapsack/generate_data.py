import random
import json

def generate_items(number_of_items: int) -> list[dict]:
    items: list = []
    for i in range(number_of_items):
        item = {}
        item["name"] = "Item " + str(i)
        item["price"] = random.randint(1, 1000)
        item["weight"] = random.randint(1, 10)
        item["usage"] = random.randint(0, 100)
        items.append(item)
    return items


def write_items_to_json_file(items: list[dict], filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(items, file, indent=4, separators=(", ", ": "))


