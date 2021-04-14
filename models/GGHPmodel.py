from util.transformToAdjacency import transformToAdjacency
from inferringAncestorGenomeStructure.GGHP import GGHP


def GGHPmodel(dup_child_file, outgroup_file, outdir,
              ancestor_name, dup_copy_number, out_copy_number):
    """
    Inferring ancestor species with GGHP model. Ancestor block copy number is only one.
    The block copy number of duplicated child species is dup_copynumber.
    The block copy number of outgroup speices is out_copy_number.
    WGD for dup_child_file: dup_copy_number = 2, out_copy_number = 1 (basic GGHP)
    IAGS allow multiple species as input
    which duplicated species block sequences and outgroup species block sequences
    should be merged together, respectively and
    the input target block copy number should be summed, respectively.

    :param dup_child_file: block sequence file for duplicated child species
    :param outgroup_file: block sequence file for outgroup species
    :param outdir: output directory
    :param ancestor_name: ancestor name
    :param dup_copy_number: target block copy number of duplicated child species
    :param out_copy_number: target block copy number of outgroup species
    """
    filelist = [dup_child_file,outgroup_file]
    adj_file = outdir + ancestor_name + '.adj'
    output_matrix_file = outdir + ancestor_name + '.matrix.xls'
    transformToAdjacency(filelist, adj_file)
    ggap = GGHP(adj_file, target_copy_number=1,
                duptype= dup_copy_number/1,
                duptype_out= out_copy_number/1)
    ggap.optimization()
    adjacency_matrix = ggap.ancestor_adjacency_matrix()
    adjacency_matrix.output(output_matrix_file)
    adjacency_matrix.assemble()
    adjacency_matrix.out_assembly(outdir + ancestor_name + '.block', remove_bar=False)
