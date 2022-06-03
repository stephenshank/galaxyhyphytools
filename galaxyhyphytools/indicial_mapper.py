import json

import numpy as np
from Bio import SeqIO


def indicial_mapper(fasta):
    fasta_np = np.array([list(str(record.seq)) for record in fasta], dtype='<U1')
    non_gaps_in_reference = fasta_np[0, :] != '-'
    sites_in_alignment = fasta_np.shape[1]
    indicial_map = np.arange(sites_in_alignment)[non_gaps_in_reference]
    return indicial_map


def indicial_mapper_io(input_fasta_path, output_json_path):
    fasta = SeqIO.parse(input_fasta_path, 'fasta')
    indicial_map = indicial_mapper(fasta)
    with open(output_json_path, 'w') as json_file:
        json.dump([int(i) for i in indicial_map], json_file)
