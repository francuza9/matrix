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

test_norms()