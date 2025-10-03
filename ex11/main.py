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

def test_matrix_determinant():
	print(f"\n{Colors.HEADER}--- MATRIX DETERMINANT TEST ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing determinant for matrix [[1, -1], [-1, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, -1], [-1, 1]])
	expected = 0
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Testing determinant for matrix [[2, 0, 0], [0, 2, 0], [0, 0, 2]] {Colors.END}", end="\n---\n")
	m = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
	expected = 8
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Testing determinant for matrix [[8, 5, -2], [4, 7, 20], [7, 6, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
	expected = -174
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Testing determinant for matrix [[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])
	expected = 1032
	result = m.determinant()
	print_comparison("Determinant", expected, result)

def test_matrix_determinant_edge_cases():
	print(f"\n{Colors.HEADER}--- MATRIX DETERMINANT EDGE CASES ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing determinant for 1x1 matrix [[42]] {Colors.END}", end="\n---\n")
	m = Matrix([[42]])
	expected = 42
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Testing determinant for matrix with duplicate rows [[1, 2, 3], [1, 2, 3], [4, 5, 6]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 2, 3], [1, 2, 3], [4, 5, 6]])
	expected = 0
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Testing determinant for upper-triangular 4x4 matrix {Colors.END}", end="\n---\n")
	m = Matrix([[1, 2, -3, 4], [0, -2, 5, -1], [0, 0, 3, 7], [0, 0, 0, 0.5]])
	expected = -3
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Testing determinant for float-heavy matrix [[1.5, 2.5, -3.5], [0.0, -1.2, 4.8], [2.1, 0.0, 3.3]] {Colors.END}", end="\n---\n")
	m = Matrix([[1.5, 2.5, -3.5], [0.0, -1.2, 4.8], [2.1, 0.0, 3.3]])
	expected = 10.44
	result = m.determinant()
	print_comparison("Determinant", expected, result)

	print(f"{Colors.TEST}Expecting ValueError for non-square matrix [[1, 2, 3], [4, 5, 6]] {Colors.END}", end="\n---\n")
	print_exception("Determinant", ValueError, lambda: Matrix([[1, 2, 3], [4, 5, 6]]).determinant())

	print(f"{Colors.TEST}Expecting NotImplementedError for 5x5 matrix {Colors.END}", end="\n---\n")
	print_exception("Determinant", NotImplementedError, lambda: Matrix([[1, 0, 0, 0, 0],
																	[0, 1, 0, 0, 0],
																	[0, 0, 1, 0, 0],
																	[0, 0, 0, 1, 0],
																	[0, 0, 0, 0, 1]]).determinant())

test_matrix_determinant()
test_matrix_determinant_edge_cases()