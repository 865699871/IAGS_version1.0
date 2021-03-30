import pandas as pd
from inferringAncestorGenomeStructure.BlockMatchingOptimization import BlockMatchingOptimization
import numpy as np

class StatisticsAdjacencies:

    # 主要完成邻接统计工作，统计祖先邻接在，下属子节点中出现情况
    def __init__(self,ancestor_file,sp_filelist,ancestor_name,splist):
        ancestor_adj = self.__sequence2Adj(ancestor_file)
        sp_adjs = []
        for i in sp_filelist:
            sp_adjs.append(self.__sequence2Adj(i))
        ancestor_adj_dir = {}
        for i in ancestor_adj:
            item = sorted(i)
            key = item[0] + '@' + item[1]
            if key not in ancestor_adj_dir.keys():
                ancestor_adj_dir[key] = 1
            else:
                ancestor_adj_dir[key] += 1
        sp_adjs_dir = []
        for i in sp_adjs:
            sp_adj_dir = {}
            sp_adj = i
            for j in sp_adj:
                item = sorted(j)
                key = item[0] + '@' + item[1]
                if key not in sp_adj_dir.keys():
                    sp_adj_dir[key] = 1
                else:
                    sp_adj_dir[key] += 1
            sp_adjs_dir.append(sp_adj_dir)
        self.__statistic = []
        columns = [ancestor_name] + splist
        index = list(ancestor_adj_dir.keys())
        for i in ancestor_adj_dir.keys():
            item = [ancestor_adj_dir[i]]
            for j in range(len(sp_adjs_dir)):
                if i in sp_adjs_dir[j].keys():
                    item.append(sp_adjs_dir[j][i])
                else:
                    item.append(0)
            self.__statistic.append(item)
        self.__statistic = pd.DataFrame(self.__statistic,index=index,columns=columns)

    def out_ev_file(self,outfile):
        self.__statistic.to_csv(outfile,sep='\t')

    def __sequence2Adj(self,sequence_file):
        sequence = []
        with open(sequence_file,'r') as sf:
            while True:
                line = sf.readline()[:-2]
                if not line:
                    break
                itemset = line.split(' ')
                sequence.append(itemset)
        adj = []
        for i in sequence:
            chr_type = i[0]
            block_sequence = i[1:]
            last = ''
            start = ''
            for j in range(len(block_sequence)):
                if j == 0:
                    if chr_type == 's':
                        block = block_sequence[j]
                        if block.startswith('-'):
                            adj.append(['$',block[1:]+'b'])
                            last = block[1:]+'a'
                        else:
                            adj.append(['$', block + 'a'])
                            last = block + 'b'
                    else:
                        block = block_sequence[j]
                        if block.startswith('-'):
                            last = block[1:] + 'a'
                            start = block[1:] + 'b'
                        else:
                            last = block + 'b'
                            start = block + 'a'

                else:
                    block = block_sequence[j]
                    if block.startswith('-'):
                        adj.append([last, block[1:] + 'b'])
                        last = block[1:] + 'a'
                    else:
                        adj.append([last, block + 'a'])
                        last = block + 'b'
            if chr_type == 's':
                adj.append([last,'$'])
            else:
                adj.append([last, start])
        return adj


def readSequence(file):
    chr = []
    with open(file, 'r') as rf:
        while True:
            line = rf.readline()[:-2]
            if not line:
                break
            itemset = line.split(' ')
            chr.append(itemset)
    return chr

def reverse(item):
    if item[-1] == 'a':
        return item[:-1] + 'b'
    else:
        return item[:-1] + 'a'

def reassembly(adjacencies,startpoint,endpoint):
    adjs = {}
    for i in adjacencies:
        if i[0] not in adjs.keys():
            adjs[i[0]] = i[1]
        if i[1] not in adjs.keys():
            adjs[i[1]] = i[0]
    path = []
    if startpoint[-1] == 'a':
        path.append(startpoint[:-1])
    else:
        path.append('-' + startpoint[:-1])
    start = reverse(startpoint)
    while True:
        next = adjs[start]
        if next[-1] == 'a':
            path.append(next[:-1])
        else:
            path.append('-' + next[:-1])
        start = reverse(next)
        if start == endpoint:
            break
    return path

def outSequence(sequence,outfile):
    outfile = open(outfile, 'w')
    for i in sequence:
        outfile.write('s ')
        for j in i[1:]:
            item = j.split('_')
            outfile.write(item[0]+' ')
        outfile.write('\n')

def transformToAdjacency_for_scoj(file):
    # 对自己连接自己的邻接进行替换，变成两个端粒
        adjacency_list = []
        with open(file) as df:
            while True:
                line = df.readline()[:-2]
                if not line:
                    break
                item = line.split(' ')
                chr_type = item[0]
                last = ''
                start = ''
                sequence = item[1:]
                for j in range(len(sequence)):
                    if j == 0:
                        if chr_type == 's':
                            if sequence[j].startswith('-'):
                                adjacency_list.append(['$', sequence[j][1:] + 'b'])
                                last = sequence[j][1:] + 'a'
                            else:
                                adjacency_list.append(['$', sequence[j] + 'a'])
                                last = sequence[j] + 'b'
                        else:
                            if sequence[j].startswith('-'):
                                last = sequence[j][1:] + 'a'
                                start = sequence[j][1:] + 'b'
                            else:
                                last = sequence[j] + 'b'
                                start = sequence[j] + 'a'
                    else:
                        if sequence[j].startswith('-'):
                            adjacency_list.append([last, sequence[j][1:] + 'b'])
                            last = sequence[j][1:] + 'a'
                        else:
                            adjacency_list.append([last, sequence[j] + 'a'])
                            last = sequence[j] + 'b'
                if chr_type == 's':
                    adjacency_list.append([last, '$'])
                else:
                    adjacency_list.append([last, start])
        # 将endpoint连接自己的情况进行替换
        new_adjacency_list = []
        for j in adjacency_list:
            new_adjacency_list.append(j[0]+'@'+j[1])
        return new_adjacency_list

def estimatedAccuracyModel(CRB_ratio,mode_type):
    if CRB_ratio == 0:
        return 1
    else:
        if mode_type == 'GMP':
            acc = -0.6095 * CRB_ratio * CRB_ratio - 0.3401 * CRB_ratio + 1.0072
        elif mode_type == 'GGHP':
            acc = -0.5456 * CRB_ratio * CRB_ratio - 0.3466 * CRB_ratio + 0.9948
        elif mode_type == 'MultiCopyGMP':
            acc = -0.85428 * CRB_ratio * CRB_ratio - 0.07805 * CRB_ratio + 0.98770
        elif mode_type == 'MultiCopyGGHP':
            acc = -0.84945 * CRB_ratio * CRB_ratio - 0.01042 * CRB_ratio + 0.95885
        else:
            acc = 0
            print('input error')
        return acc

def statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number,ancetsor_name,
                                     speciesAndCopyList,outdir,mode_type,
                                     cutcycle = False,getCRBratio = False):
    """
    Using for evaluation IAGS result. Contain three part:
    1. Calculating ancestor support table by related species.
    2. Cutting cucle block sequence to string.
    Finding an adjacency with minimum support in related species and cutting this adjacency to string.
    3. Calculating CRB ratio and estimated accuracy.

    :param ancestor_file: ancestor block sequence file
    :param ancestor_copy_number: ancestor target copy number
    :param ancetsor_name: ancestor name
    :param speciesAndCopyList: a set of related species using to infer this ancestor.
    Each one contain three items with block sequence file, target copy number and species name.
    :param outdir: output directory
    :param mode_type: calculation modes, including GMP, GGHP, MultiCopyGMP and MultiCopyGGHP.
    :param cutcycle: parameter for whether cut cycle.
    If ancestor contains cycle block sequence, we cut the minimum support adjacency.
    :param getCRBratio: parameter for whether calculted CRB ratio and estimated accuracy.
    """
    matchingFileList = []
    speciesName = []
    ancestormatchingFile = ''
    sumcopynumber = 0
    # matching
    for i in speciesAndCopyList:
        sumcopynumber += i[1]
        mo = BlockMatchingOptimization(i[0],
                                       ancestor_file,
                                       matching_dim1=i[1],
                                       matching_dim2=ancestor_copy_number,
                                       relation1=ancestor_copy_number / ancestor_copy_number,
                                       relation2=i[1] / ancestor_copy_number)
        mo.optimization()
        mo.matching_relation()
        output_sequence_file_list = [outdir + i[2]+'.ev.relabel.block',
                                     outdir + ancetsor_name + '.ev.relabel.block']
        mo.out_relabel_sequence(output_sequence_file_list)
        matchingFileList.append(outdir + i[2]+'.ev.relabel.block')
        speciesName.append(i[2])
        ancestormatchingFile = outdir + ancetsor_name + '.ev.relabel.block'

    ev = StatisticsAdjacencies(ancestormatchingFile,
                    matchingFileList,
                    ancetsor_name, speciesName)
    ev.out_ev_file(outdir + 'ev_'+ancetsor_name+'.xls')
    ev_table = pd.read_csv(outdir + 'ev_'+ancetsor_name+'.xls',sep='\t',index_col=0)
    adjs = ev_table.index.tolist()
    ev_table = np.asarray(ev_table)
    adjs_weight = {}
    for i in range(len(adjs)):
        adjs_weight[adjs[i]] = np.sum(ev_table[i][1:])

    if cutcycle == True:
        ancestorSequence = readSequence(ancestormatchingFile)
        stringSequence = []
        cycleSequence = []
        for i in ancestorSequence:
            if i[0] == 's':
                stringSequence.append(i)
            else:
                cycleSequence.append(i)
        for i in cycleSequence:
            adjacency_list = []
            last = ''
            start = ''
            sequence = i[1:]
            for j in range(len(sequence)):
                if j == 0:
                    if sequence[j].startswith('-'):
                        last = sequence[j][1:] + 'a'
                        start = sequence[j][1:] + 'b'
                    else:
                        last = sequence[j] + 'b'
                        start = sequence[j] + 'a'
                else:
                    if sequence[j].startswith('-'):
                        adjacency_list.append([last, sequence[j][1:] + 'b'])
                        last = sequence[j][1:] + 'a'
                    else:
                        adjacency_list.append([last, sequence[j] + 'a'])
                        last = sequence[j] + 'b'
            adjacency_list.append([last, start])
            # print(adjacency_list)
            new_adjacency_list = []
            minkey = ''
            minweight = 100000
            startpoint = ''
            endpoint = ''
            for j in adjacency_list:
                key = sorted(j)
                key = key[0] + '@' + key[1]
                if adjs_weight[key] < minweight:
                    minweight = adjs_weight[key]
                    minkey = key
            for j in adjacency_list:
                key = sorted(j)
                key = key[0] + '@' + key[1]
                if key != minkey:
                    new_adjacency_list.append(j)
                else:
                    new_adjacency_list.append(['$',j[0]])
                    startpoint = j[0]
                    new_adjacency_list.append(['$',j[1]])
                    endpoint = j[1]
            path = reassembly(new_adjacency_list,startpoint,endpoint)
            stringSequence.append(['s']+path)
        outSequence(stringSequence,outdir + ancetsor_name + '.cutcycle.block')

    if getCRBratio == True:
        endpoints = {}
        for i in matchingFileList:
            adj = transformToAdjacency_for_scoj(i)
            for j in adj:
                endpoint1 = j.split('@')[0]
                endpoint2 = j.split('@')[1]
                if endpoint1 not in endpoints.keys():
                    endpoints[endpoint1] = [endpoint2]
                else:
                    if endpoint2 not in endpoints[endpoint1]:
                        endpoints[endpoint1].append(endpoint2)

                if endpoint2 not in endpoints.keys():
                    endpoints[endpoint2] = [endpoint1]
                else:
                    if endpoint1 not in endpoints[endpoint2]:
                        endpoints[endpoint2].append(endpoint1)
        rate = 0

        for i in endpoints.keys():
            if i == '$':
                continue
            if len(endpoints[i]) == sumcopynumber/ancestor_copy_number:
                rate += 1

        rate = round(rate / (len(endpoints.keys()) - 1), 4)
        acc = estimatedAccuracyModel(rate,mode_type)
        ev_file = open(outdir + 'ev.txt','w')
        ev_file.write('CRB ratio: ' + str(rate) + '\n')
        ev_file.write('Mode: ' + mode_type + '\n')
        ev_file.write('Estimated accuracy: ' + str(acc) + '\n')
        ev_file.close()




# ancestor_file = 'D:/InferAncestorGenome/realData/' \
#                 'IAGS_version1.0/outputdata/Gramineae/Ancestor4/Ancestor4.block'
# ancestor_copy_number = 2
# speciesAndCopyList = [['D:/InferAncestorGenome/realData/'
#                       'IAGS_version1.0/inputdata/'
#                        'Gramineae/Maize.final.block',4,'Maize'],
#                       ['D:/InferAncestorGenome/realData/'
#                        'IAGS_version1.0/inputdata/'
#                        'Gramineae/Sorghum.final.block', 2, 'Sorghum']]
# outdir = 'D:/InferAncestorGenome/realData/' \
#          'IAGS_version1.0/outputdata/Gramineae/Ancestor4/'
# mode_type = 'MultiCopyGGHP'
# statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number,'Ancestor4',
#                                      speciesAndCopyList,outdir,mode_type,
#                                      cutcycle = True,getCRBratio = True)