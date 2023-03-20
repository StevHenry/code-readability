To determine which metrics are the most relevant, we based our analysis on some research articles.
The articles that were useful in our journey are the following:

# Articles

## 1. Datasets

- [A Comprehensive Model for Code Readability](https://dibt.unimol.it/report/readability/?fbclid=IwAR3fi0Bnu-QOcEcpMDqokbMIbQ-P0yowvEloKhJIWCkGzEK3n1oqAQUt_mM),
  Simone Scalabrino, Mario Linares-Vásquez, Denys Poshyvanyk, Rocco Oliveto
  \- Contains the links of our datasets
- [A General Software Readability Model](https://web.eecs.umich.edu/~weimerw/students/dorn-mcs-paper.pdf),
  Jonathan Dorn
  \- Explaining of the content of its dataset
- [Learning a Metric for Code Readability](https://web.eecs.umich.edu/~weimerw/p/weimer-tse2010-readability-preprint.pdf),
  Raymond P.L. Buse, Westley Weimer
  \- Explaining of the content of its dataset
- [Improving code readability classification using convolutional neural networks](https://reader.elsevier.com/reader/sd/pii/S0950584918301496?token=33FC40D6175CA34AE627B0F3CE5ECB423B1635B6FA0D3C077B6C9845F50F1B3B0407150EEE0476219FA8A08CD8E6E27A&originRegion=eu-west-1&originCreation=20230320081219),
  Qing Mi, Jacky Keung, Yan Xiao, Solomon Mensah, Yujin Gao
  \- Document about code readability classification using convolutional neural networks that use different datasets containing the one of Dorn, Buse and Weimer and other one

## 2. Metrics

- [A Comprehensive Model for Code Readability](https://sscalabrino.github.io/files/2018/JSEP2018AComprehensiveModel.pdf),
  Simone Scalabrino, Mario Linares-Vásquez, Denys Poshyvanyk, Rocco Oliveto
  \- Contains a list of possible metrics (19 metrics)
- [A New Metric for Code Readability](https://www.iosrjournals.org/iosr-jce/papers/Vol6-Issue6/G0664448.pdf?fbclid=IwAR04WfdDDuIAPwIb7W37UxQ3eJ9Eh78DiXjNL-3NvanObYxmLdw40o_gOU4),
  Rajendar Namani1, Kumar J2
  \- Propose a way to calculate code readability thanks to 7 metrics

# Chosen metrics

The metrics we chose to use are:

<div style="text-align: center;">


| Metric name | Measured element                                       | Data value interval |
|-------------|--------------------------------------------------------|---------------------|
| LN          | Lines                                                  | $[ 1; +\infty [$    |
| LC          | Loops                                                  | $[ 0; +\infty [$    |
| NL          | Nested loops + branches                                | $[ 0; +\infty [$    |
| LL          | Lines length mean                                      | $[ 1; +\infty [$    |
| CL          | Comment lines per code line                            | $[ 0; 1 ]$          |
| LBS         | Lines' break after statements                          | $[ 0; 1 ]$          |
| BL          | Blank Lines                                            | $[ 0; 1 ]$          |
| ID          | Indentation                                            | $[ 0; 1 ]$          |
| IL          | Identifiers length (characters)                        | $[ 1; +\infty [$    |
| PA          | Max streak of opening parentheses before a closing one | $[ 1; +\infty [$    |
| FP          | Max streak of following periods                        | $[ 1; +\infty [$    |
| SP          | Spaces (around comparison operators)                   | $[ 1; +\infty [$    |

</div>

To train our model, multiple arrangements will be tested:

Arrangement A: { LN, NL, LL, CL, ID }<br/>
Arrangement B: all metrics
