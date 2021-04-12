from util.transformToAdjacency import transformToAdjacency
from inferringAncestorGenomeStructure.GMP import GMP


def GMPmodel(species_file_list, outdir, ancestor_name):
    """
    Inferring ancestor species with GMP model. All species block copy number are only one.

    :param species_file_list: input species block sequence list.
    :param outdir: output directory
    :param ancestor_name: ancestor name
    """
    adj_file = outdir + ancestor_name + '.adj'
    transformToAdjacency(species_file_list, adj_file)
    output_matrix_file = outdir + ancestor_name + '.matrix.xls'
    gmp = GMP(adj_file,
              target_copy_number=1)
    gmp.optimization()
    adjacency_matrix = gmp.ancestor_adjacency_matrix()
    adjacency_matrix.output(output_matrix_file)
    adjacency_matrix.assemble()
    adjacency_matrix.out_assembly(outdir + ancestor_name + '.block', remove_bar=False)
