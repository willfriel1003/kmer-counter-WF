#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def parse_fasta(filename):
    """
    This function reads a FASTA file and returns the DNA sequence as one string.
    It skips any lines that start with '>' because those are just headers.
    """
    sequence = ""
    with open(filename, 'r') as file:
        for line in file:
            # Skip header lines
            if not line.startswith('>'):
                # Remove newline characters and make all letters uppercase
                cleaned_line = line.strip().upper()
                sequence = sequence + cleaned_line
    return sequence

def extract_kmer_context(sequence, k):
    """
    This function finds every k-mer in the sequence and counts what characters come after it.
    It returns a dictionary where each k-mer maps to another dictionary of next characters.
    Example:
      {
        'AT': {'G': 2},
        'TG': {'C': 1, 'T': 1}
      }
    """
    kmer_counts = {}

    # Go through the sequence and collect k-mers and their next characters
    for i in range(len(sequence) - k):
        kmer = sequence[i:i+k]            # The k-mer
        next_char = sequence[i+k]         # The character that comes right after

        # If the k-mer is not in the dictionary yet, add it
        if kmer not in kmer_counts:
            kmer_counts[kmer] = {}

        # If the next character is not counted yet for this k-mer, add it
        if next_char not in kmer_counts[kmer]:
            kmer_counts[kmer][next_char] = 0

        # Add 1 to the count for this next character
        kmer_counts[kmer][next_char] = kmer_counts[kmer][next_char] + 1

    return kmer_counts

def format_kmer_data(kmer_counts):
    """
    This function turns the k-mer dictionary into a list of strings that can be written to a file.
    Each k-mer and its counts are written on separate lines.
    """
    output_lines = []

    # Go through each k-mer in alphabetical order
    for kmer in sorted(kmer_counts.keys()):
        # Count the total times the k-mer appears
        total = 0
        for char in kmer_counts[kmer]:
            total = total + kmer_counts[kmer][char]

        output_lines.append(kmer + ": total " + str(total))

        # Go through each next character and add it
        for char in sorted(kmer_counts[kmer].keys()):
            count = kmer_counts[kmer][char]
            output_lines.append("  " + char + ": " + str(count))

    return output_lines

def write_output(lines, output_filename):
    """
    This function writes the lines to an output file, one line at a time.
    """
    with open(output_filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    """
    This is the main function that gets called when the script runs.
    It uses the command line to get:
      - the input filename
      - the value of k
      - the output filename
    Then it calls the other functions to process the data.
    """
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_file> <k> <output_file>")
        sys.exit()

    input_file = sys.argv[1]
    k_value = int(sys.argv[2])
    output_file = sys.argv[3]

    # Step 1: Read the DNA sequence
    full_sequence = parse_fasta(input_file)

    # Step 2: Get the k-mer counts
    kmer_data = extract_kmer_context(full_sequence, k_value)

    # Step 3: Format the results
    output_lines = format_kmer_data(kmer_data)

    # Step 4: Save the output to a file
    write_output(output_lines, output_file)

# Only run main() if this script is being run directly
if __name__ == "__main__":
    main()

