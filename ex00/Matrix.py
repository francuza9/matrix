
class Matrix:

    def __init__(self, data):
        """
        Initialize the Matrix with a list of lists.

        Args:
            data (list of lists): The data to initialize the matrix with.
        Raises:
            ValueError: If data is empty or not a list of lists, or if rows have inconsistent lengths.
        """
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Data must be a non-empty list of lists.")
        if data:
            expected_cols = len(data[0])
            for i, row in enumerate(data):
                if len(row) != expected_cols:
                    raise ValueError(f"All rows must have same length. Row {i} has {len(row)}, expected {expected_cols}")
        self.data = [row[:] for row in data]

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
        result_data = []
        for row_self, row_other in zip(self.data, other.data):
            result_data.append([a + b for a, b in zip(row_self, row_other)])
        return Matrix(result_data)
    
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
        result_data = []
        for row_self, row_other in zip(self.data, other.data):
            result_data.append([a - b for a, b in zip(row_self, row_other)])
        return Matrix(result_data)
    
    def scl(self, scalar):
        """
        Scale the matrix by a scalar.

        Args:
            scalar (float): The scalar to multiply each element by.
        Returns:
            Matrix: A new Matrix instance representing the scaled matrix.
        """
        result_data = []
        for row in self.data:
            result_data.append([scalar * x for x in row])
        return Matrix(result_data)

    def shape(self):
        """
        Get the shape of the matrix as (number of rows, number of columns).

        Returns:
            tuple: A tuple (rows, cols) representing the shape of the matrix.
        """
        if not self.data:
            return (0, 0)
        return (len(self.data), len(self.data[0]) if self.data else 0)
    
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
        return '\n'.join([f"[{', '.join(map(str, row))}]" for row in self.data])
    
    def to_vector(self):
        """ 
        Convert the matrix into a vector by flattening its elements.

        Returns:
            Vector: A new Vector instance containing all elements of the matrix in a single list.
        """
        from Vector import Vector
        if not self.data:
            return Vector([])
        flat_data = [elem for row in self.data for elem in row]
        return Vector(flat_data)