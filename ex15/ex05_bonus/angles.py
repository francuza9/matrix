from Vector import Vector

def angle_cos(u, v) -> float:
	"""
	Compute the cosine of the angle between two vectors.

	Args:
		u (Vector): The first vector.
		v (Vector): The second vector.
	Returns:
		float: The cosine of the angle between u and v.
	Raises:
		ValueError: If either vector is zero-length or if inputs are not Vectors.
	"""
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise ValueError("Both arguments must be Vector instances.")

	nu, nv = u.norm(), v.norm()
	if nu == 0 or nv == 0:
		raise ValueError("Cannot compute angle with zero-length vector.")

	inner = u.dot(v)  # may be complex
	return inner.real / (nu * nv)