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
    EXPECTED = BOLD + UNDERLINE
    END = '\033[0m'

def dot_product_test():
    print(f"\n{Colors.HEADER}--- DOT PRODUCT TEST ---{Colors.END}\n")
    
    print(f"{Colors.TEST}Testing with vectors [0, 0] and [1, 1] {Colors.END}", end="\n---\n")
    print(f"Expected: {Colors.EXPECTED}0{Colors.END}")
    v1 = Vector([0, 0])
    v2 = Vector([1, 1])
    result = v1.dot(v2)
    if abs(result - 0) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    
    print(f"{Colors.TEST}Testing with vectors [1, 1] and [1, 1] {Colors.END}", end="\n---\n")
    print(f"Expected: {Colors.EXPECTED}2{Colors.END}")
    v1 = Vector([1, 1])
    v2 = Vector([1, 1])
    result = v1.dot(v2)
    if abs(result - 2) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    
    print(f"{Colors.TEST}Testing with vectors [-1, 6] and [3, 2] {Colors.END}", end="\n---\n")
    print(f"Expected: {Colors.EXPECTED}9{Colors.END}")
    v1 = Vector([-1, 6])
    v2 = Vector([3, 2])
    result = v1.dot(v2)
    if abs(result - 9) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")
    
    print(f"{Colors.TEST}Testing with vectors [2, 3, 4] and [5, 6, 7] {Colors.END}", end="\n---\n")
    print(f"Expected: {Colors.EXPECTED}56{Colors.END}")
    v1 = Vector([2, 3, 4])
    v2 = Vector([5, 6, 7])
    result = v1.dot(v2)
    if abs(result - 56) < 1e-9:
        print(f"Result: {Colors.CORRECT}{result} (Correct){Colors.END}\n")
    else:
        print(f"Result: {Colors.RED}{result} (Incorrect){Colors.END}\n")

dot_product_test()