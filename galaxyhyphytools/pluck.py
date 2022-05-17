from Bio import SeqIO


def pluck(record, start, stop, description):
    record.seq = record.seq[start:stop]
    record.description = description
    return record


def pluck_io(input_fasta_path, output_fasta_path, start, stop, description):
    original_record = SeqIO.read(input_fasta_path, 'fasta')
    plucked_record = pluck(original_record, start, stop, description)
    SeqIO.write(plucked_record, output_fasta_path, 'fasta')
