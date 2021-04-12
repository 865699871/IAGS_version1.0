def readSequence(file):
    chr = []
    with open(file,'r') as rf:
        while True:
            line = rf.readline()[:-2]
            if not line:
                break
            itemset = line.split(' ')
            header = itemset[0]
            new_itemset = [header]
            for i in itemset[1:]:
                item = i.split('_')
                new_itemset.append(item[0])
            chr.append(new_itemset)
    return chr
def outSequence(sequence,outfile):
    outfile = open(outfile,'w')
    for i in sequence:
        for j in i:
            outfile.write(j+' ')
        outfile.write('\n')
    outfile.close()

workdir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/simulations/NonCRBs/'

filelist = ['species.sequence.1','species.sequence.2','species.sequence.3',
            'species.sequence.4','species.sequence.5','species.sequence.6',
            'species.sequence.7','species.sequence.8','species.sequence.9']
for i in filelist:
    sequence = readSequence(workdir + i)
    outSequence(sequence,workdir + i+'.noBar')
