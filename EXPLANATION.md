# Explanation of K-mer Counter Code

This document explains how the program works, what data structures were used, how edge cases are handled, and how the code avoids mistakes like overcounting.

---

## What the Program Does

The program takes a DNA sequence from a FASTA file and breaks it into overlapping substrings called k-mers (substrings of length `k`). It counts how often each k-mer appears and also counts how often each letter (A, C, G, or T) comes right after each k-mer.

For example, if `k = 2` and the sequence is `ATGCA`, the k-mers are:

AT, TG, GC, CA


Each one has a character that comes after it:
- "AT" is followed by "G"
- "TG" is followed by "C"
- "GC" is followed by "A"

The last k-mer ("CA") is the last valid one because there's no next character after it in this case.

---

## Data Structures Used

The program uses a dictionary of dictionaries to store the results.

- The **outer dictionary** stores each unique k-mer.
- The **inner dictionary** stores what letters followed that k-mer and how many times.

### Example:

{
"AT": {"G": 2},
"TG": {"C": 1, "T": 1}
}


This means:
- "AT" is followed by "G" two times.
- "TG" is followed by "C" once and "T" once.

This structure makes it easy to look up each k-mer and see all the characters that came after it, along with their counts.

---

## How Edge Cases Are Handled

### 1. The sequence is shorter than `k`
If the DNA sequence is too short to contain even one k-mer (for example, if the sequence is "AT" and `k = 5`), the program just returns an empty result. It doesn't crash or give an error.

### 2. The last k-mer has no next character
The program only includes k-mers that have a character following them. It uses:


for i in range(len(sequence) - k)


This stops the loop before it tries to look beyond the end of the sequence.

### 3. FASTA headers and multiple lines
FASTA files include lines that start with `>` to label the sequences. The program skips those lines. It also removes newline characters and joins all the sequence lines into one long string so that k-mers are formed correctly, even across lines.

---

## How Overcounting Is Avoided

The program goes through the DNA sequence one time, from left to right. At each position, it:
- Looks at the current k-mer
- Looks at the one character that comes after it
- Updates the counts accordingly

It never counts the same position twice, and it doesn’t accidentally count the final k-mer if there is no character after it.

---

## Why the Code Is Split into Functions

Each part of the program does one specific task. This makes the code easier to:
- Understand
- Test
- Reuse later

Here’s what each function does:

- `parse_fasta()`: Reads the input FASTA file, removes headers and newlines, and returns a clean DNA sequence.
- `extract_kmer_context()`: Builds the dictionary of k-mers and the characters that follow them.
- `format_kmer_data()`: Converts the dictionary into a list of text lines for writing to a file.
- `write_output()`: Saves the list of lines to the output file.
- `main()`: Connects all the pieces and handles command line input.

---

## Summary

- The program breaks up a DNA sequence into overlapping k-mers.
- It counts how often each one appears and what comes after it.
- It uses dictionaries to store everything in an organized way.
- It skips any invalid cases, like k-mers without a following character.
- The code is written clearly and divided into small functions that are easy to test.