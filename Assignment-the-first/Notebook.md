
                              ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
                                    ୨⎯ Bash commands for data exploration ⎯୧
                              ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	First I decided to "head" each file to see what they all looked like. Looks like they are all fastq files and all have the same headers except for the tabbed over section e.g. "1:N:0:1". The files are named differently as follows: 1:N:0:1, 2:N:0:1, 3:N:0:1, 4:N:0:1, respectively. 




	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Command ⇙
	╚═════════════╝

	$ zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz | head

	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Output ⇙
	╚═════════════╝

	@K00337:83:HJKJNBBXX:8:1101:1265:1191 1:N:0:1
	GNCTGGCATTCCCAGAGACATCAGTACCCAGTTGGTTCAGACAGTTCCTCTATTGGTTGACAAGGTCTTCATTTCTAGTGATATCAACACGGTGTCTACAA
	+
	A#A-<FJJJ<JJJJJJJJJJJJJJJJJFJJJJFFJJFJJJAJJJJ-AJJJJJJJFFJJJJJJFFA-7<AJJJFFAJJJJJF<F--JJJJJJF-A-F7JJJJ
	@K00337:83:HJKJNBBXX:8:1101:1286:1191 1:N:0:1
	CNACCTGTCCCCAGCTCACAGGACAGCACACCAAAGGCGGCAACCCACACCCAGTTTTACAGCCACACAGTGCCTTGTTTTACTTGAGGACCCCCCACTCC
	+
	A#AAFJJJJJJJJJJFJJJJJJJJJJJJJJJJJJJJJJJJFJJJJJJJJJJJJJJAJJJJJJJJJJJJJJFJJJJJFFFFJJJJJJJJJJJJJJJJJJ77F
	@K00337:83:HJKJNBBXX:8:1101:1347:1191 1:N:0:1
	GNGGTCTTCTACCTTTCTCTTCTTTTTTGGAGGAGTAGAATGTTGAGAGTCAGCAGTAGCCTCATCATCACTAGATGGCATTTCTTCTGAGCAAAACAGGT




	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Command ⇙
	╚═════════════╝

	$ zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | head


	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Output ⇙
	╚═════════════╝

	@K00337:83:HJKJNBBXX:8:1101:1265:1191 2:N:0:1
	NCTTCGAC
	+
	#AA<FJJJ
	@K00337:83:HJKJNBBXX:8:1101:1286:1191 2:N:0:1
	NACAGCGA
	+
	#AAAFJJJ
	@K00337:83:HJKJNBBXX:8:1101:1347:1191 2:N:0:1
	NTCCTAAG


	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Command ⇙
	╚═════════════╝
	$ zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | head

	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Output ⇙
	╚═════════════╝


	@K00337:83:HJKJNBBXX:8:1101:1265:1191 3:N:0:1
	NTCGAAGA
	+
	#AAAAJJF
	@K00337:83:HJKJNBBXX:8:1101:1286:1191 3:N:0:1
	NCGCTGTT
	+
	#AAAFJ-A
	@K00337:83:HJKJNBBXX:8:1101:1347:1191 3:N:0:1
	NTTAGGAC


	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Command ⇙
	╚═════════════╝
	$ zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz | head```



	╔══ ≪ °❈° ≫ ══╗
	  ⇘ Output ⇙
	╚═════════════╝


	@K00337:83:HJKJNBBXX:8:1101:1265:1191 4:N:0:1
	NTTTTGATTTACCTTTCAGCCAATGAGAAGGCCGTTCATGCAGACTTTTTTAATGATTTTGAAGACCTTTTTGATGATGATGATGTCCAGTGAGGCCTCCC
	+
	#AAFAFJJ-----F---7-<FA-F<AFFA-JJJ77<FJFJFJJJJJJJJJJAFJFFAJJJJJJJJFJF7-AFFJJ7F7JFJJFJ7FFF--A<A7<-A-7--
	@K00337:83:HJKJNBBXX:8:1101:1286:1191 4:N:0:1
	NTGTGTAGACAAAAGTTTTCATGAGTCTGTAAGCTGTCTATTGTCTCCTGAAAAGAAACCAGAAGTTTTCCCCTAAATGTGTTTAGAATGCTTATTCTAAT
	+
	#A-AFFJJFJJJJJJJJJJJJJJJJ<JAJFJJJJF<JFJJJAJJJJJJJJJJJJJJJJJJJFJJJAJJFJJJFJJJF<JJA-JJJ-<AFAF--FF<JAFJF
	@K00337:83:HJKJNBBXX:8:1101:1347:1191 4:N:0:1
	NAAATGCCATCTAGTGATGATGAGGCTACTGCTGACTCTCAACATTCTACTCCTCCAAAAAAGAAGAGAAAGATTCCAACCCCCAGAACCGATGACCGGCA




						▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
						୨⎯ Determine the length of the reads in each file ⎯୧
						▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	[1]   Running                 zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz | head -2 | grep -v "^@" | wc -L &
	[2]   Running                 zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | head -2 | grep -v "^@" | wc -L & #[1] 265026
	[3]   Running                 zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz |  head -2 | grep -v "^@" | wc -L & #[2] 2650265
	[4]-  Running                 zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz |  head -2 | grep -v "^@" | wc -L & #2648101
	[5]+  Running                 zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz |  head -2 | grep -v "^@" | wc -L & #2648156

	✧ All files have the same number of lines: 1452986940
	✧ R1 and R4 have read length of 101bps and R2 and R3 have length of 8bps
	✧ The phred encoding for this data is Phred33 encoding. I can determine this by looking at the phred scores in some of the data files and calculating the phred scores, either phred33 or phred64. I can use a lower score and subtract either 33 or 64 from it and if the quality score is a negative number, then I know to use phred33.

                                           

                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
                                                    ୨⎯ Submitting job to scheduler⎯୧
                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	(bgmp_py311) [leylacuf@n0187 Bi622]$ squeue -u leylacuf
				JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
				23910   compute run_demu leylacuf  R       1:17      1 n0187
				23908   compute run_demu leylacuf  R       2:17      1 n0187
				23907   compute run_demu leylacuf  R       4:17      1 n0187
				23906   compute run_demu leylacuf  R       5:32      1 n0187
				23886   compute     bash leylacuf  R      20:17      1 n0187
		✧ 07 is R2
		✧ 06 is R3
		✧ 08 is R1
		✧ 10 is R4



                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
                                                            ୨⎯ R1 run info ⎯୧
                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	Command being timed: "python /projects/bgmp/leylacuf/bioinfo/Bi622/Demultiplexing_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -o R1_results -l 101"
	User time (seconds): 5515.59
	System time (seconds): 8.66
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 1:32:21
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 66824
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 72235
	Voluntary context switches: 60
	Involuntary context switches: 1650
	Swaps: 0
	File system inputs: 0
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0




                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
                                                            ୨⎯ R2 run info ⎯୧
                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	Command being timed: "python /projects/bgmp/leylacuf/bioinfo/Bi622/Demultiplexing_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -o R2_results -l 8"
	User time (seconds): 745.21
	System time (seconds): 1.92
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 12:28.80
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 63156
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 35543
	Voluntary context switches: 32
	Involuntary context switches: 190108
	Swaps: 0
	File system inputs: 0
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0





                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
                                                            ୨⎯ R3 run info ⎯୧
                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	Command being timed: "python /projects/bgmp/leylacuf/bioinfo/Bi622/Demultiplexing_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -o R3_results -l 8"
	User time (seconds): 749.36
	System time (seconds): 1.74
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 12:34.87
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 74360
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 42021
	Voluntary context switches: 135
	Involuntary context switches: 187825
	Swaps: 0
	File system inputs: 0
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0





                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄
                                                            ୨⎯ R4 run info ⎯୧
                                        ▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄▄▀▄▀▄▀▄▀▄▀▄

	Command being timed: "python /projects/bgmp/leylacuf/bioinfo/Bi622/Demultiplexing_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -o R4_results -l 101"
	User time (seconds): 5543.29
	System time (seconds): 10.21
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 1:32:54
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 66932
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 86323
	Voluntary context switches: 894
	Involuntary context switches: 2812
	Swaps: 0
	File system inputs: 0
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0


```All output charts look good to me-- looks like the script worked as it should have :)```