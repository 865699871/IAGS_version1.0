from inferringAncestorGenomeStructure.BlockMatchingOptimization import BlockMatchingOptimization

def readSequence(file):
    chr = []
    with open(file,'r') as rf:
        while True:
            line = rf.readline()[:-2]
            if not line:
                break
            itemset = line.split(' ')[1:]
            chr.append(itemset)
    return chr

def outSequence(sequence,outfile):
    outfile = open(outfile, 'w')
    for i in sequence:
        outfile.write('s ')
        for j in i:
            outfile.write(j+' ')
        outfile.write('\n')

def build_adj(sequence):
    adjlist = []
    for i in sequence:
        start = '$'
        for j in i:
            if j.startswith('-'):
                last = j[1:]+'b'
                adj = sorted([start,last])
                adjlist.append(adj[0]+'@'+adj[1])
                start = j[1:] + 'a'
            else:
                last = j + 'a'
                adj = sorted([start, last])
                adjlist.append(adj[0]+'@'+adj[1])
                start = j + 'b'
        adj = sorted([start,'$'])
        adjlist.append(adj[0]+'@'+adj[1])
    return adjlist

def calculate(sp1_file,sp2_file):
    sp1_seq = readSequence(sp1_file)
    sp2_seq = readSequence(sp2_file)
    sp1_adj = build_adj(sp1_seq)
    sp2_adj = build_adj(sp2_seq)

    fusions = 0
    for i in sp1_adj:
        if '$' in i:
            continue
        else:
            if i not in sp2_adj:
                fusions += 1
    fissions = 0
    for i in sp2_adj:
        if '$' in i:
            continue
        else:
            if i not in sp1_adj:
                fissions += 1
    return fissions,fusions

def calculateFissionAndFussions(species1_file,species2_file,sp1_copy_number,sp2_copy_number,outdir):
    """
    Calculating shuffling events like fissions and fusions.
    Species 1 is descendant and species 2 is ancestor.
    Copy number of species 2 should no larger than species 1.
    Firstly, the copy number of species 2 should be amplifies to species 1
    Then, using BMO to find matching relation between both species
    Finally, counting shuffling events.

    :param species1_file: species1 block sequence file
    :param species2_file: species2 block sequence file
    :param sp1_copy_number: species 1 copy number
    :param sp2_copy_number: species 2 copy number
    :param outdir: output matching sequence
    :return: fissions number and fusions number
    """
    species2 = readSequence(species2_file)
    multi_species2 = []
    for i in range(int(sp1_copy_number / sp2_copy_number)):
        for j in species2:
            multi_species2.append(j)
    outSequence(multi_species2, outdir + 'speices2.amplify.block')
    mo = BlockMatchingOptimization(species1_file, outdir + 'speices2.amplify.block',
                                   matching_dim1=sp1_copy_number,
                                   matching_dim2=sp1_copy_number,
                                   relation1=1,
                                   relation2=1)
    mo.optimization()
    mo.matching_relation()
    output_sequence_file_list = [outdir+'species1.matching.block',
                                 outdir+'species2.amplify.matching.block']
    mo.out_relabel_sequence(output_sequence_file_list)
    fissions,fusions = calculate(output_sequence_file_list[0],output_sequence_file_list[1])
    return fissions,fusions

