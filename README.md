# Search Algorithm Comparison.

This exercise compares three ways to find a driver by ID:

- **Linear search** checks each driver from the beginning: `O(n)` time and `O(1)` extra space.
- **Binary search** repeatedly halves the sorted list: `O(log n)` time and `O(1)` extra space.
- **Hash map search** looks up the ID in a dictionary: `O(1)` average time and `O(n)` extra space.

## Files.

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

The script searches for the last driver in the dataset and prints the full matching driver record (name, zone, status) and elapsed time for each algorithm.

Each search is also run 100 times and averaged for more stable timing results, shown in a SUMMARY table at the end, including a speedup comparison against Linear Search as the baseline.

### Example output

```
Linear search:
  Driver : Claude Uwase
  Zone   : Gasabo
  Status : available
  Found  : 0.036818 ms

SUMMARY (averaged over 100 runs)
--------------------
Linear search          0.036818 ms avg   (baseline)
Binary search           0.001396 ms avg   (  26.4x faster than Linear)
Hash map search          0.000150 ms avg   ( 245.3x faster than Linear)
```

## Requirements

- Python 3
- No third-party packages
