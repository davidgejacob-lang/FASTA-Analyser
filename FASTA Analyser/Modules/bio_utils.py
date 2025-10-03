# Useful Bioinformatic Functions

# Create the reverse complement DNA seq    
def reverse_complement(seq):
    if not is_valid_dna(seq):
        raise ValueError("Sequence contains invalid DNA bases.")
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in seq.upper()[::-1])
    for base in seq:
        if base not in complement:
            raise ValueError(f"Invalid base '{base}' found in sequence.")
    return "".join(complement[base] for base in reversed(seq))

# Evaluates GC% content in seq
def gc_content(seq):
    seq = seq.upper()
    gc = seq.count('G') + seq.count('C')
    return gc / len(seq) * 100 if len(seq) > 0 else 0

# Converts DNA into RNA (replace T with U)
def transcribe(seq):
    return seq.upper().replace('T', 'U')

# Checks if seq contains only valid bases
def is_valid_dna(seq):
    seq = seq.upper()
    return bool(seq) and all(base in 'ATCG' for base in seq)

def count_bases(dna_sequence):
    """
    Counts the occurrences of each DNA base (A, T, C, G) in the given sequence,
    and calculates the GC% and AT% content.

    Parameters:
        dna_sequence (str): The DNA sequence to analyze.

    Returns:
        tuple: A dictionary with base counts, GC content percentage, and AT content percentage.
    """
    # Initialize base counts
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    
    # Count each base in the sequence
    for base in dna_sequence.upper():
        if base in base_counts:
            base_counts[base] += 1
    
    # Calculate total bases
    total_bases = sum(base_counts.values())
    
    # Calculate GC% and AT%
    gc_content = (base_counts['G'] + base_counts['C']) / total_bases * 100 if total_bases > 0 else 0
    at_content = (base_counts['A'] + base_counts['T']) / total_bases * 100 if total_bases > 0 else 0
    
    return base_counts, gc_content, at_content