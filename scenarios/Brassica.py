from models.GMPmodel import GMPmodel
from util.statisticsAdjacency import statisticsAdjacenciesInformation
"""
Inferring ancestor species for Brassica using GMP model
result in outdutdata/Brassica
"""
path = 'D:/InferAncestorGenome/realData'

workdir = path + '/IAGS_version1.0/inputdata/Brassica/'
species_block_filelist = [workdir + 'Boleracea.final.block',
                          workdir + 'Brapa.final.block',
                          workdir + 'Bnigra.final.block']
ancestor_name = 'Brassica'
outdir = path + '/IAGS_version1.0/outputdata/Brassica/'

GMPmodel(species_file_list=species_block_filelist,
         outdir=outdir,
         ancestor_name=ancestor_name)

# Evaluation
ancestor_file = outdir + ancestor_name + '.block'
ancestor_copy_number = 1
speciesAndCopyList = [[workdir + 'Boleracea.final.block',ancestor_copy_number,'B.oleracea'],
                      [workdir + 'Brapa.final.block',ancestor_copy_number,'B.rapa'],
                      [workdir + 'Bnigra.final.block',ancestor_copy_number,'B.nigra']]

model_type = 'GMP'
statisticsAdjacenciesInformation(ancestor_file, ancestor_copy_number, ancestor_name,
                                 speciesAndCopyList, outdir, model_type,
                                 cutcycle = False, getCRBratio = True)