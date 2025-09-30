from linear_operations import lerp
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

def test_lerp():
    print(f"\n{Colors.HEADER}--- LINEAR INTERPOLATION TESTS ---{Colors.END}\n")
    # Test with scalars
    print(f"{Colors.TEST}Testing Lerp with Scalars{Colors.END}", end="\n---\n")
    # 1
    print(f"lerp(0, 1, 0) expected: {Colors.EXPECTED}0{Colors.END}")
    result = lerp(0, 1, 0)
    if abs(result - 0) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    # 2
    print(f"lerp(0, 1, 1) expected: {Colors.EXPECTED}1{Colors.END}")
    result = lerp(0, 1, 1)
    if abs(result - 1) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    # 3
    print(f"lerp(0, 1, 0.5) expected: {Colors.EXPECTED}0.5{Colors.END}")
    result = lerp(0, 1, 0.5)
    if abs(result - 0.5) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    # 4
    print(f"lerp(21, 42, 0.3) expected: {Colors.EXPECTED}27.3{Colors.END}")
    result = lerp(21, 42, 0.3)
    if abs(result - 27.3) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    print()
    
    # Test with Vectors
    print(f"{Colors.TEST}Testing Lerp with Vectors{Colors.END}", end="\n---\n")
    v1 = Vector([2, 1])
    v2 = Vector([4, 2])
    print(f"lerp({v1}, {v2}, 0.3) expected: {Colors.EXPECTED}Vector([2.6, 1.3]){Colors.END}")
    result = lerp(v1, v2, 0.3)
    if result == Vector([2.6, 1.3]):
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    
    # Test with Matrices
    print(f"{Colors.TEST}Testing Lerp with Matrices{Colors.END}", end="\n---\n")
    m1 = Matrix([[2, 1], [3, 4]])
    m2 = Matrix([[20, 10], [30, 40]])
    print(f"lerp({m1}, {m2}, 0.5) expected: {Colors.EXPECTED}Matrix([[11.0, 5.5], [16.5, 22.0]]){Colors.END}")
    result = lerp(m1, m2, 0.5)
    if result == Matrix([[11.0, 5.5], [16.5, 22.0]]):
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")

test_lerp()