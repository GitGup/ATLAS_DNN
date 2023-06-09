import uproot
from common import np, pd
import pickle
import os

#removes empty columns given a data frame: returns data frame
def remove_empty(df):
    empty_indices = [i for i, x in enumerate(df[df.columns[0]]) if len(x) == 0]
    df = df.drop(empty_indices)
    df = df.reset_index(drop=True)
    return df

#divides every value in data frame by 1000 (Converts MeV to GeV)
def divide_by_1000(x):
    x_arr = np.array(x)
    x_arr /= 1000
    return uproot.STLVector(x_arr.tolist())

# Save data frame using pickle library (saves to folder named pickled in same dir)
def save(df, name):
    path = "pickled/"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + '{}.pickle'.format(name), 'wb') as f:
        pickle.dump(df, f)
    
# Read data frame and load it
def load(name):
    path = "pickled/"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + '{}.pickle'.format(name), 'rb') as f:
        df = pickle.load(f)
    return df

#if there are more than 2 particles in an event, remove the event (for single particle gun sampels)
def remove_duplicates(df):
    indicies = [i for i, x in enumerate(df[df.columns[0]]) if len(x) > 2]
    df = df.drop(indicies)
    df = df.reset_index(drop=True)
    print("Removed {}".format(len(indicies)) + " duplicate particles")
    return df

#given data frame get the column names
def get_columns(df):
    training_columns = []
    for col in df.columns:
        training_columns.append(col)
    return training_columns
