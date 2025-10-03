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
    print()

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

def test_complex_cos():
    print(f"\n{Colors.HEADER}--- COMPLEX VECTOR COSINE ANGLE TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing angle_cos for vectors [1+1j, 0] and [1, 0] {Colors.END}", end="\n---\n")
    v1 = Vector([1+1j, 0])
    v2 = Vector([1, 0])
    # inner = conj(1+1j)*1 = 1-1j
    # real(inner) = 1
    # norm(v1) = sqrt(|1+1j|^2) = sqrt(2), norm(v2)=1
    expected = 1 / (2**0.5)
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [i, 0] and [1, 0] {Colors.END}", end="\n---\n")
    v1 = Vector([1j, 0])
    v2 = Vector([1, 0])
    # inner = conj(i)*1 = -i, real(inner)=0
    expected = 0.0
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [1, i] and [1, -i] {Colors.END}", end="\n---\n")
    v1 = Vector([1, 1j])
    v2 = Vector([1, -1j])
    # inner = conj(1)*1 + conj(i)*(-i) = 1 + (-i)*( -i ) = 1 + (i^2) = 1 - 1 = 0
    expected = 0.0
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

    print(f"{Colors.TEST}Testing angle_cos for vectors [1+2j, 3] and [4, 5-1j] {Colors.END}", end="\n---\n")
    v1 = Vector([1+2j, 3])
    v2 = Vector([4, 5-1j])
    # inner = conj(1+2j)*4 + conj(3)*(5-1j) = (1-2j)*4 + 3*(5-1j) = 4-8j + 15-3j = 19-11j
    # real(inner)=19, norm(v1)=sqrt(|1+2j|^2+|3|^2)=sqrt(5+9)=sqrt(14), norm(v2)=sqrt(|4|^2+|5-1j|^2)=sqrt(16+26)=sqrt(42)
    expected = 19 / ((14**0.5) * (42**0.5))
    result = angle_cos(v1, v2)
    print_comparison("Cosine", expected, result)

test_cos()
test_complex_cos()