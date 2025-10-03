import csv
import os
from Bio import SeqIO
from tkinter import filedialog, Tk


## Importing choose_file function from my created module
from Modules.file_utils import choose_file

## Importing both count_bases & DNA base validator from bio_utils
from Modules.bio_utils import count_bases, is_valid_dna

## Importing both reverse_complement() & transcribe_dna() from bio_utils
from Modules.bio_utils import reverse_complement, transcribe

# FASTA Parser
def analyse_fasta(filepath, summary_path, csv_path, convert_sequences):
    if not filepath:
        print("No File Selected")
        return
    
    # Prepare CSV & Summary file
    with open(csv_path, "w", newline="") as csvfile, open(summary_path, "w") as textfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence ID", "Length", "A", "T", "C", "G", "GC %", "AT %"])

        # Write headings to the text summary once
        textfile.write(f"{'='*60}\n")
        textfile.write(f"<<< FASTA Analysis Report\n")
        textfile.write(f"{'-'*60}\n")
        textfile.write(f"<<< Input file: {os.path.basename(filepath)}\n")
        textfile.write(f"<<< Reverse complement & RNA conversion: {'Yes' if convert_sequences else 'No'}\n")
        textfile.write(f"{'='*60}\n\n")


        for record in SeqIO.parse(filepath, "fasta"):
            seq_id = record.id
            sequence = str(record.seq).upper()

            if not is_valid_dna(sequence):
                print(f"Skipping invalid sequence: {seq_id}")
                textfile.write(f"Skipping invalid sequence: {seq_id} (invalid DNA bases found)\n")
                textfile.write("-" * 50 + "\n")
                continue

            base_counts, gc_content, at_content = count_bases(sequence)
            a = base_counts.get("A", 0)
            t = base_counts.get("T", 0)
            c = base_counts.get("C", 0)
            g = base_counts.get("G", 0)
            length = len(sequence)

            # Write to CSV
            writer.writerow([seq_id, length, a, t, c, g, f"{gc_content:.2f}", f"{at_content:.2f}"])            

            print(f"Analysing sequence: {seq_id}")
            print(f"Length: {length} bases")
            print(f"Base Counts: A={a}, T={t}, C={c}, G={g}")
            print(f"GC Content: {gc_content:.2f}%")
            print(f"AT Content: {at_content:.2f}%")
            print("-" * 50)

            # Write to text summary
            textfile.write(f"Sequence ID: {seq_id}\n")
            textfile.write(f"Length: {length} bases\n")
            textfile.write(f"Base Counts: A={a}, T={t}, C={c}, G={g}\n")
            textfile.write(f"GC Content: {gc_content:.2f}%\n")
            textfile.write(f"AT Content: {at_content:.2f}%\n")

            if convert_sequences:
                rev_comp = reverse_complement(sequence)
                rna = transcribe(sequence)
                textfile.write(f"\nReverse Complement:\n{rev_comp}\n")
                textfile.write(f"Transcribed RNA:\n{rna}\n")

            textfile.write("-" * 50 + "\n")

    print(f"\nSummary saved to: {summary_path}")
    print(f"CSV saved to: {csv_path}")


# Entry Point
def main():
    # File Selection
    fasta_file = choose_file()
    if not fasta_file:
        print("No FASTA file selected. Exiting.")
        return
    
    # Ask user if they want conversions
    convert_choice = input("Include reverse complement & RNA conversion? (y/n): ").strip().lower()
    convert_sequences = convert_choice == 'y'

    # Save dialog for summary
    root = Tk()
    root.withdraw()
    summary_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save summary of results to...",
        initialfile="fasta_summary.txt"
    )
    root.destroy()

    if not summary_path:
        print("Save cancelled. Exiting")
        return
    
    # Derive CSV file path from summary filename
    csv_path = summary_path.replace(".txt", "_summary.csv")


    # Analyse and write to summary
    analyse_fasta(fasta_file, summary_path, csv_path, convert_sequences)

# Entry point
if __name__ == "__main__":
    main()