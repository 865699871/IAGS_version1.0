import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import argparse
from models.MultiGGHPmodel import MultiCopyGGHPmodel


def main():
    """
    Inferring ancestor species with MultiGGHP model
    """

    parser = argparse.ArgumentParser(description="IAGS MultiGGHP")
    parser.add_argument("-c", "--config_file")

    args = parser.parse_args()
    config_file = args.config_file

    outdir = ''
    ancestor_name = ''
    dup_child_file = ''
    outgroup_file = ''
    dup_copy_number = 0
    out_copy_number = 0
    ancestor_target_copy_number = 0
    with open(config_file,'r') as cf:
        while True:
            line = cf.readline()[:-1]
            if not line:
                break
            if line.startswith('DuplicatedChildSpecies:'):
                line = cf.readline()[:-1]
                dup_child_file = line
            elif line.startswith('DuplicatedCopyNumber:'):
                line = cf.readline()[:-1]
                dup_copy_number = int(line)
            elif line.startswith('OutgroupSpecies:'):
                line = cf.readline()[:-1]
                outgroup_file = line
            elif line.startswith('OutgroupCopyNumber:'):
                line = cf.readline()[:-1]
                out_copy_number = int(line)
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

    # three duplicated yeasts and six non duplicated yeasts, target copy number are both 6.
    MultiCopyGGHPmodel(dup_child_file, outgroup_file, outdir,
                       ancestor_name, dup_copy_number, out_copy_number,
                       ancestor_target_copy_number)


if __name__ == '__main__':
    main()