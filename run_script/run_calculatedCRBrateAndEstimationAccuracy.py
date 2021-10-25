import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import argparse
from util.calculatedCRBrateAndEstimationAccuracy import calculatedCRBrateAndEstimationAccuracy


def main():
    """
    Estimated accuracy
    """

    parser = argparse.ArgumentParser(description="IAGS get estimated accuracy")
    parser.add_argument("-c", "--config_file")

    args = parser.parse_args()
    config_file = args.config_file

    speciesAndCopyList = []
    matching_target_file = ''
    matching_target_copy_number = ''
    model_type = ''
    with open(config_file,'r') as cf:
        while True:
            line = cf.readline()[:-1]
            if not line:
                break
            if line.startswith('SpeciesCopyNumberNameList:'):
                while True:
                    line = cf.readline()[:-1]
                    if line.startswith('End'):
                        break
                    items = line.split(' ')
                    speciesAndCopyList.append([items[0],int(items[1]),items[2]])
            elif line.startswith('MatchingTargetSpecies:'):
                line = cf.readline()[:-1]
                matching_target_file = line
            elif line.startswith('MatchingTargetSpeciesCopyNumber:'):
                line = cf.readline()[:-1]
                matching_target_copy_number = int(line)
            elif line.startswith('MatchingTargetSpeciesName:'):
                line = cf.readline()[:-1]
                matching_target_name = line
            elif line.startswith('ModelType:'):
                line = cf.readline()[:-1]
                model_type = line
            elif line.startswith('Outdir:'):
                line = cf.readline()[:-1]
                outdir = line
            else:
                print('Error')
                return

    calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                           speciesAndCopyList, outdir, model_type)

if __name__ == '__main__':
    main()