from math import fma

# Functions changed: __init__, mul_vec, mul_mat
class Matrix:

	def __init__(self, data):
		"""
		Initialize the Matrix in column-major order.
		
		Args:
			data (list of lists): Row-major matrix (outer list = rows, inner list = row values).
		Raises:
			ValueError: If data is empty, not a list of lists, contains non-numeric elements,
						or if rows are of inconsistent lengths.
		"""
		if not data or not all(isinstance(row, list) for row in data):
			raise ValueError("Data must be a non-empty list of row lists.")
		if not all(all(isinstance(x, (int, float, complex)) for x in row) for row in data):
			raise ValueError("All elements in data must be int, float, or complex.")

		expected_cols = len(data[0])
		for i, row in enumerate(data):
			if len(row) != expected_cols:
				raise ValueError(f"All rows must have the same length. Row {i} has {len(row)}, expected {expected_cols}")

		# Transpose rows -> columns for column-major storage
		self.data = [[row[j] for row in data] for j in range(expected_cols)]

	def mul_vec(self, vector):
		"""
		Multiply the matrix (m×n) by a vector (size n).
		Returns a new Vector (size m).
		"""
		from Vector import Vector
		if not isinstance(vector, Vector):
			raise ValueError("The operand must be a Vector.")
		if not self.data:
			raise ValueError("Matrix is empty.")

		rows, cols = self.shape()
		if vector.size() != cols:
			raise ValueError(f"Incompatible dimensions: matrix has {cols} cols, vector has size {vector.size()}")

		results = []
		for i in range(rows):  # iterate rows
			dot = 0
			for j in range(cols):  # iterate columns
				dot += self.data[j][i] * vector.data[j]
			results.append(dot)
		return Vector(results)

	def mul_mat(self, mat):
		"""
		Multiply matrix A (m×n) by matrix B (n×p).
		Returns C = A·B (m×p), stored in column-major order.
		"""
		if not isinstance(mat, Matrix):
			raise ValueError("Argument must be a Matrix.")
		if not self.data or not mat.data:
			raise ValueError("One of the matrices is empty.")

		rows_A, cols_A = self.shape()
		rows_B, cols_B = mat.shape()

		if cols_A != rows_B:
			raise ValueError(f"Incompatible dimensions: A is {rows_A}x{cols_A}, B is {rows_B}x{cols_B}")

		result_cols = []
		for j in range(cols_B):           # for each column of B / C
			col_result = []
			for i in range(rows_A):       # for each row of A / C
				dot = 0
				for k in range(cols_A):   # shared dimension
					dot += self.data[k][i] * mat.data[j][k]  # A[i,k] * B[k,j]
				col_result.append(dot)
			result_cols.append(col_result)
		return Matrix.from_columns(result_cols)

	@classmethod
	def from_columns(cls, columns):
		"""
		Create a Matrix directly from column-major data.
		
		Args:
			columns (list of lists): Column-major representation
									(outer list = columns, inner list = values in that column).
		"""
		m = cls.__new__(cls)       # bypass __init__
		m.data = [list(col) for col in columns]
		return m

	def __add__(self, other):
		"""
		Add two matrices element-wise.

		Args:
			other (Matrix): The matrix to add.
		Returns:
			Matrix: A new Matrix instance representing the sum.
		"""
		if not isinstance(other, Matrix):
			return NotImplemented
		result_cols = []
		for col_self, col_other in zip(self.data, other.data):
			result_cols.append([a + b for a, b in zip(col_self, col_other)])
		return Matrix.from_columns(result_cols)

	def __sub__(self, other):
		"""
		Subtract two matrices element-wise.

		Args:
			other (Matrix): The matrix to subtract.
		Returns:
			Matrix: A new Matrix instance representing the difference.
		"""
		if not isinstance(other, Matrix):
			return NotImplemented
		result_cols = []
		for col_self, col_other in zip(self.data, other.data):
			result_cols.append([a - b for a, b in zip(col_self, col_other)])
		return Matrix.from_columns(result_cols)
	
	def scl(self, scalar):
		"""
		Scale the matrix by a scalar.

		Args:
			scalar (float): The scalar to multiply each element by.
		Returns:
			Matrix: A new Matrix instance representing the scaled matrix.
		"""
		result_cols = []
		for col in self.data:
			result_cols.append([scalar * x for x in col])
		return Matrix.from_columns(result_cols)
	
	def __eq__(self, other):
		"""
		Check if two matrices are equal within a small tolerance.

		Args:
			other (Matrix): The matrix to compare with.
		Returns:
			bool: True if matrices are equal, False otherwise.
		"""
		if not isinstance(other, Matrix):
			return False
		if self.shape() != other.shape():
			return False
		
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				if abs(self.data[i][j] - other.data[i][j]) > 1e-6:
					return False
		return True

	def shape(self):
		"""
		Get the shape of the matrix as (number of rows, number of columns).

		Returns:
			tuple: A tuple (rows, cols) representing the shape of the matrix.
		"""
		if not self.data:
			return (0, 0)
		return (len(self.data[0]), len(self.data))  # (rows, cols)
	
	def is_square(self):
		"""
		Check if the matrix is square (number of rows equals number of columns).

		Returns:
			bool: True if the matrix is square, False otherwise.
		"""
		if not self.data:
			return False
		rows, cols = self.shape()
		return rows == cols

	def __str__(self):
		if not self.data:
			return "M[]"
		rows, cols = self.shape()
		lines = []
		for i in range(rows):
			row = [str(self.data[j][i]) for j in range(cols)]
			lines.append("[" + ", ".join(row) + "]")
		return "\n".join(lines)
	
	def to_vector(self):
		""" 
		Convert the matrix into a vector by flattening its elements.

		Returns:
			Vector: A new Vector instance containing all elements of the matrix in a single list.
		"""
		from Vector import Vector
		flat = [elem for col in self.data for elem in col]
		return Vector(flat)
