from common import np, pd

#Given data frame apply cuts to desired features: returns mutated df
def apply_cuts(df):
    cut_indicies = []
    for index, row in df.iterrows():
        pts = row["DMesons_pt"]
        ms = row["DMesons_m"]
        etas = row["DMesons_eta"]    
        count = 0
        for pt, m, eta in zip(pts, ms, etas):
            if count == 1:
                count = 0
                continue
            if (pt < 8):
                cut_indicies.append(index)
            elif (m < 100):
                cut_indicies.append(index)
            elif (eta > 2.2):
                cut_indicies.append(index)
            count+=1
        
    #drop the row given the index we want to cut
    df = df.drop(index = cut_indicies, axis = 0)
    df = df.reset_index(drop = True)
        
    return df