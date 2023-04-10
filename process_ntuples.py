import uproot

from common import np, os
from process_df import remove_empty, divide_by_1000

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

#Takes TTree, events, list of branches and returns data frame 
def generate_df(TTree, branches: list, events):
    
    if not isinstance(branches, list):
        raise TypeError("Input must be a list")
        
    df = show(0, TTree, branches, events)
    df = remove_empty(df)

    df["DMesons_pt"] = df["DMesons_pt"].apply(divide_by_1000)
    for col in df.columns:
        df[col] = df[col].apply(list)
        
    return df