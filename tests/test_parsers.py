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
    parser = FastaParser("tests/good.fasta")
    seq = list(fasta_parser)
    assert seq[0] == ("seq1", "ATGC")
    assert seq[1] == ("seq2", "GCTA")

    # Eempty Fasta
    parser = FastaParser("tests/blank.fasta")
    with pytest.raises(ValueError, match="File .* had 0 lines"):
        list(parser)

    # Bad Fasta
    parser = FastaParser("tests/bad.fasta")
    assert parser == ("seq1", "ATGC")


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in, if a fastq file is
    read, the first item is None
    """
    # Test if a Fastq file is passed instead of Fasta
    parser = FastaParser("tests/good.fastq")
    seq = list(parser)
    assert seq[0] == (None, '@seq1')
    assert seq[1] == (None, 'ATGC')
    assert seq[2] == (None, '+')
    assert seq[3] == (None, 'IIII')
    assert seq[4] == (None, '@seq2')
    assert seq[5] == (None, 'GCTA')



def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads
    in the example Fastq File.
    """
    # valid Fastq
    parser = FastqParser("tests/good.fastq")
    reads = list(parser)
    assert reads[0] == ("seq1", "ATGC", "IIII")
    assert reads[1] == ("seq2", "GCTA", "JJJJ")

    # empty Fastq
    parser = FastqParser("tests/blank.fastq")
    with pytest.raises(ValueError, match="File .* had 0 lines"):
        list(parser)

    # corrupted Fastq
    parser = FastqParser("tests/bad.fastq")
    assert parser == ('seq1', 'ATGC', 'IIII')

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    parser = FastqParser("tests/good.fasta")
    reads = list(parser)
    assert reads[0] == (None, '>seq1', 'ATGC')
    assert reads[1] == (None, '>seq2', 'GCTA')
