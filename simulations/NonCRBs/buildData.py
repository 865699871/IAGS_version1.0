import random
import copy
import numpy as np
import pandas as pd

def outSequence(sequence,outfile):
    outfile = open(outfile,'w')
    for i in sequence:
        for j in i:
            outfile.write(j+' ')
        outfile.write('\n')
    outfile.close()

def sequence2adjacency(sequence):
    adjacency = []
    for i in sequence:
        block = i[0]
        if block.startswith('-'):
            adjacency.append(['$',block[1:] + 'b'])
            start = block[1:] + 'a'
        else:
            adjacency.append(['$', block + 'a'])
            start = block + 'b'
        for j in range(len(i)-1):
            block = i[j+1]
            if block.startswith('-'):
                adjacency.append([start, block[1:] + 'b'])
                start = block[1:] + 'a'
            else:
                adjacency.append([start, block + 'a'])
                start = block + 'b'
        adjacency.append([start,'$'])
    return adjacency

def reverse(item):
    if item[-1] == 'a':
        return item[:-1] + 'b'
    else:
        return item[:-1] + 'a'

def assemble(adjacency_list):
    # build adj M
    matrix_items = []
    for i in adjacency_list:
        for j in i:
            if j not in matrix_items:
                matrix_items.append(j)
    matrix_items = sorted(matrix_items)
    adjacency_matrix = {}  # 创建初始邻接矩阵
    for i in matrix_items:
        adjacency_matrix[i] = {}
        for j in matrix_items:
            adjacency_matrix[i][j] = 0
    for i in adjacency_list:
        adjacency_matrix[i[0]][i[1]] = 1
        adjacency_matrix[i[1]][i[0]] = 1
    adjacency_matrix = pd.DataFrame(adjacency_matrix)
    index = adjacency_matrix.index.tolist()
    columns = adjacency_matrix.columns.tolist()
    np_adjacency_matrix = np.asarray(adjacency_matrix)
    adjacencies = {}
    for i in range(len(index)):
        for j in range(len(index)):
            if int(np_adjacency_matrix[i][j]) == 1:
                if '$' == index[i] or '$' == index[j]:
                    continue
                pair = sorted([index[i], index[j]])
                key = pair[0] + '@' + pair[1]
                if key not in adjacencies.keys():
                    adjacencies[key] = 1
                else:
                    adjacencies[key] += 1
    adjs = {}
    for i in adjacencies.keys():
        itemset = i.split('@')
        if itemset[0] not in adjs.keys():
            adjs[itemset[0]] = itemset[1]
        if itemset[1] not in adjs.keys():
            adjs[itemset[1]] = itemset[0]
    startpoint = []
    # 遍历矩阵第一行，不是0的加入start:
    for j in range(len(columns)):
        if np_adjacency_matrix[0][j] == 1:
            startpoint.append(columns[j])
    markerstartpoint = []
    chr = []
    for i in startpoint:
        if i not in markerstartpoint:
            path = []
            if i[-1] == 'a':
                path.append(i[:-1])
            else:
                path.append('-' + i[:-1])
            start = reverse(i)
            if start in startpoint:
                markerstartpoint.append(start)
                chr.append(path)
            else:
                while True:
                    next = adjs[start]
                    if next[-1] == 'a':
                       path.append(next[:-1])
                    else:
                        path.append('-' + next[:-1])
                    start = reverse(next)
                    if start in startpoint:
                        markerstartpoint.append(start)
                        break
                chr.append(path)
    vector = []
    for i in chr:
        for j in i:
            if j.startswith('-'):
                vector.append(j[1:])
            else:
                vector.append(j)
    cyclepoint = []
    for i in adjs.keys():
        if i[:-1] not in vector:
            cyclepoint.append(i)
    cyclechr = []
    markercycle = []
    for i in cyclepoint:
        if i not in markercycle:
            startpoint = i
            cycle = []
            markercycle.append(i)
            start = i
            while True:
                next = adjs[start]
                if next[-1] == 'a':
                    cycle.append(next[:-1])
                else:
                    cycle.append('-' + next[:-1])
                markercycle.append(start)
                markercycle.append(next)
                start = reverse(next)
                if start == startpoint:
                    break
            cyclechr.append(cycle)
    return chr,cyclechr

def changeAdj(adj_list):
    change = copy.deepcopy(adj_list)
    endpoints = []
    for j in change:
        for k in j:
            endpoints.append(k)
    random.shuffle(endpoints)
    change_part = []
    for j in range(int(len(endpoints) / 2)):
        change_part.append([endpoints[j * 2], endpoints[2 * j + 1]])
    return change_part



def buildNoCRBSimulations(prefix_adjacencies,
                          suffix_adjacencies, save_final_species_adjacencies, change_adjacency_number,
                          divergence_level, current_level):
    split_adjacency = []
    divergence_change_adjacencies_group_number = len(suffix_adjacencies) * 2
    for i in suffix_adjacencies:
        one_change_adjacencies = []
        for j in range(divergence_change_adjacencies_group_number):
            one_change_adjacencies.append(copy.deepcopy(i[j * change_adjacency_number:(j + 1) * change_adjacency_number]))
        one_change_adjacencies.append(copy.deepcopy(i[divergence_change_adjacencies_group_number * change_adjacency_number:]))
        split_adjacency.append(one_change_adjacencies)

    sub_species_1 = []
    sub_species_2 = []
    copy_number = 0

    for i in split_adjacency:
        sp1_copy = []
        sp2_copy = []
        sp1_change = copy_number
        sp2_change = copy_number+len(split_adjacency)
        for j in range(len(i)):
            # change different part, no CRBs
            if j == sp1_change:
                change = copy.deepcopy(i[j])
                change_part = changeAdj(change)
                sp1_copy.append(change_part)
            else:
                sp1_copy.append(copy.deepcopy(i[j]))
            if j == sp2_change:
                change = copy.deepcopy(i[j])
                change_part = changeAdj(change)
                sp2_copy.append(change_part)
            else:
                sp2_copy.append(copy.deepcopy(i[j]))

        sub_species_1.append(sp1_copy)
        sub_species_2.append(sp2_copy)
        copy_number += 1

    species_1 = []
    for i in range(len(sub_species_1)):
        one_copy = []
        one_copy += copy.deepcopy(prefix_adjacencies[i])
        for j in copy.deepcopy(sub_species_1[i]):
            one_copy += j
        species_1.append(one_copy)
    # save first species
    save_final_species_adjacencies.append(species_1)
    species_2 = []
    for i in range(len(sub_species_2)):
        one_copy = []
        one_copy += copy.deepcopy(prefix_adjacencies[i])
        for j in copy.deepcopy(sub_species_2[i]):
            one_copy += j
        species_2.append(one_copy)
    # save second species
    save_final_species_adjacencies.append(species_2)

    # duplication
    dup_flag = 1
    species_2_dup = []
    if dup_flag == 1:
        for i in range(len(sub_species_2)):
            change_list = copy.deepcopy(sub_species_2[i][:-1])
            unchange = copy.deepcopy(sub_species_2[i][-1])

            split_unchange = []
            for j in range(len(sub_species_2)*2):
                split_unchange.append(copy.deepcopy(unchange[j * change_adjacency_number:(j + 1) * change_adjacency_number]))
            split_unchange.append(unchange[len(sub_species_2) * 2 * change_adjacency_number:])
            # change adjacencies
            change_1 = i*len(sub_species_2)
            change_2 = i*len(sub_species_2) + 1
            new_change_list_copy1 = []
            new_change_list_copy2 = []
            for j in range(len(split_unchange)):
                if j == change_1:
                    change = copy.deepcopy(split_unchange[j])
                    change_part = changeAdj(change)
                    new_change_list_copy1.append(change_part)
                else:
                    new_change_list_copy1.append(copy.deepcopy(split_unchange[j]))
                if j == change_2:
                    change = copy.deepcopy(split_unchange[j])
                    change_part = changeAdj(change)
                    new_change_list_copy2.append(change_part)
                else:
                    new_change_list_copy2.append(copy.deepcopy(split_unchange[j]))
            final_change_list_1 = copy.deepcopy(change_list) + new_change_list_copy1
            final_change_list_2 = copy.deepcopy(change_list) + new_change_list_copy2
            species_2_dup.append(final_change_list_1)
            species_2_dup.append(final_change_list_2)

    if current_level == divergence_level:
        species_2_dup_sequence = []
        for i in range(len(species_2_dup)):
            one_copy = []
            one_copy += copy.deepcopy(prefix_adjacencies[int(i / 2)])
            for j in copy.deepcopy(species_2_dup[i]):
                one_copy += j
            species_2_dup_sequence.append(one_copy)
        save_final_species_adjacencies.append(species_2_dup_sequence)

    else:
        species_2_dup_sequence = []
        for i in range(len(species_2_dup)):
            one_copy = []
            one_copy += copy.deepcopy(prefix_adjacencies[int(i / 2)])
            for j in copy.deepcopy(species_2_dup[i]):
                one_copy += j
            species_2_dup_sequence.append(one_copy)
        # save duplicated species
        save_final_species_adjacencies.append(species_2_dup_sequence)
        new_prefix_adjacency = []
        new_suffix_adjacency = []
        for i in range(len(species_2_dup)):
            one_copy = copy.deepcopy(prefix_adjacencies[int(i / 2)])
            change_part = species_2_dup[i][:-1]
            unchange_part = species_2_dup[i][-1]
            for j in change_part:
                one_copy += copy.deepcopy(j)
            new_prefix_adjacency.append(one_copy)
            new_suffix_adjacency.append(copy.deepcopy(unchange_part))
        # recursion build next level species, level += 1
        buildNoCRBSimulations(new_prefix_adjacency, new_suffix_adjacency,
                              save_final_species_adjacencies, change_adjacency_number,
                              divergence_level, current_level + 1)


def simulateNoCRB(workdir):
    chromosome_number = 5
    block_number = 100
    ancestor_sequence = []
    one_chromosome = int(block_number / chromosome_number)
    block = 100
    for i in range(chromosome_number):
        sequence = []
        for j in range(one_chromosome):
            if block % 2 == 0:
                sequence.append('-' + str(block))
            else:
                sequence.append(str(block))
            block += 1
        ancestor_sequence.append(sequence)
    ancestor_adjacency = sequence2adjacency(ancestor_sequence)
    random.shuffle(ancestor_adjacency)
    print('ancestor adjacency number:')
    print(len(ancestor_adjacency))
    divergence_level = 2
    change_adjacency_number = 5
    save_final_species_adjacencies = []
    buildNoCRBSimulations([[]], [ancestor_adjacency],
                          save_final_species_adjacencies, change_adjacency_number, divergence_level, current_level=0)
    species_count = 1
    # output species
    for i in save_final_species_adjacencies:
        copy_count = 1
        outfile = workdir + 'species.sequence.' + str(species_count)
        print(outfile)
        outfile = open(outfile,'w')
        for j in i:
            filter_tel2tel = []
            for k in j:
                # filter ($,$)
                if k[0] == '$' and k[1] == '$':
                    continue
                else:
                    if k[0] != '$':
                        newendpoint1 = k[0][:-1]+'_'+str(copy_count)+k[0][-1]
                    else:
                        newendpoint1 = '$'
                    if k[1] != '$':
                        newendpoint2 = k[1][:-1]+'_'+str(copy_count)+k[1][-1]
                    else:
                        newendpoint2 = '$'
                    filter_tel2tel.append([newendpoint1,newendpoint2])
            chrs,cycles = assemble(filter_tel2tel)
            for k in chrs:
                outfile.write('s ')
                for l in k:
                    outfile.write(l+' ')
                outfile.write('\n')
            for k in cycles:
                outfile.write('c ')
                min_index = -1
                min_value = 1000000
                for l in range(len(k)):
                    if k[l].startswith('-'):
                        item = k[l][1:].split('_')
                        block = int(item[0])
                    else:
                        item = k[l].split('_')
                        block = int(item[0])
                    if block < min_value:
                        min_index = l
                        min_value = block
                if k[min_index].startswith('-'):
                    half1 = k[min_index + 1:]
                    half2 = k[:min_index + 1]
                    new_string = half1 + half2
                else:
                    half1 = k[min_index:]
                    half2 = k[:min_index]
                    new_string = half1 + half2
                for l in new_string:
                    outfile.write(l+' ')
                outfile.write('\n')
            copy_count += 1
        outfile.close()
        species_count += 1

workdir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/simulations/NonCRBs/'
# simulate No CRB species
simulateNoCRB(workdir)







