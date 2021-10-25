import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import argparse
from util.calculateFissionsAndFusions import calculateFissionAndFussions


def main():
    """
    Fissions Fussions number
    """

    parser = argparse.ArgumentParser(description="IAGS get fissions and fussions number")
    parser.add_argument("-c", "--config_file")

    args = parser.parse_args()
    config_file = args.config_file

    descendant_file = ''
    ancestor_file = ''
    descendant_copy_number = 0
    ancestor_copy_number = 0
    outdir = ''
    with open(config_file,'r') as cf:
        while True:
            line = cf.readline()[:-1]
            if not line:
                break
            if line.startswith('DescendantSpecies:'):
                line = cf.readline()[:-1]
                descendant_file = line
            elif line.startswith('DescendantSpeciesCopyNumber:'):
                line = cf.readline()[:-1]
                descendant_copy_number = int(line)
            elif line.startswith('AncestorSpecies:'):
                line = cf.readline()[:-1]
                ancestor_file = line
            elif line.startswith('AncestorSpeciesCopyNumber:'):
                line = cf.readline()[:-1]
                ancestor_copy_number = int(line)
            elif line.startswith('Outdir:'):
                line = cf.readline()[:-1]
                outdir = line
            else:
                print('Error')
                return

    fissions, fusions = calculateFissionAndFussions(descendant_file, ancestor_file,
                                                    descendant_copy_number, ancestor_copy_number,
                                                    outdir)
    print('---------------------------')
    print('fissions: ' + str(fissions))
    print('fusions: ' + str(fusions))


if __name__ == '__main__':
    main()