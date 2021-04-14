from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Brassica in evolution landscape. 
result in outdutdata/Brassica/plot
"""
path = 'D:/InferAncestorGenome/realData'

colorlist = ['#DF1159','#1E93C9','#26AF67','#D5A1C5','#EBCA6D',
             '#94B51E','#000000','#A9A9A9','#62C1BD']

block_length_file = path + '/IAGS_version1.0/inputdata/Brassica/blockindex.genenumber'
target_species_block_file = path + '/IAGS_version1.0/outputdata/Brassica/Brassica.block'
target_species_name = 'Brassica'
target_species_copy_number = 1


"""
Ancestor Brassica -> B. rapa
"""
rearranged_species_block_file = path + '/IAGS_version1.0/inputdata/Brassica/Brapa.final.block'
rearranged_species_name = 'B.rapa'
rearranged_species_copy_number = 1

outdir = path + '/IAGS_version1.0/outputdata/Brassica/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor Brassica -> B. oleracea
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'inputdata/Brassica/Boleracea.final.block'
rearranged_species_name = 'B.oleracea'
rearranged_species_copy_number = 1

outdir = path + '/IAGS_version1.0/outputdata/Brassica/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
Ancestor Brassica -> B. nigra
"""
rearranged_species_block_file = path + '/IAGS_version1.0/inputdata/Brassica/Bnigra.final.block'
rearranged_species_name = 'B.nigra'
rearranged_species_copy_number = 1

outdir = path + '/IAGS_version1.0/outputdata/Brassica/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)
