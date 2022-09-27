import networkx as nx
import matplotlib.pyplot as plt

data = {0: {1: 5, 6: 10, 7: 1, 13: 20, 2: 19}, 1: {0: 5, 5: 14, 16: 6, 6: 10, 14: 15}, 6: {0: 10, 1: 10, 8: 2, 7: 10, 14: 13, 10: 2}, 7: {0: 1, 6: 10, 13: 18, 15: 8}, 13: {0: 20, 7: 18, 19: 6, 18: 11}, 2: {0: 19, 4: 5, 18: 7, 11: 2, 5: 7, 9: 2}, 5: {1: 14, 2: 7, 4: 20, 20: 19, 14: 16, 17: 11}, 16: {1: 6}, 14: {1: 15, 4: 15, 5: 16, 6: 13, 12: 13}, 4: {2: 5, 17: 13, 8: 13, 15: 17, 14: 15, 10: 9, 5: 20}, 18: {2: 7, 11: 14, 13: 11}, 11: {2: 2, 3: 20, 20: 19, 18: 14}, 9: {2: 2}, 3: {15: 19, 11: 20}, 15: {3: 19, 4: 17, 7: 8, 20: 13}, 17: {4: 13, 5: 11}, 8: {4: 13, 6: 2, 20: 7}, 10: {4: 9, 6: 2, 20: 11}, 20: {5: 19, 8: 7, 10: 11, 11: 19, 12: 1, 15: 13}, 12: {14: 13, 20: 1}, 19: {13: 6}}

from pdb import set_trace

set_trace()

edges = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 5), (5, 10), (2, 6), (6, 7), (7, 10), (3, 4), (4, 6), (1, 2), (5, 6), (1, 6)]

#for k in data:
#    for k2 in data[k]:
#        nodes.append((k, k2))

#set_trace()

nodes = [0, 1, 2, 3, 4, 5, 6, 7, 10]

for seed in range(21, 22):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edge(0, 1, length=5)

    val_map = { 0: '#c90000',
                10: '#c90000' }

    values = [val_map.get(node, '#3b4d61') for node in G.nodes()]

    # Specify the edges you want here
    #red_edges = [(0, 1), (1, 5), (5, 10)]
    red_edges = [(0, 1), (0, 2), (0, 3)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3), (2, 6)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3), (2, 6), (3, 4)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3), (2, 6), (3, 4), (5, 10)]
    red_edges = [(0, 1)]

    edge_colours = ['black' if not edge in red_edges else '#c90000'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G, seed)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                           node_color=values, node_size = 500)
    nx.draw_networkx_labels(G, pos, font_color='white')
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='#c90000', arrows=False, width=2)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False, width=2)
    

    #nx.add_edge(0, 1, length=10)

    plt.savefig(f'bfs1.png', bbox_inches='tight', pad_inches=0)
    plt.clf()
