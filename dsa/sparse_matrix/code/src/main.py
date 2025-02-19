import os
from sparse_matrix import SparseMatrix  # Import the SparseMatrix class for matrix operations

# Function to get the project's root directory
def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
    return os.path.dirname(os.path.dirname(current_dir))  # Return the parent directory (project root)

# Function to find .txt files in the specified folder, excluding 'result.txt'
def find_txt_files(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt') and f != 'result.txt']  # Filter .txt files
    if len(txt_files) < 2:
        raise FileNotFoundError("Error: Not enough .txt files found in sample_inputs folder.")  # Ensure at least 2 files are found
    return [os.path.join(folder_path, txt_files[i]) for i in range(2)]  # Return the paths of the first two .txt files

# Function to save the matrix operation result to a file
def save_result(result, operation_name, output_path):
    with open(output_path, "w") as f:  # Open the result file in write mode
        f.write(f"rows={result.numRows}\n")  # Write the number of rows
        f.write(f"cols={result.numCols}\n")  # Write the number of columns
        # Write non-zero elements in the matrix (sorted by row and column)
        for (row, col), value in sorted(result.matrix.items()):
            f.write(f"({row},{col},{value})\n")

# Main function to execute the program logic
def main():
    try:
        # Set up paths for input and output files
        project_root = get_project_root()  # Get the root directory of the project
        input_folder = os.path.join(project_root, "sample_inputs")  # Set the input folder path
        result_path = os.path.join(input_folder, "result.txt")  # Set the path for the result file
        
        print(f"Looking for input files in: {input_folder}")  # Print where the input files are located
        
        # Load the matrix files
        matrix_files = find_txt_files(input_folder)  # Find the .txt matrix files
        print(f"Loading matrices from: {os.path.basename(matrix_files[0])} and {os.path.basename(matrix_files[1])}")  # Print the filenames being loaded
        
        # Read the matrices from the files
        matrix1 = SparseMatrix.from_file(matrix_files[0])  # Load the first matrix
        matrix2 = SparseMatrix.from_file(matrix_files[1])  # Load the second matrix
        
        # Print the dimensions of the loaded matrices
        print(f"Matrix 1: {matrix1.numRows}x{matrix1.numCols}")
        print(f"Matrix 2: {matrix2.numRows}x{matrix2.numCols}")

        # Prompt the user to choose an operation
        print("\nChoose operation: 1) Add 2) Subtract 3) Multiply")
        operation = input().strip()  # Get the user's input and remove leading/trailing spaces
        
        # Perform the chosen operation
        if operation == '1':
            result = matrix1.add(matrix2)  # Perform addition
            operation_name = "Addition"
        elif operation == '2':
            result = matrix1.subtract(matrix2)  # Perform subtraction
            operation_name = "Subtraction"
        elif operation == '3':
            result = matrix1.multiply(matrix2)  # Perform multiplication
            operation_name = "Multiplication"
        else:
            print("Invalid operation")  # Handle invalid input
            return
        
        # Save the result to a file
        save_result(result, operation_name, result_path)  # Save the result of the operation
        print(f"\nResult written to {os.path.basename(result_path)}")  # Print the result file name

    except FileNotFoundError as e:
        print(e)  # Print error message if files are not found
    except ValueError as e:
        print(f"Error: {e}")  # Print error message for invalid matrix operations (e.g., dimension mismatch)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Print any other unexpected errors

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
