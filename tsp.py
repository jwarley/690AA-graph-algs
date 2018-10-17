""" This module implements the Christofides 3/2-approximation algorithm for metric TSP. """

import sys
import networkx as nx

def main():
    """ Reads in a graph and prints an approximate TSP tour """

    graph_file_path = sys.argv[1]

    input_graph = nx.read_weighted_edgelist(graph_file_path)

    # Compute an MST for G
    mst = nx.minimum_spanning_tree(input_graph)

    # Compute the subgraph in G induced by odd-degree vertices of the MST
    # Find a minimum-weight matching in this graph

    odd_verts = list(filter(lambda v: mst.degree(v) % 2 == 1, list(mst.nodes)))
    odd_induced_graph = nx.induced_subgraph(input_graph, odd_verts).copy()

    # Need to flip the edge weights since networkx only has a max-weight matching function
    orig_edges = list(odd_induced_graph.edges.items())
    max_weight = max(orig_edges, key=lambda pair: pair[1]['weight'])[1]['weight']

    # subtract the max edge weight from every edge
    flipped_edges = list(map(lambda pair: \
            (pair[0][0], pair[0][1], max_weight - pair[1]['weight']), orig_edges))
    odd_induced_graph.add_weighted_edges_from(flipped_edges)
    matching = nx.max_weight_matching(odd_induced_graph, maxcardinality=True)

    # Union the MST with the matching to get an Eulerian multigraph
    # We can forget the weights at this point

    augmented_mst = nx.MultiGraph()
    augmented_mst.add_edges_from(mst.edges)
    augmented_mst.add_edges_from(matching)

    # Compute an Eulerian circuit of the augmented MST and shortcut if necessary
    tour_nodes = [u for u, v in nx.eulerian_circuit(augmented_mst)]
    final_tour = []
    for node in tour_nodes:
        if node not in final_tour:
            final_tour.append(node)
    final_tour.append(final_tour[0])

    print("Approximate TSP Tour:", final_tour)


if __name__ == "__main__":
    main()
