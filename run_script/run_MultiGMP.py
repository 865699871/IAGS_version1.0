import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import argparse
from models.MultiGMPmodel import MultiCopyGMPmodel


def main():
    """
    Inferring ancestor species with MultiGMP model
    """

    parser = argparse.ArgumentParser(description="IAGS MultiGMP")
    parser.add_argument("-c", "--config_file")

    args = parser.parse_args()
    config_file = args.config_file

    species_block_filelist = []
    ancestor_name = ''
    guided_species_for_matching = ''
    ancestor_target_copy_number = ''
    outdir = ''
    with open(config_file,'r') as cf:
        while True:
            line = cf.readline()[:-1]
            if not line:
                break
            if line.startswith('Species:'):
                while True:
                    line = cf.readline()[:-1]
                    if line.startswith('End'):
                        break
                    species_block_filelist.append(line)
            elif line.startswith('GuidedSpecies:'):
                line = cf.readline()[:-1]
                guided_species_for_matching = line
            elif line.startswith('Outdir:'):
                line = cf.readline()[:-1]
                outdir = line
            elif line.startswith('AncestorName:'):
                line = cf.readline()[:-1]
                ancestor_name = line
            elif line.startswith('AncestorCopyNumber:'):
                line = cf.readline()[:-1]
                ancestor_target_copy_number = int(line)
            else:
                print('Error')
                return

    MultiCopyGMPmodel(species_block_filelist, outdir,
                      guided_species_for_matching, ancestor_name,
                      ancestor_target_copy_number)


if __name__ == '__main__':
    main()