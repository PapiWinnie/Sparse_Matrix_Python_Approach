class SparseMatrix:
    # Constructor to initialize the sparse matrix with given dimensions
    def __init__(self, numRows, numCols):
        self.numRows = numRows  # Number of rows in the matrix
        self.numCols = numCols  # Number of columns in the matrix
        self.matrix = {}  # Dictionary to store non-zero elements as (row, col): value pairs

    # Class method to create a SparseMatrix instance from a file
    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()  # Read all lines from the file
                
            # Get matrix dimensions from the first two lines
            numRows = int(lines[0].strip().split('=')[1])  # Extract number of rows
            numCols = int(lines[1].strip().split('=')[1])  # Extract number of columns
            
            # Create an instance of SparseMatrix with the extracted dimensions
            matrix = cls(numRows, numCols)
            
            # Process the remaining lines to extract matrix elements
            for line in lines[2:]:
                if line.strip():  # Skip empty lines
                    # Remove parentheses and split by comma to extract row, column, and value
                    values = line.strip('()\n').split(',')
                    row, col, value = map(int, values)  # Convert extracted values to integers
                    matrix.set_element(row, col, value)  # Set the non-zero element in the matrix
                    
            return matrix  # Return the constructed SparseMatrix instance
            
        except Exception as e:
            raise ValueError(f"Error reading file {file_path}: {str(e)}")  # Handle file reading errors

    # Method to set an element in the matrix at (row, col) with the given value
    def set_element(self, row, col, value):
        if value != 0:  # Only store non-zero values
            self.matrix[(row, col)] = value  # Store the value at the specified position
        elif (row, col) in self.matrix:  # Remove the element if it is zero and exists in the matrix
            del self.matrix[(row, col)]  # Delete the element

    # Method to get the value of an element at (row, col), returns 0 if the element is not found
    def get_element(self, row, col):
        return self.matrix.get((row, col), 0)  # Return the value or 0 if the element does not exist
    
    # Method to add two SparseMatrix instances and return the result as a new SparseMatrix
    def add(self, other):
        # Calculate the maximum number of rows and columns from both matrices
        max_rows = max(self.numRows, other.numRows)
        max_cols = max(self.numCols, other.numCols)
        result = SparseMatrix(max_rows, max_cols)  # Create a result matrix with the maximum dimensions

        # Add elements from the current matrix to the result matrix
        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value)

        # Add elements from the other matrix to the result matrix
        for (row, col), value in other.matrix.items():
            current_value = result.get_element(row, col)  # Get current value at (row, col) in the result
            result.set_element(row, col, current_value + value)  # Add the value from the second matrix

        return result  # Return the resulting matrix after addition
    
    # Method to subtract two SparseMatrix instances and return the result as a new SparseMatrix
    def subtract(self, other):
        # Calculate the maximum number of rows and columns from both matrices
        max_rows = max(self.numRows, other.numRows)
        max_cols = max(self.numCols, other.numCols)
        result = SparseMatrix(max_rows, max_cols)  # Create a result matrix with the maximum dimensions

        # Subtract elements from the current matrix and add them to the result matrix
        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value)

        # Subtract elements from the other matrix and add them to the result matrix
        for (row, col), value in other.matrix.items():
            current_value = result.get_element(row, col)  # Get current value at (row, col) in the result
            result.set_element(row, col, current_value - value)  # Subtract the value from the second matrix

        return result  # Return the resulting matrix after subtraction
    
    # Method to multiply two SparseMatrix instances and return the result as a new SparseMatrix
    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix multiplication requires A.cols == B.rows.")  # Check for dimension compatibility

        result = SparseMatrix(self.numRows, other.numCols)  # Create a result matrix with appropriate dimensions

        # Perform matrix multiplication by iterating over the non-zero elements of both matrices
        for (row1, col1), value1 in self.matrix.items():
            for (row2, col2), value2 in other.matrix.items():
                if col1 == row2:  # Only multiply if the column of matrix 1 matches the row of matrix 2
                    current = result.get_element(row1, col2)  # Get the current value at (row1, col2)
                    result.set_element(row1, col2, current + value1 * value2)  # Add the product to the result

        return result  # Return the resulting matrix after multiplication
