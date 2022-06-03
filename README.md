# galaxyhyphytools

A few bioinformatics utilities used on galaxy.hyphy.org.

Experimental library at the moment... use at your own risk!

## Installation

### Setuptools

Coming soon to pip/PyPI.

```
git clone https://github.com/stephenshank/galaxyhyphytools
cd galaxyhyphytools
python setup.py install
```

### conda

Coming soon to bioconda.

```
conda install -c stephenshank galaxyhyphytools
```

## Usage

### pluck

Plucks a region from a given FASTA file. Given input fasta with a **single** record:

####input.fasta
```
>input
ACGTACGT
```

run

```
ght pluck -i input.fasta -o plucked.fasta -s 1 -S 4 -d plucked
```

to obtain

#### output.fasta
```
>input plucked
CGT
```

See `ght pluck --help`.

### hstack

Horizontally stack/concatenate existing multiple sequence alignments. Given input fasta files

#### first.fasta
```
>record1
ACGTACGT
>record2
GCGCGCGC
>record3
AAAAAAAA
```

#### second.fasta
```
>record1
ACGTACGT
>record1
ATATATAT
>record3
CCCCCCCC
```

run

```
ght hstack -o stacked.fasta -d stacked -i first.fasta second.fasta
```

to obtain

#### stacked.fasta
```
>record1 stacked
ACGTACGTACGTACGT
>record2 stacked
GCGCGCGCATATATAT
>record3 stacked
AAAAAAAACCCCCCCC
```

See `ght hstack --help`.

### fastafilter

Filter a FASTA file according to various conditions. At present only a regex on the ID is supported. Given:

### input.fasta
```
>B.1999
ACGTACGTACGTACGT
>C.2002
GCGCGCGCATATATAT
>B.2003
AAAAAAAACCCCCCCC
>B.2004
CCCCCCCCCCCCCCCC
>G.2007
AAAAAAAAAAAAAAAA
```

run

```
ght fastafilter -i input.fasta -o filtered.fasta -I ^B\.'
```

to obtain

### filtered.fasta
```
>B.1999
ACGTACGTACGTACGT
>B.2003
AAAAAAAACCCCCCCC
>B.2004
CCCCCCCCCCCCCCCC
```

See `ght fastafilter --help`.