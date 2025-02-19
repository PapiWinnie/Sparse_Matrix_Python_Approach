Here’s the complete content of the `README.md` file in one piece:

```markdown
# Sparse Matrix Operations

This project provides a Python implementation of sparse matrices and supports basic matrix operations such as addition, subtraction, and multiplication. The sparse matrix is represented using a dictionary to store only the non-zero elements, ensuring efficient memory usage.

## Features

- **SparseMatrix Class**: Represents a sparse matrix and supports operations like addition, subtraction, and multiplication.
- **File Handling**: Load sparse matrices from `.txt` files and save the result to a file.
- **Matrix Operations**: Add, subtract, and multiply sparse matrices while preserving memory efficiency.

## Project Structure

```
/project-root
    ├── /code
    │   ├── /src
    │   │   ├── sparse_matrix.py  # Contains the SparseMatrix class and its methods
    │   │   └── main.py           # Main script to handle matrix file loading, operations, and results
    └── README.md                 # Project documentation
```

## Prerequisites

- Python 3.x
- Basic understanding of sparse matrices and matrix operations

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sparse-matrix-operations
```

### 2. Install Dependencies

There are no external dependencies for this project as it only uses built-in Python libraries.

### 3. File Structure

The project requires `.txt` files to represent sparse matrices. These files should have the following format:

```
rows=4
cols=4
(0,1,5)
(1,2,8)
(3,3,2)
...
```

- The first two lines specify the number of rows and columns of the matrix.
- Each subsequent line represents a non-zero element in the matrix in the form `(row, col, value)`.

### 4. Run the Program

The `main.py` script handles loading two sparse matrices from the `sample_inputs` folder, performing the chosen operation, and saving the result.

1. Place the `.txt` matrix files in the `/sample_inputs` directory.
2. Run the program:

```bash
python code/src/main.py
```

3. The program will prompt you to select a matrix operation:
    - `1` for Addition
    - `2` for Subtraction
    - `3` for Multiplication

The result will be saved in `result.txt` in the same directory.

### 5. Result

The result file will contain the resulting matrix in the same format as the input file:

```
rows=<result-rows>
cols=<result-cols>
(row1,col1,value1)
(row2,col2,value2)
...
```

## SparseMatrix Class

The `SparseMatrix` class has the following methods:

### `__init__(self, numRows, numCols)`
Constructor to initialize the sparse matrix with the given dimensions.

### `@classmethod from_file(cls, file_path)`
Class method to load a sparse matrix from a `.txt` file.

### `set_element(self, row, col, value)`
Set the value of a matrix element at the given position. It only stores non-zero elements.

### `get_element(self, row, col)`
Get the value of a matrix element at the given position. Returns `0` if the element is not set.

### `add(self, other)`
Add two sparse matrices and return the resulting matrix.

### `subtract(self, other)`
Subtract another sparse matrix from the current one and return the resulting matrix.

### `multiply(self, other)`
Multiply two sparse matrices and return the resulting matrix. It raises an error if the matrices' dimensions are not compatible for multiplication.

## Error Handling

The following errors are handled in the program:

- **FileNotFoundError**: Raised if not enough `.txt` files are found in the `sample_inputs` folder.
- **ValueError**: Raised if there is an issue reading a file or performing an operation (e.g., incompatible matrix dimensions for multiplication).
- **Exception**: Any unexpected errors will be caught and printed to the console.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the MIT License.
```

You can save this as the `README.md` file in your project directory!