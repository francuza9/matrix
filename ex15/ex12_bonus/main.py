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

def test_matrix_inverse():
	print(f"\n{Colors.HEADER}--- MATRIX INVERSE TEST ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing inverse for matrix [[1, 0, 0], [0, 1, 0], [0, 0, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	expected = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

	print(f"{Colors.TEST}Testing inverse for matrix [[2, 0, 0], [0, 2, 0], [0, 0, 2]] {Colors.END}", end="\n---\n")
	m = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
	expected = Matrix([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

	print(f"{Colors.TEST}Testing inverse for matrix [[8, 5, -2], [4, 7, 20], [7, 6, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
	expected = Matrix([
		[0.649425287, 0.097701149, -0.655172414],
		[-0.781609195, -0.126436782, 0.965517241],
		[0.143678161, 0.074712644, -0.206896552]
	])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

def test_matrix_inverse_edge_cases():
    print(f"\n{Colors.HEADER}--- MATRIX INVERSE EDGE CASES ---{Colors.END}\n")

    print(f"{Colors.TEST}Testing inverse for matrix [[4, 7], [2, 6]] {Colors.END}", end="\n---\n")
    m = Matrix([[4, 7], [2, 6]])
    expected = Matrix([[0.6, -0.7], [-0.2, 0.4]])
    result = m.inverse()
    print_comparison("Inverse", expected, result)

    print(f"{Colors.TEST}Testing inverse for matrix [[3, 0, 2], [2, 0, -2], [0, 1, 1]] {Colors.END}", end="\n---\n")
    m = Matrix([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
    expected = Matrix([[0.2, 0.2, 0.0], [-0.2, 0.3, 1.0], [0.2, -0.3, 0.0]])
    result = m.inverse()
    print_comparison("Inverse", expected, result)

    print(f"{Colors.TEST}Testing inverse for diagonal matrix [[1, 0, 0, 0], [0, -2, 0, 0], [0, 0, 3, 0], [0, 0, 0, -0.5]] {Colors.END}", end="\n---\n")
    m = Matrix([[1, 0, 0, 0], [0, -2, 0, 0], [0, 0, 3, 0], [0, 0, 0, -0.5]])
    expected = Matrix([[1.0, 0.0, 0.0, 0.0], [0.0, -0.5, 0.0, 0.0], [0.0, 0.0, 1/3, 0.0], [0.0, 0.0, 0.0, -2.0]])
    result = m.inverse()
    print_comparison("Inverse", expected, result)

    print(f"{Colors.TEST}Testing inverse for float-heavy matrix [[1.5, -2.3], [3.7, 0.4]] {Colors.END}", end="\n---\n")
    m = Matrix([[1.5, -2.3], [3.7, 0.4]])
    expected = Matrix([[0.04390779363336992, 0.252469813391877], [-0.4061470911086718, 0.1646542261251372]])
    result = m.inverse()
    print_comparison("Inverse", expected, result)

    print(f"{Colors.TEST}Expecting ValueError for singular matrix [[1, 2], [2, 4]] {Colors.END}", end="\n---\n")
    print_exception("Inverse", ValueError, lambda: Matrix([[1, 2], [2, 4]]).inverse())

    print(f"{Colors.TEST}Expecting ValueError for non-square matrix [[1, 2, 3], [4, 5, 6]] {Colors.END}", end="\n---\n")
    print_exception("Inverse", ValueError, lambda: Matrix([[1, 2, 3], [4, 5, 6]]).inverse())

def test_complex_matrix_inverse():
	print(f"\n{Colors.HEADER}--- COMPLEX MATRIX INVERSE TEST ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing inverse for matrix [[1, 0], [0, 1j]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 0], [0, 1j]])
	expected = Matrix([[1, 0], [0, -1j]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

	print(f"{Colors.TEST}Testing inverse for matrix [[1+1j, 2], [3, 4]] {Colors.END}", end="\n---\n")
	m = Matrix([[1+1j, 2], [3, 4]])
	# determinant = (1+1j)*4 - 6 = -2+4j
	# inverse = (1/det) * [[4, -2], [-3, 1+1j]]
	det = (-2+4j)
	expected = Matrix([[4/det, -2/det], [-3/det, (1+1j)/det]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

	print(f"{Colors.TEST}Testing inverse for matrix [[2j, 0], [0, 2]] {Colors.END}", end="\n---\n")
	m = Matrix([[2j, 0], [0, 2]])
	expected = Matrix([[-0.5j, 0], [0, 0.5]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)


def test_complex_matrix_inverse_edge_cases():
	print(f"\n{Colors.HEADER}--- COMPLEX MATRIX INVERSE EDGE CASES ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing inverse for diagonal complex matrix [[1j, 0, 0], [0, -2, 0], [0, 0, 3+3j]] {Colors.END}", end="\n---\n")
	m = Matrix([[1j, 0, 0], [0, -2, 0], [0, 0, 3+3j]])
	expected = Matrix([[-1j, 0, 0], [0, -0.5, 0], [0, 0, 1/(3+3j)]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

	print(f"{Colors.TEST}Testing inverse for 1x1 complex matrix [[5j]] {Colors.END}", end="\n---\n")
	m = Matrix([[5j]])
	expected = Matrix([[-0.2j]])
	result = m.inverse()
	print_comparison("Inverse", expected, result)

	print(f"{Colors.TEST}Expecting ValueError for singular complex matrix [[1j, 2], [2j, 4]] {Colors.END}", end="\n---\n")
	print_exception("Inverse", ValueError, lambda: Matrix([[1j, 2], [2j, 4]]).inverse())

	print(f"{Colors.TEST}Expecting ValueError for non-square complex matrix [[1j, 2, 3], [4, 5, 6]] {Colors.END}", end="\n---\n")
	print_exception("Inverse", ValueError, lambda: Matrix([[1j, 2, 3], [4, 5, 6]]).inverse())

test_matrix_inverse()
test_matrix_inverse_edge_cases()
test_complex_matrix_inverse()
test_complex_matrix_inverse_edge_cases()