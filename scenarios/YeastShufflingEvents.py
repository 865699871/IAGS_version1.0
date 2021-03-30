from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Yeast in evolution landscape. 
result in outdutdata/Yeast
"""

path = 'D:/InferAncestorGenome/realData'

outfile = path + '/IAGS_version1.0/outputdata/Yeast/shufflingEvents.txt'
outfile = open(outfile,'w')

"""
preWGD yeast -> N. castellii
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'castellii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> N. castellii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> S. cerevisiae
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'R64.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> S. cerevisiae\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
preWGD yeast -> K. naganishii
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'naganishii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> K. naganishii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> Z. rouxii
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'rouxii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> Z. rouxii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
preWGD yeast -> L. kluyveri
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'kluyveri.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> L. kluyveri\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> L. waltii
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'waltii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> L. waltii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
preWGD yeast -> L. thermotolerans
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'thermotolerans.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> L. thermotolerans\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> E. gossypii
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'gossypii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> E. gossypii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> K. lactis
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'lactis.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> K. lactis\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

outfile.close()