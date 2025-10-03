# 🧬 FASTA Analyser

A lightweight, modular Python tool for analysing FASTA files — designed for bioinformatics, molecular biology, and educational use. It can calculate nucleotide statistics, generate reverse complements, transcribe RNA, and export summaries to human-readable `.txt` files and `.csv`.

---

## 🚀 Features

- Load `.fasta` files using a graphical file selector
- Validate DNA sequences
- Calculate:
  - Base composition (A, T, C, G)
  - GC and AT content
  - Sequence length
- Generate:
  - Reverse complements
  - Transcribed RNA sequences
- Export:
  - Plain text summaries
  - CSV tabular output
- Built with **BioPython** and **Tkinter**

---

## 🛠 Technologies Used

- Python 3.x
- [BioPython](https://biopython.org/)
- Tkinter (built-in GUI for file selection)

---

## 📁 Folder Structure

```
FASTA_Analyser/
├── Example Data/
│   └── complex_sequences.fasta
│   └── simple_sequences.fasta
├── Modules/
│   ├── bio_utils.py
│   └── file_utils.py
├── Sequence Output/
│   └── example_fasta_summary.txt
│   └── example_fasta_summary.csv
├── FASTA_analyser.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📥 Example Input

```
>Human_COX1
ATGACCAACATTCGAAAAACACATAATCGGGAGCCCCCTCTAGCCTAGCCCTATATGGCGTCTTCTATATAGC
```

## 📤 Example Output

- Sequence ID: Human_COX1
- Length: 70 bases
- A: 15 | T: 20 | C: 18 | G: 17
- GC Content: 50.00%
- AT Content: 50.00%

---

## ▶️ How to Run

🧪 Setting Up a Virtual Environment (Recommended)

To ensure dependencies like biopython work properly and avoid version conflicts, run this project inside a virtual environment.

1. On Windows:
```bash
# Create the virtual environment
python -m venv venv
  
# Activate it
venv\Scripts\activate
  
# Install dependencies
pip install -r requirements.txt
  
# Run the program
python fasta_analyzer.py
```

2. On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 fasta_analyzer.py
```

3. To deactivate the environment later:
```bash
deactivate
```

📦 If You Don't Want a Virtual Environment

4. You can also install the package globally (not recommended for long term):
```bash
pip install biopython tk
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Run the script:
```bash
python fasta_analyzer.py
```

7. Use the GUI window to select your FASTA file.

---

## 🧪 Future Improvements

- GUI front-end with full output browser
- Web app version using Flask or Streamlit
- Add unit testing (pytest)

---

*Created by Jacob Davidge · MSc Industrial Biotechnology*
