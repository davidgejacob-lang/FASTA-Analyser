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

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python fasta_analyzer.py
```

3. Use the GUI window to select your FASTA file.

---

## 🧪 Future Improvements

- GUI front-end with full output browser
- Web app version using Flask or Streamlit
- Add unit testing (pytest)

---

## 📄 License

MIT License — see `LICENSE` file for details.

---

*Created by Jacob Davidge · MSc Industrial Biotechnology*
