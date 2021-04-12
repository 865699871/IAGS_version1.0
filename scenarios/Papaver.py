from models.MultiGMPmodel import MultiCopyGMPmodel
from models.MultiGGHPmodel import MultiCopyGGHPmodel
from models.GGHPmodel import GGHPmodel
from util.statisticsAdjacency import statisticsAdjacenciesInformation

"""
Inferring ancestor species for Papaver species. 
Ancestor 3: Multi-copy GGHP model, result in outdutdata/Papaver/Ancestor3
Ancestor 1: GGHP model, result in outdutdata/Papaver/Ancestor1
Ancestor 2: Multi-copy GMP model, Ancestor1 should be doubled,result in outdutdata/Papaver/Ancestor2
"""


def doubled(infile,outfile):
    outfile = open(outfile,'w')
    sequence = []
    with open(infile,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            sequence.append(line)
    for i in sequence:
        outfile.write(i)
    for i in sequence:
        outfile.write(i)

path = 'D:/InferAncestorGenome/realData'

workdir = path + '/IAGS_version1.0/inputdata/Papaver/'

"""
Inferring ancestor species for Papaver species. 
Ancestor 3
"""
dup_child_file = workdir + 'PT.final.block'
outgroup_file = workdir + 'PS.final.block'
outAncestor3dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor3/'
dup_copy_number = 4
out_copy_number = 2
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor3'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor3dir,
                   ancestor_name, dup_copy_number, out_copy_number,
                   ancestor_target_copy_number)

ancestor_file = outAncestor3dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'PT.final.block',dup_copy_number,'PT'],
    [workdir + 'PS.final.block',out_copy_number,'PS']
]

mode_type = 'MultiCopyGGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor3dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

"""
Inferring ancestor species for Papaver species. 
Ancestor 1
"""
dup_child_file = workdir + 'PS.final.block'
outgroup_file = workdir + 'PR.final.block'
outAncestor1dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor1/'
dup_copy_number = 2
out_copy_number = 1
ancestor_name = 'Ancestor1'
GGHPmodel(dup_child_file=dup_child_file,
          outgroup_file=outgroup_file,
          outdir=outAncestor1dir,
          ancestor_name=ancestor_name,
          dup_copy_number=dup_copy_number,
          out_copy_number=out_copy_number)


ancestor_file = outAncestor1dir + ancestor_name + '.block'
ancestor_copy_number = 1
speciesAndCopyList = [
    [workdir + 'PS.final.block',dup_copy_number,'PS'],
    [workdir + 'PR.final.block',out_copy_number,'PR']
]
mode_type = 'GGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor1dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

"""
Inferring ancestor species for Papaver species. 
Ancestor 2
"""
doubled(outAncestor1dir + 'Ancestor1.block',outAncestor1dir + 'Ancestor1.doubled.block')
species_file_list = [workdir + 'PS.final.block',
                     outAncestor3dir + 'Ancestor3.block',
                     outAncestor1dir + 'Ancestor1.doubled.block']
guided_species_for_matching = workdir + 'PS.final.block'
outAncestor2dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor2/'
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor2'
MultiCopyGMPmodel(species_file_list, outAncestor2dir, guided_species_for_matching,
                  ancestor_name, ancestor_target_copy_number)

ancestor_file = outAncestor2dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'PS.final.block',ancestor_target_copy_number,'PS'],
    [outAncestor3dir + 'Ancestor3.block',ancestor_target_copy_number,'Ancestor3'],
    [outAncestor1dir + 'Ancestor1.doubled.block',ancestor_target_copy_number,'Ancestor1.doubled']
]
mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor2dir,mode_type,
                                     cutcycle = False,getCRBratio = True)



