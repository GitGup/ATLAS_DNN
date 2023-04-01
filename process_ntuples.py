import uproot

from common import np, os

#processes ntunples given directory: returns trees 
def process_ntuple(dir_path, ntuple):
    file = uproot.open(dir_path + "/" + ntuple)
    tree = file["CharmAnalysis;1"]
    return tree

#takes event #, list of branches, and batch size: returns tuple of branches with data
def show(event, TTree, branches, batch_size):
    #if we want the entire data set set batch size = 0
    if batch_size == 0:
        batch_size = TTree.num_entries

    #iterates through TTree as generator functiona and yields batches of data
    current_event = 0
    for array in TTree.iterate(branches, step_size = batch_size, library = "pd"):
        arrays = array[branches]
        if current_event == event:
            break
        current_event+=1
    return arrays