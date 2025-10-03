from Vector import Vector
from Matrix import Matrix

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = BOLD + BLUE + UNDERLINE
    TEST = BLUE + BOLD
    CORRECT = GREEN
    EXPECTED = BOLD + UNDERLINE
    END = '\033[0m'

def print_comparison(label, expected, result, tolerance=1e-9):  
    if type(expected) != type(result):
        print(f"Error: Type mismatch between expected and result. {type(expected)} and {type(result)}")
        return

    if isinstance(expected, Vector) and isinstance(result, Vector):
        is_correct = expected == result
    elif isinstance(expected, Matrix) and isinstance(result, Matrix):
        is_correct = expected == result
    else:
        is_correct = abs(result - expected) < tolerance
    
    status = f"{Colors.CORRECT}(Correct){Colors.END}" if is_correct else f"{Colors.RED}(Incorrect){Colors.END}"
    print(f"{'Expected ' + label + ':':<25} {Colors.EXPECTED}{expected}{Colors.END}")
    if is_correct:
        print(f"{'Result:':<25} {Colors.GREEN}{result}{Colors.END} {status}")
    else:
        print(f"{'Result:':<25} {Colors.RED}{result}{Colors.END} {status}")
    print()

def test_matrix_vector_multiplication():
    print(f"\n{Colors.HEADER}--- MATRIX-VECTOR MULTIPLICATION TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing multiplications of matrices with vectors{Colors.END}", end="\n---\n")
    print("matrix [[1, 0], [0, 1]] * vector [4, 2]", end="\n---\n")
    m = Matrix([[1, 0], [0, 1]])
    v = Vector([4, 2])
    expected = Vector([4, 2])
    result = m.mul_vec(v)
    print_comparison("Matrix-Vector Product", expected, result)

    print(f"Testing matrix[[2, 0], [0, 2]] * vector [4, 2]", end="\n---\n")
    m = Matrix([[2, 0], [0, 2]])
    v = Vector([4, 2])
    expected = Vector([8, 4])
    result = m.mul_vec(v)
    print_comparison("Matrix-Vector Product", expected, result)

    print(f"Testing matrix[[2, -2], [-2, 2]] * vector [4, 2]", end="\n---\n")
    m = Matrix([[2, -2], [-2, 2]])
    v = Vector([4, 2])
    expected = Vector([4, -4])
    result = m.mul_vec(v)
    print_comparison("Matrix-Vector Product", expected, result)

    print(f"{Colors.TEST}Testing multiplications of matrices with matrices{Colors.END}", end="\n---\n")
    print("matrix [[1, 0], [0, 1]] * matrix [[1, 0], [0, 1]]", end="\n---\n")
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[1, 0], [0, 1]])
    expected = Matrix([[1, 0], [0, 1]])
    result = m1.mul_mat(m2)
    print_comparison("Matrix-Matrix Product", expected, result)

    print(f"Testing matrix [[1, 0], [0, 1]] * matrix [[2, 1], [4, 2]]", end="\n---\n")
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[2, 1], [4, 2]])
    expected = Matrix([[2, 1], [4, 2]])
    result = m1.mul_mat(m2)
    print_comparison("Matrix-Matrix Product", expected, result)

    print(f"Testing matrix [[3, -5], [6, 8]] * matrix [[2, 1], [4, 2]]", end="\n---\n")
    m1 = Matrix([[3, -5], [6, 8]])
    m2 = Matrix([[2, 1], [4, 2]])
    expected = Matrix([[-14, -7], [44, 22]])
    result = m1.mul_mat(m2)
    print_comparison("Matrix-Matrix Product", expected, result)

def test_complex_matrix_vector_multiplication():
    print(f"\n{Colors.HEADER}--- COMPLEX MATRIX-VECTOR MULTIPLICATION TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing multiplications of complex matrices with vectors{Colors.END}", end="\n---\n")
    print("matrix [[1, 0], [0, 1]] * vector [1+1j, 2]", end="\n---\n")
    m = Matrix([[1, 0], [0, 1]])
    v = Vector([1+1j, 2])
    expected = Vector([1+1j, 2])
    result = m.mul_vec(v)
    print_comparison("Matrix-Vector Product", expected, result)

    print("matrix [[2j, 0], [0, 1]] * vector [1, 3]", end="\n---\n")
    m = Matrix([[2j, 0], [0, 1]])
    v = Vector([1, 3])
    expected = Vector([2j, 3])
    result = m.mul_vec(v)
    print_comparison("Matrix-Vector Product", expected, result)

    print("matrix [[1, -1j], [1j, 1]] * vector [2, 3j]", end="\n---\n")
    m = Matrix([[1, -1j], [1j, 1]])
    v = Vector([2, 3j])
    expected = Vector([2+3, 2j+3j])
    result = m.mul_vec(v)
    print_comparison("Matrix-Vector Product", expected, result)

    print(f"{Colors.TEST}Testing multiplications of complex matrices with matrices{Colors.END}", end="\n---\n")
    print("matrix [[1, 0], [0, 1]] * matrix [[1j, 0], [0, 1]]", end="\n---\n")
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[1j, 0], [0, 1]])
    expected = Matrix([[1j, 0], [0, 1]])
    result = m1.mul_mat(m2)
    print_comparison("Matrix-Matrix Product", expected, result)

    print("matrix [[1, 1j], [0, 1]] * matrix [[1, 0], [0, 1j]]", end="\n---\n")
    m1 = Matrix([[1, 1j], [0, 1]])
    m2 = Matrix([[1, 0], [0, 1j]])
    expected = Matrix([[1, 1j*1j], [0, 1j]])
    result = m1.mul_mat(m2)
    print_comparison("Matrix-Matrix Product", expected, result)

    print("matrix [[1+1j, 2], [3, 4-1j]] * matrix [[0, 1], [1, 0]]", end="\n---\n")
    m1 = Matrix([[1+1j, 2], [3, 4-1j]])
    m2 = Matrix([[0, 1], [1, 0]])
    expected = Matrix([[2, 1+1j], [4-1j, 3]])
    result = m1.mul_mat(m2)
    print_comparison("Matrix-Matrix Product", expected, result)


test_matrix_vector_multiplication()
test_complex_matrix_vector_multiplication()