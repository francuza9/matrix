from Vector import Vector
from math import fma

def cross_product(u, v):
    """
    Compute the cross product of two 3D vectors.

    Args:
        u (Vector): The first vector (must be 3-dimensional).
        v (Vector): The second vector (must be 3-dimensional).
    Returns:
        Vector: The cross product vector.
    Raises:
        ValueError: If either vector is not 3-dimensional or if inputs are not Vectors.
    """
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("Both arguments must be Vector instances.")
    x = fma(u.data[1], v.data[2], -u.data[2] * v.data[1])
    y = fma(u.data[2], v.data[0], -u.data[0] * v.data[2])
    z = fma(u.data[0], v.data[1], -u.data[1] * v.data[0])
    return Vector([x, y, z])