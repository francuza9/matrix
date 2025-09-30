from Vector import Vector

def linear_combination(vectors, scalars):
    result = Vector([0] * vectors[0].size())

    for vec, scalar in zip(vectors, scalars):
        scaled = vec.scl(scalar)
        result = result + scaled
    return result