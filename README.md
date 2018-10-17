# 690AA-graph-algs

Python implementations for two approximation algorithms:

1. Parametric pruning for metric k-centers
2. Christofides algorithm for metric TSP

The implementations are contained in the respective python files.
Two sample graphs, one K4 and one K6, are supplied in the `.txt` files.

# Dependencies:

This code requires the [networkx](https://networkx.github.io/) Python library.

The code is only tested on Python 3.6, but may work on other versions.

# Usage:

`python k_center.py [k] [graph]`

`python tsp.py [graph]`

Here `k` is the desired number of centers and `graph` is a file path to a weighted graph in edge list format (see the provided text files for examples).
