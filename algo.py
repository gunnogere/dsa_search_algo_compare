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
    print(f"{name}:")
    print(f"  Driver : {result['name']}")
    print(f"  Zone   : {result['zone']}")
    print(f"  Status : {result['status']}")
    print(f"  Found  : {elapsed:.6f} ms")
    print()

# Speedup comparison summary
print("SUMMARY (averaged over 100 runs)")
print("-" * 20)

RUNS = 100  # average over multiple runs for more stable, reliable timing

timings = []
for name, search in searches:
    total_time = 0
    for _ in range(RUNS):
        start = time.perf_counter()
        search(target)
        total_time += (time.perf_counter() - start) * 1000
    avg_time = total_time / RUNS
    timings.append((name, avg_time))

baseline = timings[0][1]  # Linear search time as the baseline
for name, elapsed in timings:
    speedup = baseline / elapsed if elapsed > 0 else float('inf')
    print(f"{name:<20} {elapsed:>10.6f} ms avg   ({speedup:>6.1f}x faster than Linear)")