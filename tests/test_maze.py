import pytest
# os
import os
# plot
import matplotlib.pyplot as plt

@pytest.fixture
def croz():
    """test Maze class """
    # build fixture
    from wadl.lib.maze import Maze
    # cros test fixture
    starts = [(0,0),
              (1,1)]
    path = os.path.join(os.path.dirname( __file__ ), 'data')
    file = os.path.join(path, "croz_west")
    absfile = os.path.abspath(file)
    return Maze(absfile, starts,
                  step=40, rotation=15)

def test_config(croz):
    # save figure to disk
    fig, ax = plt.subplots()
    croz.plot(ax, showGrid=True)
    plt.savefig('tests/croz-grid.png') 
    # number of nodes and edges
    assert(len(croz.graph.nodes)==564), "nodes mismatch"
    assert(len(croz.graph.edges)==1048), "edges mismatch"