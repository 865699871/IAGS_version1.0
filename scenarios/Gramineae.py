from models.MultiGMPmodel import MultiCopyGMPmodel
from models.MultiGGHPmodel import MultiCopyGGHPmodel
from util.statisticsAdjacency import statisticsAdjacenciesInformation

"""
Inferring ancestor species for Gramineae species. 
Ancestor 4: Multi-copy GGHP model, result in outdutdata/Gramineae/Ancestor4
Ancestor 3: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor3
Ancestor 2: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor2
Ancestor 1: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor1

"""
path = 'D:/InferAncestorGenome/realData'

workdir = path + '/IAGS_version1.0/inputdata/Gramineae/'

"""
Inferring ancestor species for Gramineae species. 
Ancestor 4
"""
dup_child_file = workdir + 'Maize.final.block'
outgroup_file = workdir + 'Sorghum.final.block'
outAncestor4dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor4/'
dup_copy_number = 4
out_copy_number = 2
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor4'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor4dir,
                   ancestor_name, dup_copy_number, out_copy_number, ancestor_target_copy_number)

ancestor_file = outAncestor4dir + ancestor_name + '.block'
ancestor_copy_number = ancestor_target_copy_number
speciesAndCopyList = [
    [workdir + 'Maize.final.block',dup_copy_number,'Maize'],
    [workdir + 'Sorghum.final.block',out_copy_number,'Sorghum']
]

mode_type = 'MultiCopyGGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor4dir,mode_type,
                                     cutcycle = True,getCRBratio = True)

"""
Inferring ancestor species for Gramineae species. 
Ancestor 3
"""
species_file_list = [workdir + 'Sorghum.final.block',
                     outAncestor4dir + 'Ancestor4.block',
                     workdir + 'Rice.final.block']
guided_species_for_matching = workdir + 'Sorghum.final.block'
ancestor_target_copy_number = 2
outAncestor3dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor3/'
ancestor_name = 'Ancestor3'
MultiCopyGMPmodel(species_file_list, outAncestor3dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

ancestor_file = outAncestor3dir + ancestor_name + '.block'
ancestor_copy_number = ancestor_target_copy_number
speciesAndCopyList = [
    [workdir + 'Sorghum.final.block',ancestor_copy_number,'Sorghum'],
    [outAncestor4dir + 'Ancestor4.block',ancestor_copy_number,'Ancestor4'],
    [workdir + 'Rice.final.block',ancestor_copy_number,'Rice']
]

mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor3dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

"""
Inferring ancestor species for Gramineae species. 
Ancestor 2
"""
species_file_list = [workdir + 'Brachy.final.block',
                     workdir + 'Telongatum.final.block',
                     workdir + 'Rice.final.block']
guided_species_for_matching = workdir + 'Brachy.final.block'
ancestor_target_copy_number = 2
outAncestor2dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor2/'
ancestor_name = 'Ancestor2'
MultiCopyGMPmodel(species_file_list, outAncestor2dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

ancestor_file = outAncestor2dir + ancestor_name + '.block'
ancestor_copy_number = ancestor_target_copy_number
speciesAndCopyList = [
    [workdir + 'Brachy.final.block',ancestor_copy_number,'Brachy'],
    [workdir + 'Telongatum.final.block',ancestor_copy_number,'Telongatum'],
    [workdir + 'Rice.final.block',ancestor_copy_number,'Rice']
]

mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor2dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

"""
Inferring ancestor species for Gramineae species. 
Ancestor 1
"""
species_file_list = [workdir + 'Rice.final.block',
                     outAncestor2dir + 'Ancestor2.block',
                     outAncestor3dir + 'Ancestor3.block']
guided_species_for_matching = workdir + 'Rice.final.block'
ancestor_target_copy_number = 2
outAncestor1dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor1/'
ancestor_name = 'Ancestor1'
MultiCopyGMPmodel(species_file_list, outAncestor1dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

ancestor_file = outAncestor1dir + ancestor_name + '.block'
ancestor_copy_number = ancestor_target_copy_number
speciesAndCopyList = [
    [workdir + 'Rice.final.block',ancestor_copy_number,'Rice'],
    [outAncestor2dir + 'Ancestor2.block',ancestor_copy_number,'Ancestor2'],
    [outAncestor3dir + 'Ancestor3.block',ancestor_copy_number,'Ancestor3']
]

mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor1dir,mode_type,
                                     cutcycle = False,getCRBratio = True)