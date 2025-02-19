# code/src/main.py
import os
from sparse_matrix import SparseMatrix

def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current_dir))

def find_txt_files(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt') and f != 'result.txt']
    if len(txt_files) < 2:
        raise FileNotFoundError("Error: Not enough .txt files found in sample_inputs folder.")
    return [os.path.join(folder_path, txt_files[i]) for i in range(2)]

def save_result(result, operation_name, output_path):
    with open(output_path, "w") as f:
        f.write(f"rows={result.numRows}\n")
        f.write(f"cols={result.numCols}\n")
        for (row, col), value in sorted(result.matrix.items()):
            f.write(f"({row},{col},{value})\n")

def main():
    try:
        # Set up paths
        project_root = get_project_root()
        input_folder = os.path.join(project_root, "sample_inputs")
        result_path = os.path.join(input_folder, "result.txt")
        
        print(f"Looking for input files in: {input_folder}")
        
        # Load matrix files
        matrix_files = find_txt_files(input_folder)
        print(f"Loading matrices from: {os.path.basename(matrix_files[0])} and {os.path.basename(matrix_files[1])}")
        
        matrix1 = SparseMatrix.from_file(matrix_files[0])
        matrix2 = SparseMatrix.from_file(matrix_files[1])
        
        print(f"Matrix 1: {matrix1.numRows}x{matrix1.numCols}")
        print(f"Matrix 2: {matrix2.numRows}x{matrix2.numCols}")

                # Choose operation
        print("\nChoose operation: 1) Add 2) Subtract 3) Multiply")
        operation = input().strip()
        
        # Perform operation
        if operation == '1':
            result = matrix1.add(matrix2)
            operation_name = "Addition"
        elif operation == '2':
            result = matrix1.subtract(matrix2)
            operation_name = "Subtraction"
        elif operation == '3':
            result = matrix1.multiply(matrix2)
            operation_name = "Multiplication"
        else:
            print("Invalid operation")
            return
        
        # Save result
        save_result(result, operation_name, result_path)
        print(f"\nResult written to {os.path.basename(result_path)}")

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()










