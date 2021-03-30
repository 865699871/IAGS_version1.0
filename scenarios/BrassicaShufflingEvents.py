from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Brassica in evolution landscape. 
result in outdutdata/Brassica
"""
outfile = 'D:/InferAncestorGenome/realData/IAGS_version1.0/outputdata/Brassica/shufflingEvents.txt'
outfile = open(outfile,'w')

"""
Ancestor Brassica -> B. rapa
"""
species_block_sequence_dir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/inputdata/Brassica/'
ancestor_block_sequence_dir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/outputdata/Brassica/'

descendant_file = species_block_sequence_dir + 'Rapa.final.block'
ancestor_file = ancestor_block_sequence_dir + 'Brassica.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('Ancestor Brassica -> B. rapa\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor Brassica -> B. oleracea
"""
species_block_sequence_dir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/inputdata/Brassica/'
ancestor_block_sequence_dir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/outputdata/Brassica/'

descendant_file = species_block_sequence_dir + 'oleracea.final.block'
ancestor_file = ancestor_block_sequence_dir + 'Brassica.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('Ancestor Brassica -> B. oleracea\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor Brassica -> B. nigra
"""
species_block_sequence_dir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/inputdata/Brassica/'
ancestor_block_sequence_dir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/outputdata/Brassica/'

descendant_file = species_block_sequence_dir + 'nigra.final.block'
ancestor_file = ancestor_block_sequence_dir + 'Brassica.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor_block_sequence_dir)
outfile.write('Ancestor Brassica -> B. nigra\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

outfile.close()