# Search Algorithm Comparison

This exercise compares three ways to find a driver by ID:

- **Linear search** checks each driver from the beginning: `O(n)` time and `O(1)` extra space.
- **Binary search** repeatedly halves the sorted list: `O(log n)` time and `O(1)` extra space.
- **Hash map search** looks up the ID in a dictionary: `O(1)` average time and `O(n)` extra space.

## Files

- `algo.py` loads the data and measures the three search methods.
- `drivers.json` contains the driver records used by the comparison.

Each driver record has this structure:

```json
{
  "id": "DRV_08981",
  "name": "Divine Habimana",
  "status": "busy",
  "zone": "Nyamirambo"
}
```

The IDs in `drivers.json` must remain sorted for `binary_search` to work correctly.

## Run

From this directory, run:

```bash
python3 algo.py
```

The script searches for the last driver in the dataset and prints the matching driver and elapsed time for each algorithm.

## Requirements

- Python 3
- No third-party packages