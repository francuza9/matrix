from math import fma

# functions changed: __init__, dot
class Vector:
    def __init__(self, data):
        """
        Initialize the Vector with a list.

        Args:
            data (list): The data to initialize the vector with.
        Raises:
            ValueError: If data is empty, not a list, or contains non-numeric elements.
        """
        if not data:
            raise ValueError("Data cannot be empty.")
        if not isinstance(data, list):
            raise ValueError("Data must be a list.")
		if not all(isinstance(x, (int, float, complex)) for x in data):
			raise ValueError("All elements in data must be int, float, or complex.")
		self.data = data[:]

    def __add__(self, other):
        """
        Add two vectors element-wise.

        Args:
            other (Vector): The vector to add.
        Returns:
            Vector: A new Vector instance representing the sum.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        """
        Subtract two vectors element-wise.

        Args:
            other (Vector): The vector to subtract.
        Returns:
            Vector: A new Vector instance representing the difference.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector([a - b for a, b in zip(self.data, other.data)])
    
    def scl(self, scalar):
        """
        Scale the vector by a scalar.

        Args:
            scalar (float): The scalar to multiply each element by.
        Returns:
            Vector: A new Vector instance representing the scaled vector.
        """
        return Vector([scalar * x for x in self.data])
    
    def __eq__(self, other):
        """
        Compare two vectors for equality, handling float/int comparisons.
        
        Args:
            other (Vector): The vector to compare with.
        Returns:
            bool: True if vectors are equal, False otherwise.
        """
        if not isinstance(other, Vector):
            return False
        if self.size() != other.size():
            return False
        # Compare each element with tolerance for floating point comparison
        for a, b in zip(self.data, other.data):
            if abs(a - b) > 1e-6:  # Small tolerance for float comparison
                return False
        return True
    
	def dot(self, other):
		if not isinstance(other, Vector):
			raise ValueError("The operand must be a Vector.")
		if len(self.data) != len(other.data):
			raise ValueError("Vectors must be the same size.")

		result = 0
		for a, b in zip(self.data, other.data):
			result += a.conjugate() * b
		return result


    def size(self):
        """
        Get the size (number of elements) of the vector.

        Returns:
            int: The number of elements in the vector.
        """
        if not self.data:
            return 0
        return len(self.data)
    
    def __str__(self):
        if not self.data:
            return "V[]"
        return f"[{', '.join(map(str, self.data))}]"
    
    def to_matrix(self, rows, cols):
        """ 
        Reshape the vector into a matrix with the specified number of rows and columns.

        Args:
            rows (int): Number of rows in the resulting matrix.
            cols (int): Number of columns in the resulting matrix.
        Returns:
            Matrix: A new Matrix instance with the specified dimensions.
        Raises:
            ValueError: If the vector size does not match rows * cols.
        """
        from Matrix import Matrix
        if self.size() != rows * cols:
            raise ValueError("Cannot reshape vector to the specified matrix dimensions.")
        matrix_data = []
        for i in range(rows):
            row = self.data[i*cols:(i+1)*cols]
            matrix_data.append(row)
        return Matrix(matrix_data)