from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Yeast in evolution landscape. 
result in outdutdata/Yeast/plot
"""

colorlist = ['#DF1159','#1E93C9','#26AF67','#D5A1C5','#EBCA6D',
             '#94B51E','#000000']

block_length_file = 'D:/InferAncestorGenome/realData/' \
                    'IAGS_version1.0/inputdata/Yeast/blockindex.genenumber'
target_species_block_file = 'D:/InferAncestorGenome/realData/IAGS_version1.0/' \
                            'outputdata/Yeast/preWGD_yeast.block'
target_species_name = 'preWGDyeast'
target_species_copy_number = 1

"""
preWGD yeast -> N. castellii
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/castellii.final.block'
rearranged_species_name = 'N.castellii'
rearranged_species_copy_number = 2

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
preWGD yeast -> S. cerevisiae
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/R64.final.block'
rearranged_species_name = 'S.cerevisiae'
rearranged_species_copy_number = 2

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
preWGD yeast -> K.naganishii
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/naganishii.final.block'
rearranged_species_name = 'K.naganishii'
rearranged_species_copy_number = 2

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
preWGD yeast -> Z. rouxii
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/rouxii.final.block'
rearranged_species_name = 'Z.rouxii'
rearranged_species_copy_number = 1

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
preWGD yeast -> L.kluyveri
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/kluyveri.final.block'
rearranged_species_name = 'L.kluyveri'
rearranged_species_copy_number = 1

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
preWGD yeast -> L.waltii
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/waltii.final.block'
rearranged_species_name = 'L.waltii'
rearranged_species_copy_number = 1

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
preWGD yeast -> L.thermotolerans
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/thermotolerans.final.block'
rearranged_species_name = 'L.thermotolerans'
rearranged_species_copy_number = 1

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
preWGD yeast -> E. gossypii
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/gossypii.final.block'
rearranged_species_name = 'E.gossypii'
rearranged_species_copy_number = 1

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
preWGD yeast -> K. lactis
"""
rearranged_species_block_file = 'D:/InferAncestorGenome/' \
                                'realData/IAGS_version1.0/' \
                                'inputdata/Yeast/lactis.final.block'
rearranged_species_name = 'K.lactis'
rearranged_species_copy_number = 1

outdir = 'D:/InferAncestorGenome/realData/' \
         'IAGS_version1.0/outputdata/Yeast/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)