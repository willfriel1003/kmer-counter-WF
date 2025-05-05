# Genome K-mer Counter

This project is a Python program that reads a DNA sequence from a FASTA file and finds all the k-mers (substrings of length `k`) in that sequence. For each k-mer, it also keeps track of how often each letter (A, C, G, or T) appears right after it in the sequence.

This kind of analysis is useful in bioinformatics when researchers try to piece together full genomes from smaller fragments.

---

## What Is a k-mer?

A k-mer is just a short substring from a longer DNA sequence. For example, if your sequence is:

ATGCA

and `k = 2`, the 2-mers are:

AT, TG, GC, CA

Each of these 2-mers is followed by the next letter in the sequence. For example:
- "AT" is followed by "G"
- "TG" is followed by "C"
- "GC" is followed by "A"

This program records:
1. How many times each k-mer appears
2. What character(s) follow each k-mer, and how often

---

## How to Run the Program

### Step 1 – Make sure you have Python installed

To check if Python is installed, run this command in your terminal:

python --version

You should see something like `Python 3.x.x`.

### Step 2 – Run the program

To run the program, use the following format in your terminal:

python main.py reads.fa 3 output.txt


- `reads.fa` is the input FASTA file containing the DNA sequences
- `3` is the value of `k` (you can change it to any positive number)
- `output.txt` is the file where the results will be saved

---

## Example Output

If the sequence is `ATGCAT` and `k = 2`, the output might look like this:

AT: total 2
G: 1
T: 1
TG: total 1
C: 1
GC: total 1
A: 1
CA: total 1
T: 1


Each k-mer is shown with:
- Its total number of occurrences
- Each character that followed it, and how many times

---

## How to Run the Tests

This project includes tests to make sure each function works correctly. The tests use a tool called `pytest`.


### Step 1 – Install pytest

Run this command in your terminal:

pip install pytest


### Step 2 – Run the tests

Once `pytest` is installed, run this command from the root folder of your project:

pytest


This will run the test file located at `tests/test_main.py` and tell you if everything is working.

---

## Project Files

Here's what each file in this project does:

- `main.py`: The main program that reads the DNA, counts k-mers, and saves the results
- `tests/test_main.py`: Test file that checks the functions in `main.py`
- `reads.fa`: The input FASTA file (provided)
- `output.txt`: The file your program creates to store the results
- `README.md`: This instruction file
- `docs/EXPLANATION.md`: A write-up explaining how the code works and what design choices were made
- `requirements.txt`: Lists `pytest` as a requirement for testing
- `.gitignore`: Keeps unnecessary or temporary files out of version control

---