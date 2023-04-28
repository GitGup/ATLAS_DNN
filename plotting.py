import ROOT
from ROOT import TH1F, TGraph, TH2F, TCanvas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#-------------------------- ROOT --------------------------

#Given a data frame where the entries are floats
def create_histogram(column, nbins=50):
    xmin = np.min(column)
    xmax = np.max(column)

    hist = TH1F("hist", "Histogram", nbins, xmin, xmax)

    #need these when calling
    #canvas = ROOT.TCanvas("canvas", "My Canvas")
    #hist.Draw()
    #canvas.Draw()
    for val in column:
        hist.Fill(val)
            
    return hist

#given a data frame where the entries are arrays/lists, plot a ROOT Hist
def create_histogram_from_df_array(column, nbins=50):
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

def create_2dhistogram(xdata, ydata, title, xlabel, ylabel, nbinsx, xmin, xmax, nbinsy, ymin, ymax):
    hist = ROOT.TH2F("hist", title, nbinsx, xmin, xmax, nbinsy, ymin, ymax)
    hist.GetXaxis().SetTitle(xlabel)
    hist.GetYaxis().SetTitle(ylabel)

    for i in range(len(xdata)):
        hist.Fill(xdata[i], ydata[i])

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

#-------------------------- MATPLOTLIB --------------------------

#scatter plot
def scatter_plot(x, y, s):
    plot = plt.scatter(x, y, s = s)
    return plot

#histogram
def hist(x, bins):
    plt.hist(x, bins)

def hist_normalized(data1, data2, bins):
    
    if not isinstance(data1, (pd.Series, np.ndarray)) or not isinstance(data2, (pd.Series, np.ndarray)):
        raise TypeError("data must be a Pandas Series or NumPy array")
        
    counts, bins, _ = plt.hist(data1, bins=bins)
    counts2, bins2, _ = plt.hist(data2, bins=bins)
    # Normalize the histogram using the formula
    density = counts / (sum(counts) * np.diff(bins))
    density2 = counts2 / (sum(counts2) * np.diff(bins2))

    # Plot the normalized histogram
    plt.clf()
    plt.bar(bins[:-1], density, width=np.diff(bins), align='edge', alpha=0.5, label = "Sherpa Background")
    plt.bar(bins2[:-1], density2, width=np.diff(bins2), align='edge', alpha=0.5, label = "$\Lambda_C^{+}$ Signal")
    return plt