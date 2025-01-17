from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
    fasta_parser = FastaParser("data/test.fa")
    fastq_parser = FastqParser("data/test.fq")

    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print("FastaParser Transcriptions:")
    for header, sequence in fasta_parser:
        rna = transcribe(sequence)
        print(f"{rna}")

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print("FastqParser Transcriptions:")
    for header, sequence, quality in fastq_parser:
        rna = transcribe(sequence)
        print(f"{rna}")

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print("\nFastaParser Reverse Transcriptions:")
    for header, sequence in fasta_parser:
        reverse_rna = reverse_transcribe(sequence)
        print(f"{reverse_rna}")

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print("\nFastqParser Reverse Transcriptions:")
    for header, sequence, quality in fastq_parser:
        reverse_rna = reverse_transcribe(sequence)
        print(f"{reverse_rna}")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
