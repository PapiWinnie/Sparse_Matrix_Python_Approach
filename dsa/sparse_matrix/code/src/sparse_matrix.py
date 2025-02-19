# code/src/sparse_matrix.py
class SparseMatrix:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.matrix = {}

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
            # Get dimensions
            numRows = int(lines[0].strip().split('=')[1])
            numCols = int(lines[1].strip().split('=')[1])
            
            # Create matrix
            matrix = cls(numRows, numCols)
            
            # Add elements
            for line in lines[2:]:
                if line.strip():
                    # Remove parentheses and split by comma
                    values = line.strip('()\n').split(',')
                    row, col, value = map(int, values)
                    matrix.set_element(row, col, value)
                    
            return matrix
            
        except Exception as e:
            raise ValueError(f"Error reading file {file_path}: {str(e)}")

    def set_element(self, row, col, value):
        if value != 0:  # Only store non-zero values
            self.matrix[(row, col)] = value
        elif (row, col) in self.matrix:
            del self.matrix[(row, col)]

    def get_element(self, row, col):
        return self.matrix.get((row, col), 0)
    
    def add(self, other):
        max_rows = max(self.numRows, other.numRows)
        max_cols = max(self.numCols, other.numCols)
        result = SparseMatrix(max_rows, max_cols)

        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value)

        for (row, col), value in other.matrix.items():
            current_value = result.get_element(row, col)
            result.set_element(row, col, current_value + value)

        return result
    
    def subtract(self, other):
        max_rows = max(self.numRows, other.numRows)
        max_cols = max(self.numCols, other.numCols)
        result = SparseMatrix(max_rows, max_cols)

        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value)

        for (row, col), value in other.matrix.items():
            current_value = result.get_element(row, col)
            result.set_element(row, col, current_value - value)

        return result
    
    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix multiplication requires A.cols == B.rows.")

        result = SparseMatrix(self.numRows, other.numCols)

        for (row1, col1), value1 in self.matrix.items():
            for (row2, col2), value2 in other.matrix.items():
                if col1 == row2:
                    current = result.get_element(row1, col2)
                    result.set_element(row1, col2, current + value1 * value2)

        return result




