# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    if not seq:
        raise ValueError("Invalid input")
    if any(i not in ALLOWED_NUC for i in seq):
        raise ValueError("Invalid nucleotide")
    rna = []
    for i in seq:
        rna.append(TRANSCRIPTION_MAPPING[i])
    return rna


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    rna = transcribe(seq)
    return rna[::-1]
