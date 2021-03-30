from modes.MultiGMPmode import MultiCopyGMPmode
from modes.MultiGGHPmode import MultiCopyGGHPmode
from modes.GGHPmode import GGHPmode
from util.statisticsAdjacency import statisticsAdjacenciesInformation

"""
Inferring ancestor species for Papaver species. 
Ancestor 3: Multi-copy GGHP mode, result in outdutdata/Papaver/Ancestor3
Ancestor 1: GGHP mode, result in outdutdata/Papaver/Ancestor1
Ancestor 2: Multi-copy GMP mode, Ancestor1 should be doubled,result in outdutdata/Papaver/Ancestor2
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
outdir = path + '/IAGS_version1.0/outputdata/Papaver/'

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
MultiCopyGGHPmode(dup_child_file, outgroup_file, outAncestor3dir,
                  ancestor_name, dup_copy_number, out_copy_number,
                  ancestor_target_copy_number)

ancestor_file = outAncestor3dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'PT.final.block',4,'PT'],
    [workdir + 'PS.final.block',2,'PS']
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
GGHPmode(dup_child_file=dup_child_file,
         outgroup_file=outgroup_file,
         outdir=outAncestor1dir,
         ancestor_name=ancestor_name,
         dup_copy_number=2,
         out_copy_number=1)


ancestor_file = outAncestor1dir + ancestor_name + '.block'
ancestor_copy_number = 1
speciesAndCopyList = [
    [workdir + 'PS.final.block',2,'PS'],
    [workdir + 'PR.final.block',1,'PR']
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
MultiCopyGMPmode(species_file_list,outAncestor2dir,guided_species_for_matching,
                 ancestor_name,ancestor_target_copy_number)

ancestor_file = outAncestor2dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'PS.final.block',2,'PS'],
    [outAncestor3dir + 'Ancestor3.block',2,'Ancestor3'],
    [outAncestor1dir + 'Ancestor1.doubled.block',2,'Ancestor1.doubled']
]
mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor2dir,mode_type,
                                     cutcycle = False,getCRBratio = True)



