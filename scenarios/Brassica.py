from models.GMPmodel import GMPmodel
from util.statisticsAdjacency import statisticsAdjacenciesInformation
"""
Inferring ancestor species for Brassica. GMP model
result in outdutdata/Brassica
"""
path = 'D:/InferAncestorGenome/realData'

workdir = path + '/IAGS_version1.0/inputdata/Brassica/'
species_block_filelist = [workdir + 'Oleracea.final.block',
                          workdir + 'Rapa.final.block',
                          workdir + 'Nigra.final.block']
ancestor_name = 'Brassica'
outdir = path + '/IAGS_version1.0/outputdata/Brassica/'

GMPmodel(species_file_list=species_block_filelist,
         outdir=outdir,
         ancestor_name=ancestor_name)

ancestor_file = outdir + ancestor_name + '.block'
ancestor_copy_number = 1
speciesAndCopyList = [[workdir + 'Oleracea.final.block',ancestor_copy_number,'Oleracea'],
                      [workdir + 'Rapa.final.block',ancestor_copy_number,'Rapa'],
                      [workdir + 'Nigra.final.block',ancestor_copy_number,'Nigra']]

mode_type = 'GMP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outdir,mode_type,
                                     cutcycle = False,getCRBratio = True)