#!/usr/bin/env python

import os
import sys

def splitfasta(input_file, output_dir):
    outputs = {}

    while True:
        description = input_file.readline()
        if not len(description):
            return
        sequence = input_file.readline()
        if not len(sequence):
            return

        assert description.startswith('>'), 'Error: Incomplete format'
        id = description[1:].split()[0]
        assert '_' in id, 'Error: Input fasta file must be processed by split_libraries.py'

        id = id[:id.rfind('_')]
        if id not in outputs:
            outputs[id] = open(os.path.join(output_dir, id + '.fasta'), 'w')

        outputs[id].write(description)
        outputs[id].write(sequence)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s [input fasta file] [output directory]')
        sys.exit()

    if not os.path.exists(sys.argv[2]):
        os.mkdir(sys.argv[2])
    elif os.path.isfile(sys.argv[2]):
        print('Error: %s already exists' % sys.argv[2])
        sys.exit()

    with open(sys.argv[1], 'r') as f:
        splitfasta(f, sys.argv[2])
