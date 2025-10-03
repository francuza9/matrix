from linear_operations import linear_combination
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

def test_linear_combination():
	print("\n{Colors.HEADER}--- LINEAR COMBINATION TESTS ---{Colors.END}\n")
	# Define basis vectors and other vectors
	print("Defining basis vectors e1, e2, e3 and vectors v1, v2...")
	e1 = Vector([1, 0, 0])
	e2 = Vector([0, 1, 0])
	e3 = Vector([0, 0, 1])

	v1 = Vector([1, 2, 3])
	v2 = Vector([0, 10, -100])
	print(f"Basis vector e1: {Colors.GREEN}{e1}{Colors.END}")
	print(f"Basis vector e2: {Colors.GREEN}{e2}{Colors.END}")
	print(f"Basis vector e3: {Colors.GREEN}{e3}{Colors.END}")
	print(f"Vector v1: {Colors.GREEN}{v1}{Colors.END}")
	print(f"Vector v2: {Colors.GREEN}{v2}{Colors.END}")
	print()
	# Test linear combinations
	print(f"{Colors.TEST}Testing Linear Combinations 1{Colors.END}", end="\n---\n")
	result1 = linear_combination([e1, e2, e3], [10, -2, 0.5])
	expected1 = Vector([10, -2, 0.5])
	print(f"Linear combination Expected: {Colors.EXPECTED}{expected1}{Colors.END}")
	if result1 == expected1:
		print(f"Result: {Colors.CORRECT}{result1} (Correct){Colors.END}")
	else:
		print(f"Result: {Colors.RED}{result1} (Incorrect){Colors.END}")
	print()
	print(f"{Colors.TEST}Testing Linear Combinations 2{Colors.END}", end="\n---\n")
	result2 = linear_combination([v1, v2], [10, -2])
	expected2 = Vector([10, 0, 230])
	print(f"Linear combination Expected: {Colors.EXPECTED}{expected2}{Colors.END}")
	if result2 == expected2:
		print(f"Result: {Colors.CORRECT}{result2} (Correct){Colors.END}")
	else:
		print(f"Result: {Colors.RED}{result2} (Incorrect){Colors.END}")
	print()

def test_complex_linear_combination():
	print(f"\n{Colors.HEADER}--- COMPLEX LINEAR COMBINATION TESTS ---{Colors.END}\n")
	# Define complex vectors
	print("Defining complex vectors vc1, vc2...")
	vc1 = Vector([1+2j, 0, -1j])
	vc2 = Vector([0, 3-4j, 2])
	print(f"Vector vc1: {Colors.GREEN}{vc1}{Colors.END}")
	print(f"Vector vc2: {Colors.GREEN}{vc2}{Colors.END}")
	print()

	# Test linear combination with complex scalars
	print(f"{Colors.TEST}Testing Complex Linear Combination 1{Colors.END}", end="\n---\n")
	result1 = linear_combination([vc1, vc2], [2, -1j])
	expected1 = Vector([
		2*(1+2j) + (-1j)*0,
		2*0 + (-1j)*(3-4j),
		2*(-1j) + (-1j)*2
	])
	print(f"Linear combination Expected: {Colors.EXPECTED}{expected1}{Colors.END}")
	if result1 == expected1:
		print(f"Result: {Colors.CORRECT}{result1} (Correct){Colors.END}")
	else:
		print(f"Result: {Colors.RED}{result1} (Incorrect){Colors.END}")
	print()

	# Another test
	print(f"{Colors.TEST}Testing Complex Linear Combination 2{Colors.END}", end="\n---\n")
	result2 = linear_combination([vc1, vc2], [1-1j, 0.5])
	expected2 = Vector([
		(1-1j)*(1+2j) + 0.5*0,
		(1-1j)*0 + 0.5*(3-4j),
		(1-1j)*(-1j) + 0.5*2
	])
	print(f"Linear combination Expected: {Colors.EXPECTED}{expected2}{Colors.END}")
	if result2 == expected2:
		print(f"Result: {Colors.CORRECT}{result2} (Correct){Colors.END}")
	else:
		print(f"Result: {Colors.RED}{result2} (Incorrect){Colors.END}")
	print()


test_linear_combination()
test_complex_linear_combination()

