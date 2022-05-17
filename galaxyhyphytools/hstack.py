from Bio import SeqIO


def hstack(alignments, description):
    for record in alignments[0]:
        record.description = description
        for other_alignment in alignments[1:]:
            other_record = next(other_alignment)
            record.seq = record.seq + other_record.seq
        yield record


def hstack_io(input_alignment_paths, output_alignment_path, description):
    alignments = [
        SeqIO.parse(input_alignment_path, 'fasta')
        for input_alignment_path in input_alignment_paths
    ]
    stacked_alignment = hstack(alignments, description)
    SeqIO.write(stacked_alignment, output_alignment_path, 'fasta')
