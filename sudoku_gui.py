import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def _init_(self, master):
        self.master = master
        master.title("Sudoku Solver")
        self.entries = [[tk.Entry(master, width=2, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=9, column=0, columnspan=9, sticky="nsew")

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j, padx=1, pady=1)
    
    def get_grid(self):
        grid = []
        for row in self.entries:
            current_row = []
            for entry in row:
                val = entry.get()
                if val.isdigit():
                    current_row.append(int(val))
                else:
                    current_row.append(0)
            grid.append(current_row)
        return grid

    def set_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve_sudoku(self):
        grid = self.get_grid()
        if self.solve(grid):
            self.set_grid(grid)
            messagebox.showinfo("Success", "Sudoku Solved!")
        else:
            messagebox.showerror("Failure", "No solution exists for the given Sudoku.")

# Run the GUI
if _name_ == "_main_":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
