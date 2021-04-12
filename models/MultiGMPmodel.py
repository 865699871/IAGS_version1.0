from util.transformToAdjacency import transformToAdjacency
from inferringAncestorGenomeStructure.GMP import GMP
from inferringAncestorGenomeStructure.EndpointMatchingOptimization import EndpointMatchingOptimization


def MultiCopyGMPmodel(species_file_list, outdir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number):
    """
    Inferring ancestor species with Multi-copy GMP model. Ancestor with multi-copy.
    All species shared duplication events and block cop number are ancestor_target_copy_number.
    We first use GMP to get block adjacencies and
    then matching (EMO) with a guided species to relabel block adjacencies getting block sequence

    :param species_file_list: input species block sequence list.
    :param outdir: output directory.
    :param guided_species_for_matching:
    :param ancestor_name: ancestor name
    :param ancestor_target_copy_number: ancestor species target copy number copy number.
    """
    adj_file = outdir + ancestor_name + '.adj'
    transformToAdjacency(species_file_list, adj_file)
    output_matrix_file = outdir + ancestor_name + '.matrix.xls'
    gmp = GMP(adj_file,
              target_copy_number=ancestor_target_copy_number)
    gmp.optimization()
    adjacency_matrix = gmp.ancestor_adjacency_matrix()
    adjacency_matrix.output(output_matrix_file)
    mo = EndpointMatchingOptimization(output_matrix_file, guided_species_for_matching,
                                      matching_dim1=ancestor_target_copy_number,
                                      matching_dim2=ancestor_target_copy_number,
                                      relation1=1,
                                      relation2=1,relabel=True)
    mo.optimization()
    mo.matching_relation()
    adjacency_matrix = mo.build_adjacency_matrix()
    adjacency_matrix.assemble()
    adjacency_matrix.out_assembly(outdir + ancestor_name + '.block', remove_bar=True)
