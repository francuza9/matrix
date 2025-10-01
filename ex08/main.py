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

def test_trace():
    print(f"\n{Colors.HEADER}--- MATRIX TRACE TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing trace for matrix [[1, 0], [0, 1]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 0], [0, 1]])
    expected = 2.0
    result = m.trace()
    print_comparison("Trace", expected, result)

    print(f"{Colors.TEST}Testing trace for matrix [[2, -5, 0], [4, 3, 7], [-2, 3, 4]] {Colors.END}", end="\n---\n")
    m = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    expected = 9.0
    result = m.trace()
    print_comparison("Trace", expected, result)

    print(f"{Colors.TEST}Testing trace for matrix [[-2, -8, 4], [1, -23, 4], [0, 6, 4]] {Colors.END}", end="\n---\n")
    m = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    expected = -21.0
    result = m.trace()
    print_comparison("Trace", expected, result)

test_trace()