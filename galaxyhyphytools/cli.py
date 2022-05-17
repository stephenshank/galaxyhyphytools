import sys
import argparse

from .pluck import pluck_io
from .hstack import hstack_io
from .fastafilter import fastafilter_io


DESCRIPTION = '''
galaxyhyphytools - A few bioinformatics utilities used on galaxy.hyphy.org
Written by Stephen D. Shank, Ph. D.
Acme Computational Molecular Evolution Group - http://lab.hyphy.org/
https://github.com/stephenshank/galaxyhyphytools

'''


def command_line_interface():
    'Full command line interface function.'

    if len(sys.argv) == 1:
        print(DESCRIPTION)
        print('For a list of subcommands: ght -h or ght --help')
        print('For help with a subcommand: ght subcommand -h')
        print('                        or: ght subcommand --help\n')
        sys.exit(0)

    main_parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = main_parser.add_subparsers()

    pluck_description = '''
        Pluck/trim an individual sequence in a FASTA file to a specified region.
    '''
    pluck_subparser = subparsers.add_parser(
        'pluck', description=pluck_description
    )
    pluck_subparser.set_defaults(func=pluck_cli)
    pluck_subparser.add_argument(
        '-i', '--input', help='input FASTA file', dest='input', required=True
    )
    pluck_subparser.add_argument(
        '-o', '--output', help='output FASTA file', dest='output', required=True
    )
    pluck_subparser.add_argument(
        '-s',
        '--start',
        help='zero-based start index, inclusive',
        dest='start',
        type=int
    )
    pluck_subparser.add_argument(
        '-S',
        '--stop',
        help='zero-based stop index, exclusive',
        dest='stop',
        type=int
    )
    pluck_subparser.add_argument(
        '-d',
        '--description',
        help='modify description of output',
        dest='description'
    )

    hstack_description = '''
        Horizontally stack/concatenate several multiple sequence alignments.
    '''
    hstack_subparser = subparsers.add_parser(
        'hstack', description=hstack_description
    )
    hstack_subparser.set_defaults(func=hstack_cli)
    hstack_subparser.add_argument(
        '-o', '--output', help='output FASTA file', dest='output', required=True
    )
    hstack_subparser.add_argument(
        '-d',
        '--description',
        help='modify description of output',
        dest='description'
    )
    hstack_subparser.add_argument(
        '-i',
        '--input',
        nargs='+',
        help='input FASTA files',
        dest='input',
        required=True
    )

    fastafilter_description = '''
        Filter a FASTA file according to various conditions.
    '''
    fastafilter_subparser = subparsers.add_parser(
        'fastafilter', description=fastafilter_description
    )
    fastafilter_subparser.set_defaults(func=fastafilter_cli)
    fastafilter_subparser.add_argument(
        '-i',
        '--input',
        help='input FASTA files',
        dest='input',
        required=True
    )
    fastafilter_subparser.add_argument(
        '-o', '--output', help='output FASTA file', dest='output', required=True
    )
    fastafilter_subparser.add_argument(
        '-I',
        '--id-regex',
        help='regular expression for IDs, keeping those that match',
        dest='idregex'
    )
    args = main_parser.parse_args()
    args.func(args)


def pluck_cli(args):
    'Command line interface for pluck.'
    pluck_io(
        args.input, args.output, args.start, args.stop, args.description
    )


def hstack_cli(args):
    'Command line interface for hstack.'
    hstack_io(
        args.input, args.output, args.description
    )


def fastafilter_cli(args):
    'Command line interface for fastafilter.'
    fastafilter_io(
        args.input, args.output, args.idregex
    )


if __name__ == '__main__':
    command_line_interface()

