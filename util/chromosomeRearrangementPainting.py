import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
from inferringAncestorGenomeStructure.BlockMatchingOptimization import BlockMatchingOptimization
import pandas as pd

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

def plotBarplot(matched_target_species_block_file, matched_rearranged_species_block_file,
                blockindex_genenumber_file, colorlist, outdir, rearranged_species_name,
                target_species_name):
    ancestorSequence = readSequence(matched_target_species_block_file)
    speciesSequence = readSequence(matched_rearranged_species_block_file)
    blockindex_genenumber_table = np.asarray(pd.read_csv(blockindex_genenumber_file,sep='\t'))
    blockindex_genenumber = {}
    sum_genenumber = 0
    for i in blockindex_genenumber_table:
        blockindex_genenumber[str(i[0])] = i[1]
        sum_genenumber += i[1]
    chr_interval = int(sum_genenumber / (len(ancestorSequence)))
    bar_weight = int(chr_interval/5)
    # plot ancestor
    target_block_color = {}
    fig, ax = plt.subplots()
    for i in range(len(ancestorSequence)):
        color = colorlist[i]
        sequence = ancestorSequence[i]
        start = 0
        for j in sequence:
            if j.startswith('-'):
                block = j[1:]
            else:
                block = j
            target_block_color[block] = color
            blockindex = block.split('_')[0]
            genenumber = blockindex_genenumber[blockindex]
            xy = np.array([i*chr_interval-bar_weight/2, start])
            rect = mpathes.Rectangle(xy, bar_weight, genenumber, color=color)
            start = start + genenumber
            ax.add_patch(rect)
    plt.axis('auto')
    plt.title(target_species_name+' Chromosome plot')
    plt.savefig(outdir + target_species_name+'.chrspaint.pdf')
    plt.close()

    fig, ax = plt.subplots()
    for i in range(len(speciesSequence)):
        sequence = speciesSequence[i]
        start = 0
        for j in sequence:
            if j.startswith('-'):
                block = j[1:]
            else:
                block = j
            blockindex = block.split('_')[0]
            genenumber = blockindex_genenumber[blockindex]
            xy = np.array([i * chr_interval - bar_weight / 2, start])
            rect = mpathes.Rectangle(xy, bar_weight, genenumber, color=target_block_color[block])
            start = start + genenumber
            ax.add_patch(rect)
    plt.axis('auto')
    plt.title(rearranged_species_name + ' Chromosome plot')
    plt.savefig(outdir + rearranged_species_name + '.chrspaint.pdf')
    plt.close()


def plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir):
    """
    Chromosomes rearrangement paint.
    First matching two block sequence and then show the chromosome change in rearranged_species

    :param block_length_file: a table recorded each block length (gene number)
    :param rearranged_species_block_file: block sequence for rearranged species which is species with rearrangement
    :param rearranged_species_name: rearranged species name
    :param rearranged_species_copy_number: rearranged species copy number
    :param target_species_block_file: block sequence for target species
    :param target_species_name: target species name
    :param target_species_copy_number: target species copy number
    :param colorlist: color for chromosomes in target species
    :param outdir: output directory
    """
    mo = BlockMatchingOptimization(rearranged_species_block_file,
                                   target_species_block_file,
                                   matching_dim1=rearranged_species_copy_number,
                                   matching_dim2=target_species_copy_number,
                                   relation1=target_species_copy_number / target_species_copy_number,
                                   relation2=rearranged_species_copy_number / target_species_copy_number)
    mo.optimization()
    mo.matching_relation()
    output_sequence_file_list = [outdir + rearranged_species_name + '.plot.block',
                                 outdir + target_species_name + '.plot.block']
    mo.out_relabel_sequence(output_sequence_file_list)

    plotBarplot(output_sequence_file_list[1], output_sequence_file_list[0],
                block_length_file, colorlist, outdir,
                    rearranged_species_name,target_species_name)




