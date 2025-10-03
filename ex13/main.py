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

def print_exception(label, expected_exception, func):
	expected_name = expected_exception.__name__
	try:
		func()
	except Exception as err:
		is_correct = isinstance(err, expected_exception)
		status = f"{Colors.CORRECT}(Correct){Colors.END}" if is_correct else f"{Colors.RED}(Incorrect){Colors.END}"
		print(f"{'Expected ' + label + ':':<25} {Colors.EXPECTED}{expected_name}{Colors.END}")
		color = Colors.GREEN if is_correct else Colors.RED
		print(f"{'Result:':<25} {color}{type(err).__name__}: {err}{Colors.END} {status}")
	else:
		status = f"{Colors.RED}(Incorrect){Colors.END}"
		print(f"{'Expected ' + label + ':':<25} {Colors.EXPECTED}{expected_name}{Colors.END}")
		print(f"{'Result:':<25} {Colors.RED}No exception raised{Colors.END} {status}")
	print()

def test_matrix_rank():
	print(f"\n{Colors.HEADER}--- MATRIX RANK TEST ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing rank for matrix [[1, 0, 0], [0, 1, 0], [0, 0, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	expected = 3
	result = m.rank()
	print_comparison("Rank", expected, result)

	print(f"{Colors.TEST}Testing rank for matrix [[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]])
	expected = 2
	result = m.rank()
	print_comparison("Rank", expected, result)

	print(f"{Colors.TEST}Testing rank for matrix [[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]] {Colors.END}", end="\n---\n")
	m = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]])
	expected = 3
	result = m.rank()
	print_comparison("Rank", expected, result)

def test_matrix_rank_edge_cases():
    print(f"\n{Colors.HEADER}--- MATRIX RANK EDGE CASES ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing rank for zero matrix [[0, 0, 0], [0, 0, 0], [0, 0, 0]] {Colors.END}", end="\n---\n")
    m = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    expected = 0
    result = m.rank()
    print_comparison("Rank", expected, result)

    print(f"{Colors.TEST}Testing rank for rectangular matrix [[1, 2, 3], [4, 5, 6]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    expected = 2
    result = m.rank()
    print_comparison("Rank", expected, result)

    print(f"{Colors.TEST}Testing rank for tall matrix [[1, 2], [2, 4], [3, 6]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 2], [2, 4], [3, 6]])
    expected = 1
    result = m.rank()
    print_comparison("Rank", expected, result)

    print(f"{Colors.TEST}Testing rank for full-rank matrix [[2, -1, 0], [0, 3, 1], [4, 5, -2]] {Colors.END}", end="\n---\n")
    m = Matrix([[2, -1, 0], [0, 3, 1], [4, 5, -2]])
    expected = 3
    result = m.rank()
    print_comparison("Rank", expected, result)

    print(f"{Colors.TEST}Testing rank for matrix with float dependencies [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [1.0, 2.5, 3.0]] {Colors.END}", end="\n---\n")
    m = Matrix([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [1.0, 2.5, 3.0]])
    expected = 2
    result = m.rank()
    print_comparison("Rank", expected, result)

    print(f"{Colors.TEST}Expecting ValueError for ragged matrix [[1, 2], [3]] {Colors.END}", end="\n---\n")
    print_exception("Rank", ValueError, lambda: Matrix([[1, 2], [3]]))


test_matrix_rank()
test_matrix_rank_edge_cases()