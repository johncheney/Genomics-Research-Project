
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742321/

Routine RNA-seq workflow may consist of the following five steps as shown in Fig. 
1: (1) preprocessing of raw data, 
  (2) read alignment,
  (3) transcriptome reconstruction, 
  (4) expression quantification, and 
  (5) differential expression analysis. 
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
