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

def test_transpose():
    print(f"\n{Colors.HEADER}--- MATRIX TRANSPOSE TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing transpose for matrix [[1, 2, 3], [4, 5, 6]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    expected = Matrix([[1, 4], [2, 5], [3, 6]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1]] {Colors.END}", end="\n---\n")
    m = Matrix([[1]])
    expected = Matrix([[1]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1, 2], [3, 4], [5, 6]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 2], [3, 4], [5, 6]])
    expected = Matrix([[1, 3, 5], [2, 4, 6]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1, 2, 3, 4]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 2, 3, 4]])
    expected = Matrix([[1], [2], [3], [4]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1], [2], [3], [4]] {Colors.END}", end="\n---\n")
    m = Matrix([[1], [2], [3], [4]])
    expected = Matrix([[1, 2, 3, 4]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [] {Colors.END}", end="\n---\n")
    m = Matrix([[]])
    expected = Matrix([[]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

def test_complex_transpose():
    print(f"\n{Colors.HEADER}--- COMPLEX MATRIX TRANSPOSE TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing transpose for matrix [[1+1j, 2], [3, 4]] {Colors.END}", end="\n---\n")
    m = Matrix([[1+1j, 2], [3, 4]])
    expected = Matrix([[1+1j, 3], [2, 4]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1, 2j, 3], [4, 5, 6j]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 2j, 3], [4, 5, 6j]])
    expected = Matrix([[1, 4], [2j, 5], [3, 6j]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1j]] {Colors.END}", end="\n---\n")
    m = Matrix([[1j]])
    expected = Matrix([[1j]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1+2j, 3-4j]] {Colors.END}", end="\n---\n")
    m = Matrix([[1+2j, 3-4j]])
    expected = Matrix([[1+2j], [3-4j]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)

    print(f"{Colors.TEST}Testing transpose for matrix [[1j], [2j], [3j]] {Colors.END}", end="\n---\n")
    m = Matrix([[1j], [2j], [3j]])
    expected = Matrix([[1j, 2j, 3j]])
    result = m.transpose()
    print_comparison("Transpose", expected, result)


test_transpose()
test_complex_transpose()
