import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dotprod = float(np.dot(a,b))
    mag_a = float(np.linalg.norm(a))
    mag_b=float(np.linalg.norm(b))

    if mag_a*mag_b == 0:
        return float(0)
    cos = dotprod/(mag_a*mag_b)

    return cos
    
    pass