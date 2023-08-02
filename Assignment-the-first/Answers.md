# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | read1 | 101 | phred33+ |
| 1294_S1_L008_R2_001.fastq.gz | index1 | 8 | phred33+ |
| 1294_S1_L008_R3_001.fastq.gz | index2 | 8 | phred33+ |
| 1294_S1_L008_R4_001.fastq.gz | read2 | 101 | phred33+ |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.

    2. [R1 chart](https://github.com/leycufur/Demultiplex/blob/master/Assignment-the-first/R1_results.png)
    3. [R2 chart](https://github.com/leycufur/Demultiplex/blob/master/Assignment-the-first/R2_results.png)
    4. [R3 chart](https://github.com/leycufur/Demultiplex/blob/master/Assignment-the-first/R3_results.png)
    5. [R4 chart](https://github.com/leycufur/Demultiplex/blob/master/Assignment-the-first/R4_results.png)

```
***** R2 and R3 charts are updated to the correct mean values.
***** R1 and R4 will be /projects/bgmp/leylacuf/bioinfo/Bi622/R1_results.png and /projects/bgmp/leylacuf/bioinfo/Bi622/R4_results.png respectively 
```

3. What is a good quality score cutoff for index reads and biological read pairs to utilize for sample identification and downstream analysis, respectively? Justify your answer.
    ```A good quality score cutoff for the index and biological reads is 30. I chose to do 30 because, looking at the charts, most of the data falls at or around 30. I think that anything below 30 would result in less quality data and anything above 30 would eliminate a majority of the good data.```


4. How many indexes have undetermined (N) base calls? (Utilize your command line tool knowledge. Submit the command(s) you used. CHALLENGE: use a one-line command)
    ```zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | grep -v "^@" | grep -v "^+$" | grep "N" | wc -l```

```3976613```
    
    ```zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | grep -v "^@" | grep -v "^+$" | gr
ep "N" | wc -l```

```3328051```
## Part 2
1. Define the problem

```Reads are multiplexed and need to be demultiplexed e.g. decoded and need to report amount of index hopping```

2. Describe output

```Output should be 48 fastq files named with acceptable index pairs that contain all the reads for forward (24 files) and reverse reads (24 files). Another 2 files will have all the index hopped reads for forward and reverse reads, and a final 2 files that have reads with unknown indexes that either do not match the known indexes or do not pass the quality score threshold.```


3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement

```
def reverse_complement
	"This function takes a DNA string and reurns the reverse complement"
	return reverse complement
example input: 'ATCG'
example output: 'CGAT'	

def demultiplex_reads
    "this function uses approximately maybe 900 if statements and some loops to take multiplexed sequences and their indexes and demultiplex them and store them in a dictionary."
    return matched read pairs, index hopped read pairs, unknown read pairs, and their counts
example input: read1, index1, index2, read2
example output: "matched read pairs:" [list of matched reads]
                "index hopped pairs:" [list of index hopped reads]
                "unknown pairs:" [list of unknown reads]
                "matched read pairs:" (int) number of matched reads
                "index hopped pairs:" (int) number of hopped reads
                "unknown pairs:" (int) number of unknown reads
```
