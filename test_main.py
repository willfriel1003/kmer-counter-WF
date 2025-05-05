#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
from main import parse_fasta, extract_kmer_context, format_kmer_data

def test_parse_fasta_single_sequence(tmp_path):
    """
    Test that a simple FASTA file with one sequence returns the correct string.
    """
    # Create a temporary FASTA file
    file_path = tmp_path / "test.fa"
    file_path.write_text(">sequence1\nATGC\nGCTA")

    # Read the sequence
    result = parse_fasta(str(file_path))

    # Check that lines were joined and cleaned properly
    assert result == "ATGCGCTA"

def test_parse_fasta_multiple_sequences(tmp_path):
    """
    Test a FASTA file with two separate sequences.
    """
    file_path = tmp_path / "test2.fa"
    file_path.write_text(">seq1\nAAA\nTTT\n>seq2\nGGG\nCCC")

    result = parse_fasta(str(file_path))

    assert result == "AAATTTGGGCCC"

def test_extract_kmer_context_basic_case():
    """
    Test that k-mers and their next characters are counted correctly.
    """
    sequence = "ATGCG"
    k = 2
    result = extract_kmer_context(sequence, k)

    assert result["AT"]["G"] == 1
    assert result["TG"]["C"] == 1
    assert result["GC"]["G"] == 1

def test_extract_kmer_context_not_enough_sequence():
    """
    Test that an empty dictionary is returned if the sequence is too short.
    """
    sequence = "AT"
    k = 3
    result = extract_kmer_context(sequence, k)

    assert result == {}

def test_format_kmer_data_simple_case():
    """
    Test that the formatted output lines are correct.
    """
    test_data = {
        "AT": {"G": 2},
        "TG": {"A": 1, "T": 1}
    }

    result = format_kmer_data(test_data)

    expected_output = [
        "AT: total 2",
        "  G: 2",
        "TG: total 2",
        "  A: 1",
        "  T: 1"
    ]

    assert result == expected_output

