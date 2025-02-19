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

