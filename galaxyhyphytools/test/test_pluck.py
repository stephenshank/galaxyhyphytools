import os
import unittest

from galaxyhyphytools.pluck import pluck_io


class TestPluck(unittest.TestCase):

    def test_simple(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(base_path, 'data', 'simple.fasta')
        output_path = os.path.join(base_path, 'data', 'simple-plucked.fasta')
        pluck_io(
            input_path, output_path, 1, 4, 'plucked'
        )

if __name__ == '__main__':
    unittest.main()
