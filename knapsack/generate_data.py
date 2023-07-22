import random
import json
import tqdm


def _generate_items(number_of_items: int) -> list[dict]:
    items: list = []
    for i in tqdm.tqdm(range(number_of_items)):
        item = {}
        item["name"] = "Item " + str(i)
        item["price"] = random.randint(1, 1000)
        item["weight"] = random.randint(1, 10)
        item["usage"] = random.randint(0, 100)
        items.append(item)
    return items


def _write_items_to_json_file(items: list[dict], filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(items, file, indent=4, separators=(", ", ": "))


def generate_data(number_of_items: int, filename: str) -> None:
    items = _generate_items(number_of_items)
    _write_items_to_json_file(items, filename)
    print("DONE")
