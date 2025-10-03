from math import fma

def my_abs(x):
	if isinstance(x, complex):
		return (x.real * x.real + x.imag * x.imag) ** 0.5
	elif x >= 0:
		return x
	else:
		return -x

# Functions changed: __init__, mul_vec, mul_mat, trace, transpose, determinant
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

	def trace(self):
		if not self.is_square():
			raise ValueError("Trace is only defined for square matrices.")
		if not self.data:
			return 0
		diag_sum = 0
		for i in range(len(self.data)):
			diag_sum += self.data[i][i]
		return diag_sum

	def transpose(self):
		"""
		Return the transpose B = A^T,
		stored in column-major order.
		"""
		if not self.data:
			return Matrix.from_columns([])

		rows, cols = self.shape()
		new_cols = []
		for i in range(rows):  # new column index
			new_col = []
			for j in range(cols):  # go through old columns
				new_col.append(self.data[j][i])
			new_cols.append(new_col)

		return Matrix.from_columns(new_cols)

	def determinant(self):
		if not self.is_square():
			raise ValueError("Determinant is only defined for square matrices.")
		
		n, _ = self.shape()
		if n == 0:
			raise ValueError("Determinant is not defined for empty matrices.")
		if n > 4:
			raise NotImplementedError("Determinant calculation is only implemented for matrices up to 4x4.")
		
		if n == 1:
			return self.data[0][0]
		elif n == 2:
			a, b = self.data[0][0], self.data[1][0]
			c, d = self.data[0][1], self.data[1][1]
			return a * d - b * c
		
		det = 0  # <-- was 0.0
		for col in range(n):
			elem = self.data[col][0]
			if abs(elem) < 1e-9:
				continue

			minor_cols = []
			for j in range(n):
				if j == col:
					continue
				minor_col = self.data[j][1:]
				minor_cols.append(minor_col)
			minor = Matrix.from_columns(minor_cols)

			cofactor = ((-1) ** col) * elem * minor.determinant()
			det += cofactor
		return det

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
	
	def swap_rows(self, i, j):
		"""
		Swap row i and row j in the matrix (in-place).
		"""
		rows, cols = self.shape()
		if not (0 <= i < rows and 0 <= j < rows):
			raise IndexError("Row index out of range")
		if i == j:
			return
		for col in self.data:
			col[i], col[j] = col[j], col[i]

	def row_echelon(self):
		A = self.copy()
		rows, cols = A.shape()
		pivot_row = 0

		for col in range(cols):
			# Find pivot in current column (largest modulus)
			pivot = None
			max_val = 0
			for r in range(pivot_row, rows):
				val = my_abs(A.data[col][r])
				if val > max_val + 1e-12:  # strictly compare modulus
					max_val = val
					pivot = r

			if pivot is None:
				continue

			# Swap pivot row with current row
			if pivot != pivot_row:
				A.swap_rows(pivot_row, pivot)

			# Normalize pivot row so pivot = 1
			pivot_val = A.data[col][pivot_row]
			if my_abs(pivot_val) > 1e-12:
				A.scale_row(pivot_row, 1.0 / pivot_val)

			# Eliminate other rows
			for r in range(rows):
				if r == pivot_row:
					continue
				factor = A.data[col][r]
				if my_abs(factor) > 1e-12:
					A.add_multiple_of_row(r, pivot_row, -factor)

			pivot_row += 1
			if pivot_row >= rows:
				break

		return A

	@staticmethod
	def identity(n):
		"""
		Create an n x n identity matrix.

		Args:
			n (int): The size of the identity matrix.
		Returns:
			Matrix: An n x n identity matrix.
		"""
		cols = []
		for j in range(n):
			col = [0.0] * n
			col[j] = 1.0
			cols.append(col)
		return Matrix.from_columns(cols)


	def copy(self):
		"""
		Create a deep copy of the matrix.

		Returns:
			Matrix: A new Matrix instance that is a copy of the current matrix.
		"""
		return Matrix.from_columns([col[:] for col in self.data])


	def add_multiple_of_row(self, target, source, scalar):
		"""
		Add a multiple of row 'source' to row 'target' (in-place).

		Args:
			target (int): Index of the row to be modified.
			source (int): Index of the row to be scaled and added.
			scalar (float): The scalar to multiply the source row by.
		Raises:
			IndexError: If row indices are out of range.
		"""
		rows, _ = self.shape()
		if not (0 <= target < rows and 0 <= source < rows):
			raise IndexError("Row index out of range")
		for col in self.data:
			col[target] += scalar * col[source]


	def scale_row(self, i, scalar):
		"""
		Scale row i by a scalar (in-place).

		Args:
			i (int): Index of the row to scale.
			scalar (float): The scalar to multiply the row by.
		Raises:
			IndexError: If row index is out of range.
		"""
		rows, _ = self.shape()
		if not (0 <= i < rows):
			raise IndexError("Row index out of range")
		for col in self.data:
			col[i] *= scalar


	def swap_rows(self, i, j):
		"""
		Swap row i and row j in the matrix (in-place).

		Args:
			i (int): Index of the first row to swap.
			j (int): Index of the second row to swap.
		Raises:
			IndexError: If row indices are out of range.
		"""
		rows, cols = self.shape()
		if not (0 <= i < rows and 0 <= j < rows):
			raise IndexError("Row index out of range")
		if i == j:
			return
		for col in self.data:
			col[i], col[j] = col[j], col[i]

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
		Handles real and complex entries (treats 1.0 and (1+0j) as equal).
		
		Args:
			other (Matrix): The matrix to compare with.
		Returns:
			bool: True if matrices are equal, False otherwise.
		"""
		if not isinstance(other, Matrix):
			return False
		if self.shape() != other.shape():
			return False
		
		tol = 1e-6
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				a = self.data[i][j]
				b = other.data[i][j]
				try:
					if abs(a - b) > tol:
						return False
				except Exception:
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
