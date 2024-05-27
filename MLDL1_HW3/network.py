import matplotlib.pyplot as plt
import networkx as nx

# Define the neural network structure
layers = {
    'Input': ['X1', 'X2', 'X3', '...', 'XN'],
    'Layer 1': ['z1_1', 'z1_2', '...', 'z1_H'],
    'Activation 1': ['a1_1', 'a1_2', '...', 'a1_H'],
    'Layer 2': ['z2_1', 'z2_2', '...', 'z2_C'],
    'Output': ['y1', 'y2', '...', 'yC']
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges for each layer
for i, (layer, nodes) in enumerate(layers.items()):
    for node in nodes:
        G.add_node(node, layer=layer)
        if i > 0:
            prev_layer_nodes = layers[list(layers.keys())[i - 1]]
            for prev_node in prev_layer_nodes:
                G.add_edge(prev_node, node)

# Define node positions
pos = {}
layer_pos = 0
for layer, nodes in layers.items():
    layer_width = len(nodes)
    for j, node in enumerate(nodes):
        pos[node] = (layer_pos, layer_width - 2 * j)
    layer_pos += 1

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
plt.title('Two-Layer Neural Network')
plt.show()