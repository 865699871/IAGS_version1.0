# IAGS: Inferring Ancestor Genome Structure in a wide range of evolutionary scenarios

The number of novel species with high quality genomes are rapidly accumulating, signaling the start of a golden age for the study of genome structure evolution. Here, we develop IAGS, a generalized novel computational framework to infer ancestral genome structure for a variety of evolutionary scenarios. IAGS provides four basic models to solve simple single-copy (GMP and GGHP) and complex multi-copy ancestor problems (Multi-copy GMP and GGHP) with blocks / endpoints matching optimization (BMO and EMO) strategies and their combinations to decode complex evolutionary history in a bottom-up manner.

## Dependencies
Python 3.6

Packages  | Version used in Research|
--------- | --------|
numpy  | 1.16.4 |
pandas  | 0.20.3 |
matplotlib  | 3.0.3 |

Gurobi solver 9.0.2 (https://www.gurobi.com/ ) with Academic License.   
Development environment: Windows 10  
Development tool: Pycharm  

## Usage
Detailed instruction at docs UserGuide.pdf  
Example usages in scenarios  

## Introductions

### docs
User guide

### dataSturcture
Basic data structure for IAGS.

### inferringAncestorGenomeStructure
Containing the source code of four formulations, including GMP, GGHP, BMO and EMO.

### models
Containing the source code of four basic models for IAGS, including GMP, GGHP, Multi-copy GMP and Multi-copy GGHP.

### util
Including utils for downstream analysis.

### inputdata
Four real datasets used in our research, including block sequences for three Brassica, nine Yeast, five Gramineae and three Papaver species.

### scenarios
Pipline and example usages for four real datasets.

### outputdata
Output for four real datasets

### simulations
Including Non-CRBs and CRBs simulations.
 

## Contact
If you have any questions, please feel free to contact: gaoxian15002970749@163.com




