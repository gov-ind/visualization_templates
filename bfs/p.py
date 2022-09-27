import networkx as nx
import matplotlib.pyplot as plt
from pdb import set_trace

edges = [(0, 1), (1, 2), (2, 3), (3, 5), (0, 4), (4, 5)]
edge_weights = [50, 100, 100, 100, 1, 1]

edge_lens = [1, 1, 3, 1, 4, 5] 

nodes = [0, 1, 2, 3, 4, 5]

for seed in range(3, 4):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)

    for i in range(len(edges)):
        G.add_edge(edges[i][0], edges[i][1], length=edge_weights[i], label=edge_lens[i])

    val_map = { 0: '#c90000',
                5: '#c90000' }

    values = [val_map.get(node, '#3b4d61') for node in G.nodes()]

    red_edges = [(0, 1), (0, 2), (0, 3)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3), (2, 6)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3), (2, 6), (3, 4)]
    red_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (1, 3), (2, 6), (3, 4), (5, 10)]
    red_edges = [(0, 1), (0, 4), (1, 2)]
    red_edges = [(0, 1), (0, 4), (1, 2), (2, 3), (4, 5), (3, 5)]

    edge_colours = ['black' if not edge in red_edges else '#c90000'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    pos = nx.spring_layout(G, weight='length', seed=seed)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                           node_color=values, node_size = 500)
    nx.draw_networkx_labels(G, pos, font_color='white')
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='#c90000', arrows=False, width=2)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False, width=2)
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))

    plt.savefig(f'bfs6.png', bbox_inches='tight', pad_inches=0)
    plt.clf()
