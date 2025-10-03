# File Functions

import tkinter as tk
from tkinter import filedialog

# Create popup window to choose FASTA file
def choose_file():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(
        title="Select FASTA file",
        filetypes=[("FASTA files", "*fasta *.fa"), ("All files", "*.*")]
    )
    return filename

# Reads .FASTA file -> Skips header lines and combines into one big string
def read_fasta(filename):
    with open(filename) as file:
        lines = file.readlines()
        # Skip header lines starting with '>'
        sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
        return sequence