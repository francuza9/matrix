from Vector import Vector
from angles import angle_cos

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
    is_correct = abs(result - expected) < tolerance
    status = f"{Colors.CORRECT}(Correct){Colors.END}" if is_correct else f"{Colors.RED}(Incorrect){Colors.END}"
    print(f"{'Expected ' + label + ':':<25} {Colors.EXPECTED}{expected}{Colors.END}")
    if is_correct:
        print(f"{'Result:':<25} {Colors.GREEN}{result}{Colors.END} {status}")
    else:
        print(f"{'Result:':<25} {Colors.RED}{result}{Colors.END} {status}")

def test_cos():
    print(f"\n{Colors.HEADER}--- VECTOR COSINE ANGLE TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing angle_cos for vectors [1, 0] and [1, 0] {Colors.END}", end="\n---\n")
    v1 = Vector([1, 0])
    v2 = Vector([1, 0])
    expected = 1.0
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [1, 0] and [0, 1] {Colors.END}", end="\n---\n")
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    expected = 0.0
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [-1, 1] and [1, -1] {Colors.END}", end="\n---\n")
    v1 = Vector([-1, 1])
    v2 = Vector([1, -1])
    expected = -1.0
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [2, 1] and [4, 2] {Colors.END}", end="\n---\n")
    v1 = Vector([2, 1])
    v2 = Vector([4, 2])
    expected = 1
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [1, 2, 3] and [4, 5, 6] {Colors.END}", end="\n---\n")
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    expected = 0.9746318461970762
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

test_cos()