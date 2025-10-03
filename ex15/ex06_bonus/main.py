from Vector import Vector
from cross_product import cross_product

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
    if isinstance(expected, Vector) and isinstance(result, Vector):
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

def test_cross_product():
    print(f"\n{Colors.HEADER}--- CROSS PRODUCT TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing cross product for vectors [0, 0, 1] and [1, 0, 0] {Colors.END}", end="\n---\n")
    v1 = Vector([0, 0, 1])
    v2 = Vector([1, 0, 0])
    expected = Vector([0, 1, 0])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

    print(f"{Colors.TEST}Testing cross product for vectors [1, 2, 3] and [4, 5, 6] {Colors.END}", end="\n---\n")
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    expected = Vector([-3, 6, -3])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

    print(f"{Colors.TEST}Testing cross product for vectors [4, 2, -3] and [-2, -5, 16] {Colors.END}", end="\n---\n")
    v1 = Vector([4, 2, -3])
    v2 = Vector([-2, -5, 16])
    expected = Vector([17, -58, -16])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

def test_complex_cross_product():
    print(f"\n{Colors.HEADER}--- COMPLEX CROSS PRODUCT TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing cross product for vectors [1j, 0, 0] and [0, 1, 0] {Colors.END}", end="\n---\n")
    v1 = Vector([1j, 0, 0])
    v2 = Vector([0, 1, 0])
    expected = Vector([0, 0, 1j])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

    print(f"{Colors.TEST}Testing cross product for vectors [1+1j, 0, 0] and [0, 1, 0] {Colors.END}", end="\n---\n")
    v1 = Vector([1+1j, 0, 0])
    v2 = Vector([0, 1, 0])
    expected = Vector([0, 0, 1+1j])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

    print(f"{Colors.TEST}Testing cross product for vectors [1, 2j, 3] and [4, 5, 6j] {Colors.END}", end="\n---\n")
    v1 = Vector([1, 2j, 3])
    v2 = Vector([4, 5, 6j])
    expected = Vector([-27, 12-6j, 5-8j])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

    print(f"{Colors.TEST}Testing cross product for vectors [1+2j, 3, 4] and [0, -1j, 2] {Colors.END}", end="\n---\n")
    v1 = Vector([1+2j, 3, 4])
    v2 = Vector([0, -1j, 2])
    expected = Vector([6+4j, -2-4j, 2-1j])
    result = cross_product(v1, v2)
    print_comparison("Cross Product", expected, result)

test_cross_product()
test_complex_cross_product()