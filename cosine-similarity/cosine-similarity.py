import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dotprod = np.dot(a,b)
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)

    if mag_a*mag_b == 0:
        return float(0)
    cos = float(dotprod/(mag_a*mag_b))

    return cos
    
    pass