#ATLAS_DNN

ATLAS Group at Berkeley

Author: Written by Gurpreet (Gup) Singh (gupsingh@berkeley.edu)

--------------------------------------------------------------------------------
Purpose: Classifier for $D^{+}\rightarrow k^{-} \pi^{+} \pi^{+}$ and $\Lambda_c^{+}\rightarrow p k^{-} \pi^{+}$ from background or W+c jets

--------------------------------------------------------------------------------
Required Packages:

- > Python
- > ROOT, uproot
- > Tensorflow, keras, sklearn
- > Pandas
--------------------------------------------------------------------------------
Description of Scripts:

process_ntuples.py: takes director of ntuples, uses uproot to turn data into a pandas data frame, objects within the data frame are STL Vector objects

process_df.py: methods to manipulate the data frame, or columns/rows of the data frame

cuts.py: apply cutoffs to certain features corresponding to candidate reconstructed particle or tracks of the daughters of the candidate particle

plotting.py: ROOT plotting of HIST, TH1D, etc, as well as matplotlib plotting methods

common.py: common imports used across the modules

--------------------------------------------------------------------------------
Jupyter Notebooks:

These notebooks are Monte Carlo analyses of forced decays of $D^{+}\rightarrow k^{-} \pi^{+} \pi^{+}$ and $\Lambda_c^{+}\rightarrow p k^{-} \pi^{+}$

MC_DNN: Monte Carlo analysis, cuts, and machine learning applied 

MC_Dalitz: Creation of Dalitz plots through TLorentzVectors of $D^{+}$ and $\Lambda_C^{+}$ using p_t, eta, phi, and m (from pdg https://pdg.lbl.gov/), confirmed $D^{+}$ Dalitz in according to CLEO paper (https://arxiv.org/pdf/0707.3060.pdf), extended to $\Lambda_C^{+}$

--------------------------------------------------------------------------------
