from modes.GMPmode import GMPmode
from util.statisticsAdjacency import statisticsAdjacenciesInformation
"""
Inferring ancestor species for Brassica. GMP mode
result in outdutdata/Brassica
"""

workdir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/inputdata/Brassica/'
species_block_filelist = [workdir + 'Oleracea.final.block',
                          workdir + 'Rapa.final.block',
                          workdir + 'Nigra.final.block']
ancestor_name = 'Brassica'
outdir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/outputdata/Brassica/'

GMPmode(species_file_list=species_block_filelist,
        outdir=outdir,
        ancestor_name=ancestor_name)

ancestor_file = outdir + ancestor_name + '.block'
ancestor_copy_number = 1
speciesAndCopyList = [[workdir + 'Oleracea.final.block',1,'Oleracea'],
                      [workdir + 'Rapa.final.block',1,'Rapa'],
                      [workdir + 'Nigra.final.block',1,'Nigra']]

mode_type = 'GMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outdir,mode_type,
                                     cutcycle = False,getCRBratio = True)