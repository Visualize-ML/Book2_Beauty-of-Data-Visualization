"""
=============
Circular Tree
=============

This example needs Graphviz and PyGraphviz.
https://networkx.org/documentation/stable/auto_examples/graphviz_layout/plot_circular_tree.html#sphx-glr-auto-examples-graphviz-layout-plot-circular-tree-py
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.balanced_tree(3, 5)
pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="")
plt.figure(figsize=(8, 8))
nx.draw(G, pos, node_size=20, alpha=0.5, node_color="blue", with_labels=False)
plt.axis("equal")
plt.show()
