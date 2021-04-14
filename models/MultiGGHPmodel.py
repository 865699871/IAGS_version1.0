from util.transformToAdjacency import transformToAdjacency
from inferringAncestorGenomeStructure.GGHP import GGHP
from inferringAncestorGenomeStructure.BlockMatchingOptimization import BlockMatchingOptimization
from inferringAncestorGenomeStructure.EndpointMatchingOptimization import EndpointMatchingOptimization


def MultiCopyGGHPmodel(dup_child_file, outgroup_file, outdir,
                       ancestor_name, dup_copy_number, out_copy_number, ancestor_target_copy_number):
    """
    Inferring ancestor species with Multi-copy GGHP model. Ancestor with multi-copy.
    We first use GGHP to get block adjacencies and
    then matching (BMO) dup child species with itself.
    Finally, using EMO with self matched duplicated child to relabel block adjacencies getting block sequence

    :param dup_child_file: block sequence for duplicated child species
    :param outgroup_file: block sequence for outgroup species
    :param outdir: output directory
    :param ancestor_name: ancestor name
    :param dup_copy_number: the block copy number for duplicated child species
    :param out_copy_number: the block copy number for outgroup speices
    :param ancestor_target_copy_number: target copy number of ancestor species.
    """
    adj_file = outdir + ancestor_name + '.adj'
    filelist = [dup_child_file,
                outgroup_file]
    transformToAdjacency(filelist, adj_file)
    ggap = GGHP(adj_file, target_copy_number=ancestor_target_copy_number,
                duptype=dup_copy_number/ancestor_target_copy_number,
                duptype_out=out_copy_number/ancestor_target_copy_number)
    ggap.optimization()
    adjacency_matrix = ggap.ancestor_adjacency_matrix()
    adjacency_matrix.output(outdir + ancestor_name + '.matrix.xls')
    mo = BlockMatchingOptimization(dup_child_file, dup_child_file,
                                   matching_dim1=dup_copy_number,
                                   matching_dim2=dup_copy_number,
                                   relation1=1,
                                   relation2=1,
                                   self_matching=True)
    mo.optimization()
    mo.matching_relation()
    outmatching = outdir + 'dup_self_matching.table.txt'
    mo.output_matching_relation(outmatching)
    output_sequence_file_list = [outdir + 'dup_self_matching.block.relabel']
    mo.out_relabel_sequence(output_sequence_file_list)

    mo = EndpointMatchingOptimization(outdir + ancestor_name + '.matrix.xls',
                                      outdir + 'dup_self_matching.block.relabel',
                                      matching_dim1=ancestor_target_copy_number,
                                      matching_dim2=ancestor_target_copy_number,
                                      relation1=1,
                                      relation2=1,
                                      relabel=False)
    mo.optimization()
    mo.matching_relation()
    adjacency_matrix = mo.build_adjacency_matrix()
    adjacency_matrix.assemble()
    adjacency_matrix.out_assembly(outdir + ancestor_name + '.block', remove_bar=True)

