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

def print_comparison(label, expected, result, tolerance=1e-9):
    is_correct = abs(result - expected) < tolerance
    status = f"{Colors.CORRECT}(Correct){Colors.END}" if is_correct else f"{Colors.RED}(Incorrect){Colors.END}"
    print(f"{'Expected ' + label + ':':<25} {Colors.EXPECTED}{expected}{Colors.END}")
    print(f"{'Result:':<25} {Colors.GREEN}{result}{Colors.END} {status}")
    print()

def test_norms():
    print(f"\n{Colors.HEADER}--- VECTOR NORMS TEST ---{Colors.END}\n")
    
    print(f"{Colors.TEST}Testing norms for vector [0, 0, 0] {Colors.END}", end="\n---\n")
    u = Vector([0, 0, 0])
    result_1 = u.norm_1()
    result_2 = u.norm()
    result_inf = u.norm_inf()
    print_comparison("1-norm", 0, result_1)
    print_comparison("2-norm", 0, result_2)
    print_comparison("inf-norm", 0, result_inf)
    
    print(f"{Colors.TEST}Testing norms for vector [1, 2, 3] {Colors.END}", end="\n---\n")
    u = Vector([1, 2, 3])
    result_1 = u.norm_1()
    result_2 = u.norm()
    result_inf = u.norm_inf()
    print_comparison("1-norm", 6, result_1)
    print_comparison("2-norm", 3.7416573867739413, result_2)
    print_comparison("inf-norm", 3, result_inf)

    print(f"{Colors.TEST}Testing norms for vector [-1, -2] {Colors.END}", end="\n---\n")
    u = Vector([-1, -2])
    result_1 = u.norm_1()
    result_2 = u.norm()
    result_inf = u.norm_inf()
    print_comparison("1-norm", 3, result_1)
    print_comparison("2-norm", 2.23606797749979, result_2)
    print_comparison("inf-norm", 2, result_inf)

def test_complex_norms():
    print(f"\n{Colors.HEADER}--- COMPLEX VECTOR NORMS TEST ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing norms for vector [0+0j, 0] {Colors.END}", end="\n---\n")
    u = Vector([0+0j, 0])
    result_1 = u.norm_1()
    result_2 = u.norm()
    result_inf = u.norm_inf()
    print_comparison("1-norm", 0, result_1)
    print_comparison("2-norm", 0, result_2)
    print_comparison("inf-norm", 0, result_inf)

    print(f"{Colors.TEST}Testing norms for vector [3+4j, 0] {Colors.END}", end="\n---\n")
    u = Vector([3+4j, 0])
    # |3+4j| = 5
    result_1 = u.norm_1()
    result_2 = u.norm()
    result_inf = u.norm_inf()
    print_comparison("1-norm", 5, result_1)
    print_comparison("2-norm", 5, result_2)
    print_comparison("inf-norm", 5, result_inf)

    print(f"{Colors.TEST}Testing norms for vector [1+1j, -1j, 2] {Colors.END}", end="\n---\n")
    u = Vector([1+1j, -1j, 2])
    # Magnitudes: |1+1j| = sqrt(2) ≈ 1.4142, |-1j| = 1, |2| = 2
    # 1-norm = sqrt(2) + 1 + 2
    expected_1 = (2 ** 0.5) + 1 + 2
    # 2-norm = sqrt((sqrt(2))^2 + 1^2 + 2^2) = sqrt(2 + 1 + 4) = sqrt(7)
    expected_2 = 7 ** 0.5
    # inf-norm = max(sqrt(2), 1, 2) = 2
    expected_inf = 2
    result_1 = u.norm_1()
    result_2 = u.norm()
    result_inf = u.norm_inf()
    print_comparison("1-norm", expected_1, result_1)
    print_comparison("2-norm", expected_2, result_2)
    print_comparison("inf-norm", expected_inf, result_inf)


test_norms()
test_complex_norms()