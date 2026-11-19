from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))

    counter = Counter(x)
    max_frequency = max(counter.values())

    mode = min(value for value,frequency in counter.items()
              if frequency == max_frequency)

    return {"mean": mean , "median": median , "mode": float(mode)}
    pass