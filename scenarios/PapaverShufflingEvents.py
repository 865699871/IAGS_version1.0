from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Papaver in evolution landscape. 
result in outdutdata/Papaver
"""

path = 'D:/InferAncestorGenome/realData'

outfile = path + '/IAGS_version1.0/outputdata/Papaver/shufflingEvents.txt'
outfile = open(outfile,'w')


"""
Ancestor 1 -> P. rhoeas
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Papaver/'
ancestor1_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor1/'

descendant_file = species_block_sequence_dir + 'PR.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,1,1,ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> P. rhoeas\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 2
"""
ancestor2_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor2/'
ancestor1_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor1/'

descendant_file = ancestor2_block_sequence_dir + 'Ancestor2.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,1,ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 2\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 2 -> Ancestor 3
"""
ancestor3_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor3/'
ancestor2_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor2/'

descendant_file = ancestor3_block_sequence_dir + 'Ancestor3.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> Ancestor 3\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 2 -> P. somniferum
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Papaver/'
ancestor2_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor2/'

descendant_file = species_block_sequence_dir + 'PS.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,2,2,ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> P. somniferum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 3 -> P. setigerum
"""
species_block_sequence_dir = path + '/IAGS_version1.0/inputdata/Papaver/'
ancestor3_block_sequence_dir = path + '/IAGS_version1.0/outputdata/Papaver/Ancestor3/'

descendant_file = species_block_sequence_dir + 'PT.final.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,4,2,ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> P. setigerum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')
outfile.close()