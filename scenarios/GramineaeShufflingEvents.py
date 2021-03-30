from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Gramineae in evolution landscape. 
result in outdutdata/Gramineae
"""
path = 'D:/InferAncestorGenome/realData'

outfile = path + '/IAGS_version1.0/outputdata/Gramineae/shufflingEvents.txt'
outfile = open(outfile,'w')


"""
Ancestor 1 -> O. sativa
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Gramineae/'
ancestor1_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor1/'

descendant_file = species_block_sequence_dir + 'Rice.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> O. sativa\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 2
"""
ancestor2_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor2/'
ancestor1_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor1/'

descendant_file = ancestor2_block_sequence_dir + 'Ancestor2.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 2\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 3
"""
ancestor3_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor3/'
ancestor1_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor1/'

descendant_file = ancestor3_block_sequence_dir + 'Ancestor3.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 3\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 2 -> T. elongatum
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Gramineae/'
ancestor2_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor2/'

descendant_file = species_block_sequence_dir + 'Telongatum.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> T. elongatum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 2 -> B. distachyon
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Gramineae/'
ancestor2_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor2/'

descendant_file = species_block_sequence_dir + 'Brachy.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> B. distachyon\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 3 -> S. bicolor
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Gramineae/'
ancestor3_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor3/'

descendant_file = species_block_sequence_dir + 'Sorghum.final.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> S. bicolorn\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 3 -> Ancestor 4
"""
ancestor4_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor4/'
ancestor3_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor3/'

descendant_file = ancestor4_block_sequence_dir + 'Ancestor4.cutcycle.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> Ancestor 4\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 4 -> Z. mays
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Gramineae/'
ancestor4_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Gramineae/Ancestor4/'

descendant_file = species_block_sequence_dir + 'Maize.final.block'
ancestor_file = ancestor4_block_sequence_dir + 'Ancestor4.cutcycle.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,4,2,ancestor4_block_sequence_dir)
outfile.write('Ancestor 4 -> Z. mays\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')
outfile.close()