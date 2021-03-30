from modes.GGHPmode import GGHPmode
from util.statisticsAdjacency import statisticsAdjacenciesInformation

"""
Inferring ancestor species for Yeast species. GGHP mode
nonWGD and WGD yeast should be merged respectively.

result in outdutdata/Yeast
"""

def mergeblock(filelist,outfile):
    """
    merge multi-species file
    :param filelist: species block sequence file list
    :param outfile: output file
    """
    filelines = []
    for i in filelist:
        file = open(i,'r')
        for j in file:
            filelines.append(j)
        file.close()
    outfile = open(outfile,'w')
    for i in filelines:
        outfile.write(i)
    outfile.close()

workdir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/inputdata/Yeast/'
nonWGD_yeast = [workdir + 'gossypii.final.block',
                workdir + 'kluyveri.final.block',
                workdir + 'lactis.final.block',
                workdir + 'rouxii.final.block',
                workdir + 'thermotolerans.final.block',
                workdir + 'waltii.final.block']
merged_nonWGDspecies_file = workdir + 'merged_non_WGD_yeast.block'
mergeblock(nonWGD_yeast,merged_nonWGDspecies_file)

WGD_yeast = [workdir + 'castellii.final.block',
             workdir + 'naganishii.final.block',
             workdir + 'R64.final.block']
merged_WGDspecies_file = workdir + 'merged_WGD_yeast.block'
mergeblock(WGD_yeast,merged_WGDspecies_file)

outdir = 'D:/InferAncestorGenome/realData/IAGS_version1.0/outputdata/Yeast/'
ancestor_name = 'preWGD_yeast'
# three duplicated yeasts and six non duplicated yeasts
GGHPmode(dup_child_file=merged_WGDspecies_file,
         outgroup_file=merged_nonWGDspecies_file,
         outdir=outdir,
         ancestor_name=ancestor_name,
         dup_copy_number=2+2+2,
         out_copy_number=1+1+1+1+1+1)

ancestor_file = outdir + ancestor_name + '.block'
ancestor_copy_number = 1
speciesAndCopyList = [
    [workdir + 'merged_non_WGD_yeast.block',6,'merged_non_WGD_yeast'],
    [workdir + 'merged_WGD_yeast.block',6,'merged_WGD_yeast']
]

mode_type = 'GGHP'
statisticsAdjacenciesInformation(ancestor_file,ancestor_copy_number, ancestor_name,
                                     speciesAndCopyList,outdir,mode_type,
                                     cutcycle = False,getCRBratio = True)