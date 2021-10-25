import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import argparse
from util.chromosomeRearrangementPainting import plotChrsRearrangement


def main():
    """
    Chrs Paint
    """

    parser = argparse.ArgumentParser(description="IAGS Chrs Paint")
    parser.add_argument("-c", "--config_file")

    args = parser.parse_args()
    config_file = args.config_file

    block_length_file = ''
    rearranged_species_block_file = ''
    rearranged_species_name = ''
    rearranged_species_copy_number = 0
    target_species_block_file = ''
    target_species_name = ''
    target_species_copy_number = 0
    colorlist = []
    outdir = ''
    with open(config_file,'r') as cf:
        while True:
            line = cf.readline()[:-1]
            if not line:
                break
            if line.startswith('BlockLength:'):
                line = cf.readline()[:-1]
                block_length_file = line
            elif line.startswith('RearrangedSpecies:'):
                line = cf.readline()[:-1]
                rearranged_species_block_file = line
            elif line.startswith('RearrangedSpeciesName:'):
                line = cf.readline()[:-1]
                rearranged_species_name = line
            elif line.startswith('RearrangedSpeciesCopyNumber:'):
                line = cf.readline()[:-1]
                rearranged_species_copy_number = int(line)
            elif line.startswith('TargetSpecies:'):
                line = cf.readline()[:-1]
                target_species_block_file = line
            elif line.startswith('TargetSpeciesName:'):
                line = cf.readline()[:-1]
                target_species_name = line
            elif line.startswith('TargetSpeciesCopyNumber:'):
                line = cf.readline()[:-1]
                target_species_copy_number = int(line)
            elif line.startswith('ColorList:'):
                while True:
                    line = cf.readline()[:-1]
                    if line.startswith('End'):
                        break
                    colorlist.append(line)
            elif line.startswith('Outdir:'):
                line = cf.readline()[:-1]
                outdir = line
            else:
                print('Error')
                return
    plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file, rearranged_species_name, rearranged_species_copy_number,
                          target_species_block_file, target_species_name, target_species_copy_number,
                          colorlist, outdir)


if __name__ == '__main__':
    main()