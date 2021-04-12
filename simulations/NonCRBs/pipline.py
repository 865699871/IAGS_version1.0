from models.MultiGMPmodel import MultiCopyGMPmodel
from models.MultiGGHPmodel import MultiCopyGGHPmodel
from models.GGHPmodel import GGHPmodel
from util.statisticsAdjacency import statisticsAdjacenciesInformation
from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Inferring ancestor species for 3 WGD simulations. 
Ancestor 8: Multi-copy GGHP model, GGHP with species 9 and 7, EMO with species 9 (self-BMO species 9), 
result ancestor 8.
Ancestor 5: Multi-copy GGHP model, GGHP with species 7 and 4, EMO with species 7 (self-BMO species 7), 
result ancestor 5.
Ancestor 6: Multi-copy GMP model, GMP with species 7, ancestor 8 and doubled ancestor 5, 
result ancestor 6.
Ancestor 2: GGHP model, GGHP with species 4 and 1, 
result ancestor 2.
Ancestor 3: Multi-copy GMP model, GMP with species 4, ancestor 5 and doubled ancestor 2, 
result ancestor 3.
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

workdir = path + '/IAGS_version1.0/simulations/NonCRBs/'
resultfile = open(workdir + 'result.txt', 'w')

"""
Ancestor 8: Multi-copy GGHP model
"""
dup_child_file = workdir + 'species.sequence.9.noBar'
outgroup_file = workdir + 'species.sequence.7.noBar'
outAncestor8dir = path + '/IAGS_version1.0/simulations/NonCRBs/inferring/Ancestor8/'
dup_copy_number = 8
out_copy_number = 4
ancestor_target_copy_number = 4
ancestor_name = 'Ancestor8'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor8dir,
                   ancestor_name, dup_copy_number, out_copy_number,
                   ancestor_target_copy_number)

ancestor_file = outAncestor8dir + ancestor_name + '.block'
speciesAndCopyList = [
    [dup_child_file,dup_copy_number,'species.sequence.9'],
    [outgroup_file,out_copy_number,'species.sequence.7']
]

mode_type = 'MultiCopyGGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor8dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

fissions,fusions = calculateFissionAndFussions(ancestor_file,
                                               workdir + 'species.sequence.8.noBar',
                                               ancestor_target_copy_number,ancestor_target_copy_number,outAncestor8dir)
resultfile.write('Ancestor 8 fissions: ' + str(fissions) + '\t' + 'fusions: '+str(fusions) + '\n')

"""
Ancestor 5: Multi-copy GGHP model
"""
dup_child_file = workdir + 'species.sequence.7.noBar'
outgroup_file = workdir + 'species.sequence.4.noBar'
outAncestor5dir = path + '/IAGS_version1.0/simulations/NonCRBs/inferring/Ancestor5/'
dup_copy_number = 4
out_copy_number = 2
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor5'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor5dir,
                   ancestor_name, dup_copy_number, out_copy_number,
                   ancestor_target_copy_number)

ancestor_file = outAncestor5dir + ancestor_name + '.block'
speciesAndCopyList = [
    [dup_child_file,dup_copy_number,'species.sequence.7'],
    [outgroup_file,out_copy_number,'species.sequence.4']
]

mode_type = 'MultiCopyGGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor5dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

fissions,fusions = calculateFissionAndFussions(ancestor_file,
                                               workdir + 'species.sequence.5.noBar',
                                               ancestor_target_copy_number,ancestor_target_copy_number,outAncestor5dir)
resultfile.write('Ancestor 5 fissions: ' + str(fissions) + '\t' + 'fusions: '+str(fusions) + '\n')

"""
Ancestor 6: Multi-copy GMP model
"""
outAncestor6dir = path + '/IAGS_version1.0/simulations/NonCRBs/inferring/Ancestor6/'
doubled(outAncestor5dir + 'Ancestor5.block', outAncestor6dir + 'Ancestor5.doubled.block')
species_file_list = [workdir + 'species.sequence.7.noBar',
                     outAncestor8dir + 'Ancestor8.block',
                     outAncestor6dir + 'Ancestor5.doubled.block']
guided_species_for_matching = workdir + 'species.sequence.7.noBar'
ancestor_target_copy_number = 4
ancestor_name = 'Ancestor6'
MultiCopyGMPmodel(species_file_list, outAncestor6dir, guided_species_for_matching,
                  ancestor_name, ancestor_target_copy_number)

ancestor_file = outAncestor6dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'species.sequence.7.noBar',ancestor_target_copy_number,'species.sequence.7'],
    [outAncestor8dir + 'Ancestor8.block',ancestor_target_copy_number,'Ancestor8'],
    [outAncestor6dir + 'Ancestor5.doubled.block',ancestor_target_copy_number,'Ancestor5.doubled']
]
mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor6dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

fissions,fusions = calculateFissionAndFussions(ancestor_file,
                                               workdir + 'species.sequence.6.noBar',
                                               ancestor_target_copy_number,ancestor_target_copy_number,outAncestor6dir)
resultfile.write('Ancestor 6 fissions: ' + str(fissions) + '\t' + 'fusions: '+str(fusions) + '\n')

"""
Ancestor 2: GGHP model
"""
dup_child_file = workdir + 'species.sequence.4.noBar'
outgroup_file = workdir + 'species.sequence.1.noBar'
outAncestor2dir = path + '/IAGS_version1.0/simulations/NonCRBs/inferring/Ancestor2/'
dup_copy_number = 2
out_copy_number = 1
ancestor_target_copy_number = 1
ancestor_name = 'Ancestor2'
GGHPmodel(dup_child_file=dup_child_file,
          outgroup_file=outgroup_file,
          outdir=outAncestor2dir,
          ancestor_name=ancestor_name,
          dup_copy_number=dup_copy_number,
          out_copy_number=out_copy_number)


ancestor_file = outAncestor2dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'species.sequence.4.noBar',dup_copy_number,'species.sequence.4'],
    ['species.sequence.1.noBar',out_copy_number,'species.sequence.1']
]
mode_type = 'GGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor2dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

fissions,fusions = calculateFissionAndFussions(ancestor_file,
                                               workdir + 'species.sequence.2.noBar',
                                               ancestor_target_copy_number,ancestor_target_copy_number,outAncestor2dir)
resultfile.write('Ancestor 2 fissions: ' + str(fissions) + '\t' + 'fusions: '+str(fusions) + '\n')



"""
Ancestor 3: Multi-copy GMP model
"""
outAncestor3dir = path + '/IAGS_version1.0/simulations/NonCRBs/inferring/Ancestor3/'
doubled(outAncestor2dir + 'Ancestor2.block', outAncestor3dir + 'Ancestor2.doubled.block')
species_file_list = [workdir + 'species.sequence.4.noBar',
                     outAncestor5dir + 'Ancestor5.block',
                     outAncestor3dir + 'Ancestor2.doubled.block']
guided_species_for_matching = workdir + 'species.sequence.4.noBar'
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor3'
MultiCopyGMPmodel(species_file_list, outAncestor3dir, guided_species_for_matching,
                  ancestor_name, ancestor_target_copy_number)

ancestor_file = outAncestor3dir + ancestor_name + '.block'
speciesAndCopyList = [
    [workdir + 'species.sequence.4.noBar',ancestor_target_copy_number,'species.sequence.4'],
    [outAncestor5dir + 'Ancestor5.block',ancestor_target_copy_number,'Ancestor5'],
    [outAncestor3dir + 'Ancestor2.doubled.block',ancestor_target_copy_number,'Ancestor2.doubled']
]
mode_type = 'MultiCopyGMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_target_copy_number, ancestor_name,
                                     speciesAndCopyList,outAncestor3dir,mode_type,
                                     cutcycle = False,getCRBratio = True)

fissions,fusions = calculateFissionAndFussions(ancestor_file,
                                               workdir + 'species.sequence.3.noBar',
                                               ancestor_target_copy_number,ancestor_target_copy_number,outAncestor3dir)
resultfile.write('Ancestor 3 fissions: ' + str(fissions) + '\t' + 'fusions: '+str(fusions) + '\n')



resultfile.close()

