from Vector import Vector
from Matrix import Matrix

def linear_combination(objects, scalars):
	"""
	Compute the linear combination of a list of Vectors or Matrices with given scalars.

	Args:
		objects (list): A list of Vector or Matrix instances.
		scalars (list): A list of scalars corresponding to each object.
	Returns:
		Vector or Matrix: A new instance representing the linear combination.
	"""
	first = objects[0]
	if isinstance(first, Vector):
		result = Vector([0] * first.size())
	elif isinstance(first, Matrix):
		rows, cols = first.shape()
		row_major = [[0 for _ in range(cols)] for _ in range(rows)]
		result = Matrix(row_major)
	else:
		result = first.scl(0)
	
	for obj, scalar in zip(objects, scalars):
		scaled = obj.scl(scalar)
		result = result + scaled
	return result

def lerp(u, v, t):
	"""
	Perform linear interpolation between two Vectors or Matrices.

	Args:
		u (Vector or Matrix): The starting object.
		v (Vector or Matrix): The ending object.
		t (float): The interpolation factor (0 <= t <= 1).
	Returns:
		Vector or Matrix: A new instance representing the interpolated object.
	Raises:
		ValueError: If t is not in the range [0, 1].
	"""
	if not (0 <= t <= 1):
		raise ValueError("Interpolation factor t must be in the range [0, 1].")
	if type(t) not in (int, float):
		raise ValueError("Interpolation factor t must be a float or int.")
	if hasattr(u, 'scl') and hasattr(u, '__add__'):
		return linear_combination([u, v], [1-t, t])
	else:
		return (1-t) * u + t * v