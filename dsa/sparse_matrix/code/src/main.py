# code/src/main.py
import os
from sparse_matrix import SparseMatrix

def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current_dir))

