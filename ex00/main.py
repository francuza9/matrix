from Matrix import Matrix
from Vector import Vector

class Colors:
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = BOLD + RED + UNDERLINE
    TEST = RED + UNDERLINE
    END = '\033[0m'

# VECTOR TESTS
def vector_validation():
    print(f"\n{Colors.HEADER}--- VECTOR VALIDATION ---{Colors.END}\n")
    # Creation
    print("Creating vectors v1 and v2...")
    v1 = Vector([2, 3])
    v2 = Vector([5, 7])
    print(f"Vector v1 with size {v1.size()}: {v1}")
    print(f"Vector v2 with size {v2.size()}: {v2}")
    print()
    # Addition
    print(f"{Colors.TEST}Testing Addition{Colors.END}", end="\n---\n")
    v_sum = v1 + v2
    print(f"v1 + v2 = {v_sum}")
    print()
    # Subtraction
    print(f"{Colors.TEST}Testing Subtraction{Colors.END}", end="\n---\n")
    v_diff = v1 - v2
    print(f"v1 - v2 = {v_diff}")
    print()
    # Scaling
    print(f"{Colors.TEST}Testing Scaling{Colors.END}", end="\n---\n")
    scalar = 2
    v_scaled = v1.scl(scalar)
    print(f"v1 scaled by {scalar}: {v_scaled}")
    print()
    # Reshape to Matrix
    print(f"{Colors.TEST}Testing Reshape to Matrix{Colors.END}", end="\n---\n")
    matrix = v1.to_matrix(1, 2)
    print(f"v1 reshaped to matrix (1x2):\n{matrix}")

# MATRIX TESTS
def matrix_validation():
    print(f"\n{Colors.HEADER}--- MATRIX VALIDATION ---{Colors.END}\n")
    # Creation
    print("Creating matrices m1 and m2...")
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[7, 4], [-2, 2]])
    print(f"Matrix m1 with shape {m1.shape()}:\n{m1}")
    print(f"Matrix m2 with shape {m2.shape()}:\n{m2}")
    print()
    # Addition
    print(f"{Colors.TEST}Testing Addition{Colors.END}", end="\n---\n")
    m_sum = m1 + m2
    print(f"m1 + m2 =\n{m_sum}")
    print()
    # Subtraction
    print(f"{Colors.TEST}Testing Subtraction{Colors.END}", end="\n---\n")
    m_diff = m1 - m2
    print(f"m1 - m2 =\n{m_diff}")
    print()
    # Scaling
    print(f"{Colors.TEST}Testing Scaling{Colors.END}", end="\n---\n")
    scalar = 3
    m_scaled = m1.scl(scalar)
    print(f"m1 scaled by {scalar}:\n{m_scaled}")
    print()
    # Check if square
    print(f"{Colors.TEST}Checking if m1 is square{Colors.END}", end="\n---\n")
    print(f"Is m1 square? {m1.is_square()}")
    print()
    # Convert to Vector
    print(f"{Colors.TEST}Testing Conversion to Vector{Colors.END}", end="\n---\n")
    v_from_m = m1.to_vector()
    print(f"m1 converted to vector: {v_from_m}")
    

vector_validation()
matrix_validation()