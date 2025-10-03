from math import tan
from Matrix import Matrix

def projection(fov: float, ratio: float, near: float, far: float):
    """
    Compute a 4x4 perspective projection matrix (OpenGL-style, column-major).

    Args:
        fov (float): Field of view (in radians).
        ratio (float): Aspect ratio (width / height).
        near (float): Near clipping plane.
        far (float): Far clipping plane.
    Returns:
        Matrix: The projection matrix.
    Raises:
		ValueError: If near or far are non-positive, or if near is not less than far.
	"""
    if near <= 0 or far <= 0:
        raise ValueError("Near and far must be positive.")
    if near >= far:
        raise ValueError("Near must be less than far.")

    f = 1.0 / tan(fov / 2.0)
    a = ratio
    n, fr = near, far

    cols = [
        [f / a, 0,    0,                     0],
        [0,     f,    0,                     0],
        [0,     0,    fr / (fr - n),         1],
        [0,     0,   -(fr * n) / (fr - n),   0]
    ]
    return Matrix.from_columns(cols)
