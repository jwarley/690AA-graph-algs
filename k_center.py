"""
This module implements the parametric pruning approximation algorithm
for the metric k-center problem.
"""

import sys
import networkx as nx

def main():
    """ Reads in a value of k and a graph and prints an approximate k-centers solution """

    k = int(sys.argv[1])
    graph_file_path = sys.argv[2]

    input_graph = nx.read_weighted_edgelist(graph_file_path)

    # sort the edges of G by nondecreasing weight
    all_edges = list(input_graph.edges.items())
    all_edges.sort(key=lambda pair: pair[1]['weight'])

    # Construct the squares of the edge-induced subgraphs for each edge subset [1..i]
    power_graphs = []
    for i in range(0, len(all_edges)):
        edges_to_remove = list(map(lambda pair: pair[0], all_edges[i+1:]))
        induced_graph = nx.restricted_view(input_graph, [], edges_to_remove)
        power_graphs.append(nx.power(induced_graph, 2))

    # Compute a maximal independent set for each power graph
    # If its size is less than k, return it as our approximate solution
    for pow_graph in power_graphs:
        indep_set = nx.maximal_independent_set(pow_graph)
        if len(indep_set) <= k:
            print("k centers are:", indep_set)
            break

if __name__ == "__main__":
    main()
