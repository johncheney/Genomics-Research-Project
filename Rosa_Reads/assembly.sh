#!bin/bash/

#fastqc "$1, $2"  

#bbduk.sh -Xmx24g in1="$1" in2="$2" out1="$1"_clean1.fastq out2="$2"_clean2.fastq ref=adapters ktrim=r k=23 mink=11 hdist=1 tpe tbo

#fastqc *_clean1.fastq *_clean2.fastq 

mkdir spades_output

spades.py -o spades_output -1 *_clean1.fastq -2 *_clean2.fastq
