#!/usr/bin/env python

import bioinfo
import argparse
import matplotlib.pyplot as plt
import numpy
import gzip

parser = argparse.ArgumentParser()
parser.add_argument('-br1', type=str, help='Biological read 1 file name', required=True)
parser.add_argument('-br2', type=str, help='Biological read 2 file name', required=True)
parser.add_argument('-ind1', type=str, help='Index 1 file name', required=True)
parser.add_argument('-ind2', type=str, help='Index 2 file name', required=True)
parser.add_argument('-k', type=str, help="text file with known indexes")
parser.add_argument('-o', type=str, help='Output file name', required=True)

args = parser.parse_args()

read1 = args.br1
read2 = args.br2
index1 = args.ind1
index2 = args.ind2
known_index_file = args.k
outfile = args.o

#------------------------------------------------------------------------------------------------------
                                            # Example from the file:
                                    # sample  group   treatment       index   index sequence
                                    # 1       2A      control B1      GTAGCGTA
                                    # 2       2B      control A5      CGATCGAT
                                    # 3       2B      control C1      GATCAAGG
                                    # 4       2C      mbnl    B9      AACAGCGA
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
#                                     Required dictionaries
#------------------------------------------------------------------------------------------------------
# keys(str): indexes from known_index_file; values(fh): filehandles made in make_fhs; tuples
extracted_index_dict = {}

# keys(str): ALL index sequences; values(int): count of reads that have that index sequence
readpair_counts = {}

#keys(str): MATCHED index sequences; values(int): count of reads that have that index sequence
# E.g. {'AAAA-AAAA' 4}
matched_indv_count_dict = {}

#keys(str): hopped index pair tuples; values(int): count of reads with that index pair
# E.g. {'AAAA-GGGG' 4}
hopped_pairs_dict = {}

#------------------------------------------------------------------------------------------------------
#                       Defining function to make file handles and write/open all 52 files
#------------------------------------------------------------------------------------------------------
# this function will return a 6-tuple 
def make_fhs(index:str):
    fh_R1 = open(f"{index}_R1.fq", 'a+')
    fh_R2 = open(f"{index}_R2.fq", 'a+')
    fh_lowqual_R1 = open(f'lowqual_R1.fq', 'a+')
    fh_lowqual_R2 = open(f'lowqual_R2.fq', 'a+')
    fh_hopped_R1 = open(f'hopped_R1.fq', 'a+')
    fh_hopped_R2 = open(f'hopped_R2.fq', 'a+')
    return fh_R1, fh_R2, fh_lowqual_R1, fh_lowqual_R2, fh_hopped_R1, fh_hopped_R2

#------------------------------------------------------------------------------------------------------
#                           Extract the indexes from the known index file
#------------------------------------------------------------------------------------------------------
with open(known_index_file, 'r') as fh:
    lines = fh.readlines()
    for line in lines[1:]:
        columns = line.strip().split('\t')
        if len(columns) >= 5 and columns[4]:  # Check if the index sequence is empty by requiring a length of 5 characters or more
            index_sequence = columns[4]
            # print(f"Processing index sequence: '{index_sequence}'")
            extracted_index_dict[index_sequence] = make_fhs(index_sequence)

# Print the keys in the dictionary
# print("Keys in extracted_index_dict:", extracted_index_dict.keys())

#------------------------------------------------------------------------------------------------------
#                                  Defining reverse complement function
#------------------------------------------------------------------------------------------------------
def rev_complement(sequence):
    complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C', 'N':'N'}
    return ''.join(complement[base] for base in sequence[::-1])

#------------------------------------------------------------------------------------------------------
#            Opening the fastq files and defining each line as a set of 4 (4 lines per record)
#------------------------------------------------------------------------------------------------------
# Initiating counts matched, low quality, and hopped index read-pairs
# Needs to be outside of the loop otherwise it'll print all three every time the algorithm reads a fastq record
matched_count = 0
lowqual_count = 0
hopped_count = 0


# need to have these files open in order to write to them
lowqual_R1 = open("lowqual_R1.fq", 'a+')
lowqual_R2 = open("lowqual_R2.fq", 'a+')
hopped_R1 = open("hopped_R1.fq", 'a+')
hopped_R2 = open("hopped_R2.fq", 'a+')

#with open(read1, 'rt') as r1, open(read2, 'rt') as r2, open(index1, 'rt') as ind1, open(index2, 'rt') as ind2:
with gzip.open(read1, 'rt') as r1, gzip.open(read2, 'rt') as r2, gzip.open(index1, 'rt') as ind1, gzip.open(index2, 'rt') as ind2:
# use gzip for files that are zipped, otherwise just use "with open"

    #Store all four lines of the first FASTQ record in memory 
    while True:
        R1_header=r1.readline().strip()
        R1_seq=r1.readline().strip()
        R1_plus=r1.readline().strip()
        R1_qualscore=r1.readline().strip()
       
        R2_header=r2.readline().strip()
        R2_seq=r2.readline().strip()
        R2_plus=r2.readline().strip()
        R2_qualscore=r2.readline().strip()

        Ind1_header=ind1.readline().strip()
        Ind1_seq=ind1.readline().strip()
        Ind1_plus=ind1.readline().strip()
        Ind1_qualscore=ind1.readline().strip()
        
        Ind2_header = ind2.readline().strip()
        Ind2_seq = rev_complement(ind2.readline().strip())
        Ind2_plus = ind2.readline().strip()
        Ind2_qualscore = ind2.readline().strip()

        # Convert Ind1_seq and Ind2_seq to strings if they are bytes
        Ind1_seq = Ind1_seq.decode() if isinstance(Ind1_seq, bytes) else Ind1_seq
        Ind2_seq = Ind2_seq.decode() if isinstance(Ind2_seq, bytes) else Ind2_seq
        Ind1_qualscore = Ind1_qualscore.decode() if isinstance(Ind1_qualscore, bytes) else Ind1_qualscore
        Ind2_qualscore = Ind2_qualscore.decode() if isinstance(Ind2_qualscore, bytes) else Ind2_qualscore

        # counting how many times and index occurs and storing it in the readpair_counts dict
        if Ind1_seq in readpair_counts:
            readpair_counts[Ind1_seq] += 1
        else:
            readpair_counts[Ind1_seq] = 1


        #print(seq)
        if R1_header == '' or R2_header == '' or Ind1_header == '' or Ind2_header == '':
            break
#------------------------------------------------------------------------------------------------------
#                              Distributing records to appropriate files
#------------------------------------------------------------------------------------------------------
        # Defining qual_score cutoffs
        avg_score_R1 = bioinfo.qual_score(Ind1_qualscore)
        avg_score_R2 = bioinfo.qual_score(Ind2_qualscore)
        score_cutoff = int(30)
        # print(avg_score_R1)
        # print(avg_score_R2)
        # Writing to lowqual files if index sequences contain ambiguous character, "N"
        if Ind1_seq not in extracted_index_dict or Ind2_seq not in extracted_index_dict: # if there is an ambiguous character in either of the "barcodes" i.e. indexes then...
            
            lowqual_R1.write(f"{R1_header} {Ind1_seq}-{Ind2_seq}\n{R1_seq}\n{R1_plus}\n{R1_qualscore}\n")
            lowqual_R2.write(f"{R2_header} {Ind1_seq}-{Ind2_seq}\n{R2_seq}\n{R2_plus}\n{R2_qualscore}\n")
            lowqual_count += 1

        # Writing to lowqual files if index quality scores are less than 30
        elif avg_score_R1 < score_cutoff or avg_score_R2 < score_cutoff:
            lowqual_R1.write(f"{R1_header} {Ind1_seq}-{Ind2_seq}\n{R1_seq}\n{R1_plus}\n{R1_qualscore}\n")
            lowqual_R2.write(f"{R2_header} {Ind1_seq}-{Ind2_seq}\n{R2_seq}\n{R2_plus}\n{R2_qualscore}\n")
            lowqual_count += 1

        # Writing to files for dual matched indexes
        elif Ind1_seq != Ind2_seq:
            hopped_R1.write(f"{R1_header} {Ind1_seq}-{Ind2_seq}\n{R1_seq}\n{R1_plus}\n{R1_qualscore}\n")
            hopped_R2.write(f"{R2_header} {Ind1_seq}-{Ind2_seq}\n{R2_seq}\n{R2_plus}\n{R2_qualscore}\n")
            hopped_count += 1

            #if Ind1_seq != Ind2_seq:
            hopped_index_pair = (Ind1_seq, Ind2_seq)
            hopped_pairs_dict[hopped_index_pair] = hopped_pairs_dict.get(hopped_index_pair, 0) + 1
            # print(hopped_pairs_dict)
        # Writing to files for index hopping
        else:
            extracted_index_dict[Ind1_seq][0].write(f"{R1_header} {Ind1_seq}-{Ind2_seq}\n{R1_seq}\n{R1_plus}\n{R1_qualscore}\n")
            extracted_index_dict[Ind1_seq][1].write(f"{R2_header} {Ind1_seq}-{Ind2_seq}\n{R2_seq}\n{R2_plus}\n{R2_qualscore}\n")
            matched_count += 1
            # from the extracted_index_dict, we need to call the "barcode" i.e. the index which is in the key of the dictionary
            # then, we need to call the value, which is a tuple containing all of the 6 filehandles we made in the make_fhs function
            # I want to access the 1st and 2nd elements in the value/tuple (tuple is 0 based; these elements are the biological reads), so we use 0 and 1, respectively

            # increase count in matched count dictionary to count how many times a known and matched index is read
            if Ind1_seq in matched_indv_count_dict:
                matched_indv_count_dict[Ind1_seq] += 1
            else:
                matched_indv_count_dict[Ind1_seq] = 1
        

#------------------------------------------------------------------------------------------------------
#                                         Data analysis
#------------------------------------------------------------------------------------------------------

# # Calculating percentage of read pairs from each index sequence
# total_readpairs = sum(readpair_counts.values())
# print(total_readpairs)

# with open('pct_read_pairs_each_index.txt', 'w') as out:
#     out.write('Percentage of read pairs from each index sequence:\n')
#     for index_seq, count in readpair_counts.items():
#         pct_reads = (count / total_readpairs) * 100
#         out.write(f'Index {index_seq}: {pct_reads:.2f}%\n')

# Calculate totals 
total_read_pairs = matched_count + hopped_count + lowqual_count  # Total number of read pairs
total_dual_matched = sum(count for index_seq, count in readpair_counts.items() if index_seq in extracted_index_dict) #total number of read pairs that were dual matched

print("Hopped index pairs and their counts:")
for index_pair, count in hopped_pairs_dict.items(): #index_pair refers to the tuple (key) and count refers to the number of times that pair occured (value)
    print(f"{index_pair[0]}-{index_pair[1]}:\t{count} read-pairs")


# Calculate percentage of each individual read pair 

with open('pct_count_read_pairs.tsv', 'w') as out:
    out.write('Percentage and Counts of read pairs from each index sequence (Dual Matched Read-Pairs only):\n')
    out.write(f"Index\t\tPercentage\tCount\n")
    for index_seq, count in readpair_counts.items():
        if index_seq in extracted_index_dict:
            pct_reads = (count / total_dual_matched) * 100
            out.write(f'{index_seq}\t{pct_reads:.2f}%\t\t{count}\n')

# Calculate the percentage of index hopped read pairs
pct_index_hopped = (hopped_count / total_read_pairs) * 100
print(f'Percentage of read pairs that showed index hopping: {pct_index_hopped:.2f}%')

# Calculate percentage of low quality reads
pct_low_quality = (lowqual_count / total_read_pairs) * 100
print(f'Percentage of low quality read pairs: {pct_low_quality:.2f}%')

# Calculate percentage of reads that were matched
pct_matched = (matched_count / total_read_pairs) * 100
print(f'Percentage of reads that were matched: {pct_matched:.2f}%')


print(f"Number of Dual Matched Read-Pairs: {matched_count}\nNumber of Index Hopped Read-Pairs: {hopped_count}\nNumber of Unknown/Low Quality Read-Pairs: {lowqual_count}")

# Creating a bar chart for read pair counts
categories = ['Index Hopping', 'Low Quality', 'Dual Matched']
counts = [hopped_count, lowqual_count, matched_count]

plt.bar(categories, counts)
plt.xlabel("Read Pair Category")
plt.ylabel("Number of Read Pairs")
plt.title("Number of Read Pairs by Category")
plt.tight_layout()
plt.savefig("read_pair_counts.png")
