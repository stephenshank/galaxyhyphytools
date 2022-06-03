import re

from Bio import SeqIO


def fasta_filter(fasta, id_regex):
    prog = re.compile(id_regex)
    return (record for record in fasta if prog.match(record.id))


def fasta_filter_io(input_fasta_path, output_fasta_path, id_regex):
    original_fasta = SeqIO.parse(input_fasta_path, 'fasta')
    filtered_fasta = fastafilter(original_fasta, id_regex)
    SeqIO.write(filtered_fasta, output_fasta_path, 'fasta')
