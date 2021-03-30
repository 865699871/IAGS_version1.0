from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution landscape. 
result in outdutdata/Gramineae/plot
"""
path = 'D:/InferAncestorGenome/realData'

colorlist = ['#DF1159','#1E93C9','#26AF67','#D5A1C5','#EBCA6D',
             '#94B51E','#000000','#A9A9A9','#62C1BD','#FF8C00','#4169E1']

block_length_file = path + '/IAGS_version1.0/inputdata/Gramineae/blockindex.genenumber'
target_species_block_file = path + '/IAGS_version1.0/' \
                            'outputdata/Gramineae/Ancestor1/Ancestor1.block'
target_species_name = 'Ancestor1'
target_species_copy_number = 2

"""
Ancestor 1 -> O. sativa
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'inputdata/Gramineae/Rice.final.block'
rearranged_species_name = 'O.sativa'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> Ancestor 2
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'outputdata/Gramineae/Ancestor2/Ancestor2.block'
rearranged_species_name = 'Ancestor2'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> Ancestor 3
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'outputdata/Gramineae/Ancestor3/Ancestor3.block'
rearranged_species_name = 'Ancestor3'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> T. elongatum
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'inputdata/Gramineae/Telongatum.final.block'
rearranged_species_name = 'T.elongatum'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> B. distachyon
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'inputdata/Gramineae/Brachy.final.block'
rearranged_species_name = 'B.distachyon'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
Ancestor 1 -> S. bicolor
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'inputdata/Gramineae/Sorghum.final.block'
rearranged_species_name = 'S.bicolor'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
Ancestor 1 -> Ancestor 4
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'outputdata/Gramineae/Ancestor4/Ancestor4.cutcycle.block'
rearranged_species_name = 'Ancestor4'
rearranged_species_copy_number = 2

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
Ancestor 1 -> Z. mays
"""
rearranged_species_block_file = path + '/IAGS_version1.0/' \
                                'inputdata/Gramineae/Maize.final.block'
rearranged_species_name = 'Z.mays'
rearranged_species_copy_number = 4

outdir = path + '/IAGS_version1.0/outputdata/Gramineae/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)