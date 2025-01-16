# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # Check if the input sequence is empty
    if not seq:
        raise ValueError("Invalid input")
    # Check if all characters in the sequence are valid.
    if any(i not in ALLOWED_NUC for i in seq):
        raise ValueError("Invalid nucleotide")
    # Initialize an empty list
    rna = []
    # Iterate through each nucleotide
    for i in seq:
        # Map each DNA nucleotide to RNA nucleotide
        rna.append(TRANSCRIPTION_MAPPING[i])
    # Join the list of RNA
    return "".join(rna)


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Call the transcribe function: DNA to RNA
    rna = transcribe(seq)
    # Reverse the RNA sequence
    return rna[::-1]
