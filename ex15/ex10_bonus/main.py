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
	if isinstance(expected, (int, float, complex)) and isinstance(result, (int, float, complex)):
		diff = abs(result - expected)
		is_correct = diff < tolerance
	elif isinstance(expected, Vector) and isinstance(result, Vector):
		is_correct = expected == result
	elif isinstance(expected, Matrix) and isinstance(result, Matrix):
		is_correct = expected == result
	else:
		try:
			diff = abs(result - expected)
			is_correct = diff < tolerance
		except Exception:
			print(f"Error: Type mismatch between expected={type(expected)} and result={type(result)}")
			return

	status = f"{Colors.CORRECT}(Correct){Colors.END}" if is_correct else f"{Colors.RED}(Incorrect){Colors.END}"

	print(f"{'Expected ' + label + ':':<25} {Colors.EXPECTED}{expected}{Colors.END}")
	if is_correct:
		print(f"{'Result:':<25} {Colors.GREEN}{result}{Colors.END} {status}")
	else:
		print(f"{'Result:':<25} {Colors.RED}{result}{Colors.END} {status}")
	print()


def test_row_echelon():
	print(f"\n{Colors.HEADER}--- MATRIX ROW ECHELON FORM TEST ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing row echelon form for matrix [[1, 0, 0], [0, 1, 0], [0, 0, 1]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	expected = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	result = m.row_echelon()
	print_comparison("Row Echelon", expected, result)

	print(f"{Colors.TEST}Testing row echelon form for matrix [[1, 2], [3, 4]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 2], [3, 4]])
	expected = Matrix([[1, 0], [0, 1]])
	result = m.row_echelon()
	print_comparison("Row Echelon", expected, result)

	print(f"{Colors.TEST}Testing row echelon form for matrix [[1, 2], [2, 4]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 2], [2, 4]])
	expected = Matrix([[1, 2], [0, 0]])
	result = m.row_echelon()
	print_comparison("Row Echelon", expected, result)

	print(f"{Colors.TEST}Testing row echelon form for matrix [[8, 5, -2, 4, 28], [4, 2.5, 20, 4, -4], [8, 5, 1, 4, 17]] {Colors.END}", end="\n---\n")
	m = Matrix([[8, 5, -2, 4, 28], [4, 2.5, 20, 4, -4], [8, 5, 1, 4, 17]])
	expected = Matrix([[1, 0.625, 0, 0, -12.1666667], [0, 0, 1, 0, -3.6666667], [0, 0, 0, 1, 29.5]])
	result = m.row_echelon()
	print_comparison("Row Echelon", expected, result)

def test_row_echelon_edge_cases():
	print(f"\n{Colors.HEADER}--- MATRIX ROW ECHELON EDGE CASE TESTS ---{Colors.END}\n")

	print(f"{Colors.TEST}Pivot requires row swap {Colors.END}", end="\n---\n")
	m = Matrix([[0, 0, 1], [1, 2, 3]])
	expected = Matrix([[1, 2, 0], [0, 0, 1]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Matrix with zero leading row {Colors.END}", end="\n---\n")
	m = Matrix([[0, 2, 4], [0, 2, 4]])
	expected = Matrix([[0, 1, 2], [0, 0, 0]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Tall matrix (more rows than pivots) {Colors.END}", end="\n---\n")
	m = Matrix([[1, -1, 2, 0],
				[2, -2, 4, 1],
				[-1, 1, -2, 3]])
	expected = Matrix([[1, -1, 2, 0],
					[0,  0, 0,  1],
					[0,  0, 0,  0]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Already reduced matrix stays stable {Colors.END}", end="\n---\n")
	m = Matrix([[1, 0, 2.5],
				[0, 1, -4.5],
				[0, 0, 0]])
	expected = Matrix([[1, 0, 2.5],
					[0, 1, -4.5],
					[0, 0, 0]])
	print_comparison("Row Echelon", expected, m.row_echelon())

def test_complex_row_echelon():
	print(f"\n{Colors.HEADER}--- COMPLEX MATRIX ROW ECHELON FORM TEST ---{Colors.END}\n")

	print(f"{Colors.TEST}Testing row echelon form for matrix [[1+1j, 2], [3, 4]] {Colors.END}", end="\n---\n")
	m = Matrix([[1+1j, 2], [3, 4]])
	expected = Matrix([[1, 0], [0, 1]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Testing row echelon form for matrix [[1, 2j], [3j, 4]] {Colors.END}", end="\n---\n")
	m = Matrix([[1, 2j], [3j, 4]])
	expected = Matrix([[1, 0], [0, 1]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Testing row echelon form for matrix [[0, 1j, 2], [1, 2, 3]] {Colors.END}", end="\n---\n")
	m = Matrix([[0, 1j, 2], [1, 2, 3]])
	expected = Matrix([[1, 0, 3+4j],
					[0, 1, -2j]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Testing row echelon form for matrix [[1+2j, 3-4j], [2, 4]] {Colors.END}", end="\n---\n")
	m = Matrix([[1+2j, 3-4j], [2, 4]])
	expected = Matrix([[1, 0], [0, 1]])
	print_comparison("Row Echelon", expected, m.row_echelon())


def test_complex_row_echelon_edge_cases():
	print(f"\n{Colors.HEADER}--- COMPLEX MATRIX ROW ECHELON EDGE CASE TESTS ---{Colors.END}\n")

	print(f"{Colors.TEST}Pivot requires row swap {Colors.END}", end="\n---\n")
	m = Matrix([[0, 0, 1j], [1+1j, 2, 3]])
	expected = Matrix([[1, (1-1j), 0],
					[0, 0, 1]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Matrix with zero leading row {Colors.END}", end="\n---\n")
	m = Matrix([[0, 2j, 4], [0, 2j, 4]])
	expected = Matrix([[0, 1, -2j],
					[0, 0, 0]])
	print_comparison("Row Echelon", expected, m.row_echelon())

	print(f"{Colors.TEST}Tall matrix with complex coefficients {Colors.END}", end="\n---\n")
	m = Matrix([[1j, -1, 2, 0],
				[2, -2, 4, 1j],
				[-1, 1j, -2, 3]])
	expected = Matrix([[1, 0, 0, (-0.25+0.25j)],
					[0, 1, 0, (-1.25-1.75j)],
					[0, 0, 1, (-0.5-0.75j)]])
	print_comparison("Row Echelon", expected, m.row_echelon())



test_row_echelon()
test_row_echelon_edge_cases()
test_complex_row_echelon()
test_complex_row_echelon_edge_cases()