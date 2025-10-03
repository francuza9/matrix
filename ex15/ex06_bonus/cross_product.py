from Vector import Vector
from math import fma

def cross_product(u, v):
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("Both arguments must be Vector instances.")
    if u.size() != 3 or v.size() != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")

    x = u.data[1] * v.data[2] - u.data[2] * v.data[1]
    y = u.data[2] * v.data[0] - u.data[0] * v.data[2]
    z = u.data[0] * v.data[1] - u.data[1] * v.data[0]

    return Vector([x, y, z])
