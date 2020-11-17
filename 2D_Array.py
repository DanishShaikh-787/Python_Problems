"""
   * Author - danish
   * Date - 16/11/20
   * Time - 1:30 PM
   * Title - A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
"""
# A basic code for matrix input from user

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
	a.append(int(input()))
	matrix.append(a)

# For printing the matrix
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()
