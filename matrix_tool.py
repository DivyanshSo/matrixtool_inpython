import numpy as np    #for matrix operations.......
import tkinter as tk   #for gui user interface..
from tkinter import messagebox   #for error display...

class MatrixOperationsApp:    #create gui application class....
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations Tool")
        
        #input field for matrices....
        self.label = tk.Label(root, text="Enter matrices (comma-separated values, rows separated by new lines):")
        self.label.pack()
        
        self.entry1 = tk.Text(root, height=5, width=40)
        self.entry1.pack()
        
        self.entry2 = tk.Text(root, height=5, width=40)
        self.entry2.pack()
        
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        
        self.result_display = tk.Text(root, height=5, width=40, state='disabled')
        self.result_display.pack()
        
        #creating buttons in the tool...
        self.add_button = tk.Button(root, text="Add", command=self.add_matrices)
        self.add_button.pack()
        
        self.subtract_button = tk.Button(root, text="Subtract", command=self.subtract_matrices)
        self.subtract_button.pack()
        
        self.multiply_button = tk.Button(root, text="Multiply", command=self.multiply_matrices)
        self.multiply_button.pack()
        
        self.transpose_button = tk.Button(root, text="Transpose Matrix 1", command=self.transpose_matrix)
        self.transpose_button.pack()
        
        self.determinant_button = tk.Button(root, text="Determinant of Matrix 1", command=self.calculate_determinant)
        self.determinant_button.pack()
    
    def get_matrix(self, text_widget):
        try:
            matrix_str = text_widget.get("1.0", tk.END).strip()
            if not matrix_str:
                return None
            matrix = np.array([list(map(float, row.split(','))) for row in matrix_str.split('\n') if row])
            return matrix
        except ValueError:
            messagebox.showerror("Input Error", "Invalid matrix input. Please enter valid numbers.")
            return None
    
    #to display result of operation.....
    def display_result(self, result):
        self.result_display.config(state='normal')
        self.result_display.delete("1.0", tk.END)
        self.result_display.insert(tk.END, str(result))
        self.result_display.config(state='disabled')
    
    #matrix addition is done here....
    def add_matrices(self):
        matrix1 = self.get_matrix(self.entry1)
        matrix2 = self.get_matrix(self.entry2)
        if matrix1 is None or matrix2 is None:
            return
        if matrix1.shape != matrix2.shape:
            messagebox.showerror("Dimension Error", "Matrices must have the same dimensions for addition.")
            return
        self.display_result(matrix1 + matrix2)

    #matrix subtraction is done here....
    def subtract_matrices(self):
        matrix1 = self.get_matrix(self.entry1)
        matrix2 = self.get_matrix(self.entry2)
        if matrix1 is None or matrix2 is None:
            return
        if matrix1.shape != matrix2.shape:
            messagebox.showerror("Dimension Error", "Matrices must have the same dimensions for subtraction.")
            return
        self.display_result(matrix1 - matrix2)

    #matrix multiplication is done here....
    def multiply_matrices(self):
        matrix1 = self.get_matrix(self.entry1)
        matrix2 = self.get_matrix(self.entry2)
        if matrix1 is None or matrix2 is None:
            return
        if matrix1.shape[1] != matrix2.shape[0]:
            messagebox.showerror("Dimension Error", "Number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
            return
        self.display_result(np.dot(matrix1, matrix2))

    #matrix transpose is done here....
    def transpose_matrix(self):
        matrix1 = self.get_matrix(self.entry1)
        if matrix1 is None:
            return
        self.display_result(matrix1.T)

    #calculate the determinant..
    def calculate_determinant(self):
        matrix1 = self.get_matrix(self.entry1)
        if matrix1 is None:
            return
        if matrix1.shape[0] != matrix1.shape[1]:
            messagebox.showerror("Dimension Error", "Matrix must be square to calculate determinant.")
            return
        self.display_result(np.linalg.det(matrix1))

#running the application....
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixOperationsApp(root)
    root.mainloop()