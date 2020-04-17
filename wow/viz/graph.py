import matplotlib.pyplot as plt
from scipy.sparse import csc_matrix
import networkx as nx

def bipartite_graph(M):
    ''' Shows the graph corresponding to the biadjacency measurement matrix '''
    # Creates a basic bipartite group testing type graph from the biadjacency matrix
    SM = csc_matrix(M)
    SG = nx.algorithms.bipartite.matrix.from_biadjacency_matrix(SM)
    X, Y = nx.algorithms.bipartite.sets(SG)
    nx.draw_networkx(
    SG,
    pos = nx.drawing.layout.bipartite_layout(SG, X))
    # nx.draw(SG)
    plt.show()
    return
