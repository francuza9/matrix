
class Vector:
    def __init__(self, data):
        """
        Initialize the Vector with a list.

        Args:
            data (list): The data to initialize the vector with.
        Raises:
            ValueError: If data is empty or not a list.
        """
        if not data:
            raise ValueError("Data cannot be empty.")
        if not isinstance(data, list):
            raise ValueError("Data must be a list.")
        self.data = data[:]

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