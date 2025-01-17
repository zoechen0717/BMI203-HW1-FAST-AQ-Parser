# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_transcribe():
    """
    Unit tests for the transcribe function.
    """
    # Test with a valid DNA sequence
    assert transcribe("A") == "U"
    assert transcribe("TTT") == "AAA"
    assert transcribe("ATCG") == "UAGC"
    assert transcribe("TTAGCC") == "AAUCGG"
    assert transcribe("ACTGAACCC") == "UGACUUGGG"


    # Test with an empty DNA sequence
    try:
        transcribe("")
    except ValueError as e:
        assert str(e) == "Invalid input"

    # Test with invalid characters in the sequence
    try:
        transcribe("ATXG")
    except ValueError as e:
        assert str(e) == "Invalid nucleotide"


def test_reverse_transcribe():
    """
    Unit tests for the reverse_transcribe function.
    """
    # Test with a valid DNA sequence
    assert reverse_transcribe("A") == "U"
    assert reverse_transcribe("AAA") == "UUU"
    assert reverse_transcribe("ATCG") == "CGAU"
    assert reverse_transcribe("TTAGCC") == "GGCUAA"
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU"

    # Test with an empty input
    try:
        reverse_transcribe("")
    except ValueError as e:
        assert str(e) == "Invalid input"

    # Test with invalid characters in the sequence
    try:
        reverse_transcribe("ATXG")
    except ValueError as e:
        assert str(e) == "Invalid nucleotide"
