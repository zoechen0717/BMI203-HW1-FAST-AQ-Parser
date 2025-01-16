# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Valid Fasta
    fasta_parser = FastaParser("tests/good.fasta")
    sequences = list(fasta_parser)
    assert len(sequences) == 2
    assert sequences[0] == ("seq1", "ATGC")
    assert sequences[1] == ("seq2", "GCTA")

    # Eempty Fasta
    fasta_parser = FastaParser("tests/blank.fasta")
    with pytest.raises(ValueError, match="File .* had 0 lines"):
        list(fasta_parser)

    # Bad Fasta
    fasta_parser = FastaParser("tests/bad.fasta")
    with pytest.raises(ValueError):
        list(fasta_parser)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Test if a Fastq file is passed instead of Fasta
    fasta_parser = FastaParser("tests/good.fastq")
    with pytest.raises(ValueError):
        list(fasta_parser)


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads
    in the example Fastq File.
    """
    # valid Fastq
    fastq_parser = FastqParser("tests/good.fastq")
    reads = list(fastq_parser)
    assert len(reads) == 2
    assert reads[0] == ("seq1", "ATGC", "IIII")
    assert reads[1] == ("seq2", "GCTA", "JJJJ")

    # empty Fastq
    fastq_parser = FastqParser("tests/blank.fastq")
    with pytest.raises(ValueError, match="File .* had 0 lines"):
        list(fastq_parser)

    # corrupted Fastq
    fastq_parser = FastqParser("tests/bad.fastq")
    with pytest.raises(ValueError):
        list(fastq_parser)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_parser = FastqParser("tests/good.fasta")
    with pytest.raises(ValueError):
        list(fastq_parser)
