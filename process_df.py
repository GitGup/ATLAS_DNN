import uproot
from common import np, pd

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