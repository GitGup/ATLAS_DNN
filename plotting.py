from ROOT import TH1F, TGraph
import numpy as np
import matplotlib.pyplot as plt

#takes branch name and creates a ROOT histogram
def create_histogram(column, nbins=50):
    data = []
    for arr in column:
        data.extend(arr)

    xmin = np.min(data)
    xmax = np.max(data)

    hist = TH1F("hist", "Histogram", nbins, xmin, xmax)

    for arr in column:
        for val in arr:
            hist.Fill(val)
            
    return hist
    
#ROOT TGraph
def createTGraph(x, y, title="", xtitle="", ytitle=""):
    """Create a ROOT TGraph from given x and y arrays."""
    # Create a TGraph object
    graph = TGraph(len(x), x, y)
    
    # Set the graph title and axis labels
    graph.SetTitle(title)
    graph.GetXaxis().SetTitle(xtitle)
    graph.GetYaxis().SetTitle(ytitle)
    
    # Set the marker style and size
    graph.SetMarkerStyle(1)
    graph.SetMarkerSize(0.5)
    
    # Return the TGraph object
    return graph

#matplotlib scatter plot
def scatter_plot(x, y, title, xlabel, ylabel, s):
    plt.scatter(x, y, s = s)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()