from Matrix import Matrix
from Vector import Vector

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = BOLD + BLUE + UNDERLINE
    TEST = BLUE + BOLD
    CORRECT = GREEN
    END = '\033[0m'

# VECTOR TESTS
def vector_validation():
    print(f"\n{Colors.HEADER}--- VECTOR VALIDATION ---{Colors.END}\n")
    # Creation
    print("Creating vectors v1 and v2...")
    v1 = Vector([2, 3])
    v2 = Vector([5, 7])
    print(f"Vector v1 with size {Colors.CORRECT}{v1.size()}{Colors.END}: {Colors.GREEN}{v1}{Colors.END}")
    print(f"Vector v2 with size {Colors.CORRECT}{v2.size()}{Colors.END}: {Colors.GREEN}{v2}{Colors.END}")
    print()
    # Addition
    print(f"{Colors.TEST}Testing Addition{Colors.END}", end="\n---\n")
    v_sum = v1 + v2
    print(f"v1 + v2 = {Colors.GREEN}{v_sum}{Colors.END}")
    print()
    # Subtraction
    print(f"{Colors.TEST}Testing Subtraction{Colors.END}", end="\n---\n")
    v_diff = v1 - v2
    print(f"v1 - v2 = {Colors.GREEN}{v_diff}{Colors.END}")
    print()
    # Scaling
    print(f"{Colors.TEST}Testing Scaling{Colors.END}", end="\n---\n")
    scalar = 2
    v_scaled = v1.scl(scalar)
    print(f"v1 scaled by {scalar}: {Colors.GREEN}{v_scaled}{Colors.END}")
    print()
    # Reshape to Matrix
    print(f"{Colors.TEST}Testing Reshape to Matrix{Colors.END}", end="\n---\n")
    matrix = v1.to_matrix(1, 2)
    print(f"v1 reshaped to matrix (1x2):\n{Colors.GREEN}{matrix}{Colors.END}")

# MATRIX TESTS
def matrix_validation():
    print(f"\n{Colors.HEADER}--- MATRIX VALIDATION ---{Colors.END}\n")
    # Creation
    print("Creating matrices m1 and m2...")
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[7, 4], [-2, 2]])
    print(f"Matrix m1 with shape {Colors.CORRECT}{m1.shape()}{Colors.END}:\n{Colors.GREEN}{m1}{Colors.END}")
    print(f"Matrix m2 with shape {Colors.CORRECT}{m2.shape()}{Colors.END}:\n{Colors.GREEN}{m2}{Colors.END}")
    print()
    # Addition
    print(f"{Colors.TEST}Testing Addition{Colors.END}", end="\n---\n")
    m_sum = m1 + m2
    print(f"m1 + m2 =\n{Colors.GREEN}{m_sum}{Colors.END}")
    print()
    # Subtraction
    print(f"{Colors.TEST}Testing Subtraction{Colors.END}", end="\n---\n")
    m_diff = m1 - m2
    print(f"m1 - m2 =\n{Colors.GREEN}{m_diff}{Colors.END}")
    print()
    # Scaling
    print(f"{Colors.TEST}Testing Scaling{Colors.END}", end="\n---\n")
    scalar = 3
    m_scaled = m1.scl(scalar)
    print(f"m1 scaled by {scalar}:\n{Colors.GREEN}{m_scaled}{Colors.END}")
    print()
    # Check if square
    print(f"{Colors.TEST}Checking if m1 is square{Colors.END}", end="\n---\n")
    print(f"Is m1 square? {Colors.GREEN}{m1.is_square()}{Colors.END}")
    print()
    # Convert to Vector
    print(f"{Colors.TEST}Testing Conversion to Vector{Colors.END}", end="\n---\n")
    v_from_m = m1.to_vector()
    print(f"m1 converted to vector: {Colors.GREEN}{v_from_m}{Colors.END}")

def complex_vector_validation():
    print(f"\n{Colors.HEADER}--- COMPLEX VECTOR VALIDATION ---{Colors.END}\n")
    # Creation
    print("Creating complex vectors vc1 and vc2...")
    vc1 = Vector([2+3j, -1j])
    vc2 = Vector([1-2j, 4])
    print(f"Vector vc1 with size {Colors.CORRECT}{vc1.size()}{Colors.END}: {Colors.GREEN}{vc1}{Colors.END}")
    print(f"Vector vc2 with size {Colors.CORRECT}{vc2.size()}{Colors.END}: {Colors.GREEN}{vc2}{Colors.END}")
    print()
    # Addition
    print(f"{Colors.TEST}Testing Addition (complex){Colors.END}", end="\n---\n")
    v_sum = vc1 + vc2
    print(f"vc1 + vc2 = {Colors.GREEN}{v_sum}{Colors.END}")
    print()
    # Subtraction
    print(f"{Colors.TEST}Testing Subtraction (complex){Colors.END}", end="\n---\n")
    v_diff = vc1 - vc2
    print(f"vc1 - vc2 = {Colors.GREEN}{v_diff}{Colors.END}")
    print()
    # Scaling
    print(f"{Colors.TEST}Testing Scaling (complex){Colors.END}", end="\n---\n")
    scalar = 1+2j
    v_scaled = vc1.scl(scalar)
    print(f"vc1 scaled by {scalar}: {Colors.GREEN}{v_scaled}{Colors.END}")
    print()
    # Reshape to Matrix
    print(f"{Colors.TEST}Testing Reshape to Matrix (complex){Colors.END}", end="\n---\n")
    matrix = vc1.to_matrix(1, 2)
    print(f"vc1 reshaped to matrix (1x2):\n{Colors.GREEN}{matrix}{Colors.END}")

def complex_matrix_validation():
    print(f"\n{Colors.HEADER}--- COMPLEX MATRIX VALIDATION ---{Colors.END}\n")
    # Creation
    print("Creating complex matrices mc1 and mc2...")
    mc1 = Matrix([[1+2j, 2], [3, -1j]])
    mc2 = Matrix([[0, 1j], [2-2j, -1]])
    print(f"Matrix mc1 with shape {Colors.CORRECT}{mc1.shape()}{Colors.END}:\n{Colors.GREEN}{mc1}{Colors.END}")
    print(f"Matrix mc2 with shape {Colors.CORRECT}{mc2.shape()}{Colors.END}:\n{Colors.GREEN}{mc2}{Colors.END}")
    print()
    # Addition
    print(f"{Colors.TEST}Testing Addition (complex){Colors.END}", end="\n---\n")
    m_sum = mc1 + mc2
    print(f"mc1 + mc2 =\n{Colors.GREEN}{m_sum}{Colors.END}")
    print()
    # Subtraction
    print(f"{Colors.TEST}Testing Subtraction (complex){Colors.END}", end="\n---\n")
    m_diff = mc1 - mc2
    print(f"mc1 - mc2 =\n{Colors.GREEN}{m_diff}{Colors.END}")
    print()
    # Scaling
    print(f"{Colors.TEST}Testing Scaling (complex){Colors.END}", end="\n---\n")
    scalar = -1j
    m_scaled = mc1.scl(scalar)
    print(f"mc1 scaled by {scalar}:\n{Colors.GREEN}{m_scaled}{Colors.END}")
    print()
    # Check if square
    print(f"{Colors.TEST}Checking if mc1 is square (complex){Colors.END}", end="\n---\n")
    print(f"Is mc1 square? {Colors.GREEN}{mc1.is_square()}{Colors.END}")
    print()
    # Convert to Vector
    print(f"{Colors.TEST}Testing Conversion to Vector (complex){Colors.END}", end="\n---\n")
    v_from_m = mc1.to_vector()
    print(f"mc1 converted to vector: {Colors.GREEN}{v_from_m}{Colors.END}")


vector_validation()
matrix_validation()
complex_vector_validation()
complex_matrix_validation()