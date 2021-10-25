import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import argparse
from models.GMPmodel import GMPmodel


def main():
    """
    Inferring ancestor species with GMP model
    """

    parser = argparse.ArgumentParser(description="IAGS GMP")
    parser.add_argument("-c", "--config_file")

    args = parser.parse_args()
    config_file = args.config_file

    species_block_filelist = []
    outdir = ''
    ancestor_name = ''
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
            elif line.startswith('Outdir:'):
                line = cf.readline()[:-1]
                outdir = line
            elif line.startswith('AncestorName:'):
                line = cf.readline()[:-1]
                ancestor_name = line
            else:
                print('Error')
                return

    GMPmodel(species_file_list=species_block_filelist,
             outdir=outdir,
             ancestor_name=ancestor_name)


if __name__ == '__main__':
    main()