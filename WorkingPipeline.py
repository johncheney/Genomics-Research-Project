# Pipeline for genome assembly from raw SRA reads, annotation and genome statistics. 


# Step 1
# Obtain raw SRA reads 
# https://www.ncbi.nlm.nih.gov/sra/docs/sradownload/
# 

#prefetch - downloads runs in compressed SRA format 
#fasterq-dump changes compressed SRA format to fasta

# prefetch SRR13401411 (downloads drosphilla genome to SRA directory)

"""johncheney@Johns-MBP-4 SRA % prefetch SRR13401411

2021-01-24T13:38:12 prefetch.2.10.9: 1) Downloading 'SRR13401411'...
2021-01-24T13:38:12 prefetch.2.10.9:  Downloading via HTTPS...
2021-01-24T14:00:18 prefetch.2.10.9:  HTTPS download succeed
2021-01-24T14:00:19 prefetch.2.10.9:  'SRR13401411' is valid
2021-01-24T14:00:19 prefetch.2.10.9: 1) 'SRR13401411' was downloaded successfully
2021-01-24T14:00:19 prefetch.2.10.9: 'SRR13401411' has 0 unresolved dependencies
johncheney@Johns-MBP-4 SRA %  fasterq-dump SRR13401411 
spots read      : 9,959,292
reads read      : 19,918,584
reads written   : 9,959,292
reads 0-length  : 9,959,292
johncheney@Johns-MBP-4 SRA %      """



# Step 2
# Inital quality testing with fastqc / multiqc 
# How many reads are available? Do they represent the genome? Are there adapters Present? 
#https://www.bioinformatics.babraham.ac.uk/projects/download.html <- to download fastqc software 

""" johncheney@Johns-MBP-4 SRA % fastqc SRR13401411.fastq
Started analysis of SRR13401411.fastq
Approx 5% complete for SRR13401411.fastq
Approx 10% complete for SRR13401411.fastq
Approx 15% complete for SRR13401411.fastq
Approx 20% complete for SRR13401411.fastq
Approx 25% complete for SRR13401411.fastq
Approx 30% complete for SRR13401411.fastq
Approx 35% complete for SRR13401411.fastq
Approx 40% complete for SRR13401411.fastq
Approx 45% complete for SRR13401411.fastq
Approx 50% complete for SRR13401411.fastq
Approx 55% complete for SRR13401411.fastq
Approx 60% complete for SRR13401411.fastq
Approx 65% complete for SRR13401411.fastq
Approx 70% complete for SRR13401411.fastq
Approx 75% complete for SRR13401411.fastq
Approx 80% complete for SRR13401411.fastq
Approx 85% complete for SRR13401411.fastq
Approx 90% complete for SRR13401411.fastq
Approx 95% complete for SRR13401411.fastq
Analysis complete for SRR13401411.fastq
johncheney@Johns-MBP-4 SRA % ls
SRR13401411		SRR13401411_fastqc.zip	refseq
SRR13401411.fastq	files			sra
SRR13401411_fastqc.html	nannot			wgs
johncheney@Johns-MBP-4 SRA % open SRR13401411_fastqc.html """


# Step 3 
# Trim adapters/ filter data etc with Trimmomatic? BBduk? 
#Erroneous seqs and adapters are removed before assembly
#https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/bbduk-guide/



# Step 4 
# Sequence Assembly (SPAdes)
# Reads assembled into contigs
#https://github.com/ablab/spades←to download SPAdes soft





""" FASTQC PIPELINE INFO

Running FastQC as part of a pipeline
------------------------------------
To run FastQC non-interactively you should use the fastqc wrapper script to launch
the program.  You will probably want to use the zipped install file on every platform
(even OSX).

To run non-interactively you simply have to specify a list of files to process
on the commandline

fastqc somefile.txt someotherfile.txt

You can specify as many files to process in a single run as you like.  If you don't
specify any files to process the program will try to open the interactive application
which may result in an error if you're running in a non-graphical environment.

There are a few extra options you can specify when running non-interactively.  Full
details of these can be found by running 

fastqc --help

By default, in non-interactive mode FastQC will create an HTML report with embedded
graphs, but also a zip file containing individual graph files and additional data files
containing the raw data from which plots were drawn.  The zip file will not be extracted
by default but you can enable this by adding:

--extract

To the launch command.

If you want to save your reports in a folder other than the folder which contained
your original FastQ files then you can specify an alternative location by setting a
--outdir value:

--outdir=/some/other/dir/

If you want to run fastqc on a stream of data to be read from standard input then you
can do this by specifing 'stdin' as the name of the file to be processed and then 
streaming uncompressed fastq format data to the program.  For example:

zcat *fastq.gz | fastqc stdin

If you want the results from a streamed analysis sent to a file with a name other than
stdin then you can add a colon and put the file name you want, for example:

zcat *fastq.gz | fastqc stdin:my_results

..would write results to my_result.html and my_results.zip.


Customising the report output
-----------------------------

If you want to run FastQC as part of a sequencing pipeline you may wish to change the
formatting of the report to add in your own branding or to include extra information.

In the Templates directory you will find a file called 'header_template.html' which
you can edit to change the look of the report.  This file contains all of the header for
the report file, including the CSS section and you can alter this however you see fit.

Whilst you can make whatever changes you like you should probably leave in place the
<div> structure of the html template since later code will expect to close the main div
which is left open at the end of the header.  There is no facility to change the code in
the main body of the report or the footer (although you can of course change the styling).

The text tags @@FILENAME@@ and @@DATE@@ are placeholders which are filled in when the
report it created.  You can use these placeholders in other parts of the header if you
wish."""
