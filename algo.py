import json
import time

# The seed file is already sorted by driver ID.
with open("drivers.json", "r") as file:
    drivers = json.load(file)

# A hash map uses extra memory, but gives fast average lookups.
drivers_map = {driver["id"]: driver for driver in drivers}

def linear_search(search_item):
    """Check every driver from left to right: O(n) time, O(1) space."""
    for driver in drivers:
        if driver["id"] == search_item:
            return driver
    return None

def binary_search(search_item):
    """Repeatedly halve the sorted list: O(log n) time, O(1) space."""
    low = 0
    high = len(drivers) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_id = drivers[middle]["id"]

        if middle_id == search_item:
            return drivers[middle]
        if middle_id < search_item:
            low = middle + 1
        else:
            high = middle - 1

    return None


def hashmap_search(search_item):
    """Use the ID as a key: O(1) average time, O(n) extra space."""
    return drivers_map.get(search_item)


# Search for the last driver so linear search does the most work.
target = drivers[-1]["id"]
searches = [
    ("Linear search", linear_search),
    ("Binary search", binary_search),
    ("Hash map search", hashmap_search),
]

print(f"Searching for {target}\n")

for name, search in searches:
    start = time.perf_counter()
    result = search(target)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"{name}: {result['name']} found in {elapsed:.6f} ms")