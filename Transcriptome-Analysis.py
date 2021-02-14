"""

A Brief Overview of My Workflow

Downloaded E.coli RNAseq Reads from SRA
Downloaded E.coli Reference genome from SRA

1. fasterq-dump to change from sra format to fastq 

2. fastqc quality control step

3. bbduk to trim adapters

4. fastqc to double check step 3

5. BWA to align reads to the reference genome

6. Samtools to convert and sort to gtf format

7. Stringtie to assemble and quantify

8. Cuffdiff for differential expression analysis

de novo

5a. 

6a. Samtools to convert and sort to gtf format

7a. Stringtie to assemble and quantify

8a. Cuffdiff for differential expression analysis



"""
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742321/

#Analysis of Whole Transcriptome Sequencing Data: Workflow and Software
# In Seok Yang and Sangwoo Kim
'''
Routine RNA-seq workflow may consist of the following five steps as shown in Fig. 1:
 
  (1) preprocessing of raw data, 
      Raw data QC: FASTQC
      Read trimming: FASTX-Toolkit
  (2) read alignment,
      Unspliced Aligners: BWA, Bowtie. 
      Spliced Aligners: TopHat
  (3) transcriptome reconstruction, 
      Reference Guided: Cufflinks, Scriptome
      Reference Independent: Trinity, Oases
  (4) expression quantification, 
      Gene-level: ALEXA-seq, ERANGE
      Inform-level: Cufflinks, Stringtie, Sailfish, 
  (5) differential expression analysis. 
      Gene-level: NOIseq, EdgeR, DESeq, 
      Isoform-level: Cuffdiff, EBSeq, Ballgown
  
  As an initial step, RNA-seq data may be subjected to quality control (QC) of the raw data before data analysis.
  Similar to whole genome or exome sequencing, read alignment can be performed to map the reads to the reference genome or transcriptome. 
  Clinical samples including formalin-fixed paraffin-embedded specimen and cancer tissue biopsies are often degraded or exist in limited amount [6]. 
  Thus additional QC procedure can be performed to evaluate the performance of the RNA-seq experiment itself after read alignment. 
  Next, transcriptome reconstruction is carried out to identify all transcripts expressed in a specimen based on read mapping data. 
  If there is no available reference sequence, this procedure can be conducted directly using a de novo assembly approach. 
  Once all transcripts are identified, their abundances can be estimated using read mapping data.
  Finally, differential expression analysis is conducted using currently available programs. 
  In this review, we discuss the RNA-seq workflow and its related bioinformatics tools in each step (Table 1), focusing on transcriptome reconstruction and abundance 
  quantification.
'''

