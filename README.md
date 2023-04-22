# ATLAS_DNN

**ATLAS Group at Berkeley**

**Author**: Written by Gurpreet (Gup) Singh (gupsingh@berkeley.edu)

--------------------------------------------------------------------------------
**Purpose**: 

Monte Carlo Forced Decays: $D^{+}\rightarrow k^{-} \pi^{+} \pi^{+}$ and $\Lambda_c^{+}\rightarrow p k^{-} \pi^{+}$

Create a method of distinguishing D and Lambda Mesons from Lambda Cadidate Reconstructed data. $D^{+}$ and $\Lambda_c^{+}$ have distinct dalitz structure. We want to incoperate the dalitz information through computation of Lorentz Vectors and invariant mass combinations into training to see how well we can seperate D Meson and Lambda reconunstructed particles. 

--------------------------------------------------------------------------------
**Required Packages**:

- > Python
- > ROOT, uproot
- > Tensorflow, keras, sklearn
- > Pandas
--------------------------------------------------------------------------------
**Description of Scripts**:

- **process_ntuples.py**: takes director of ntuples, uses uproot to turn data into a pandas data frame, objects within the data frame are STL Vector objects

- **process_df.py**: methods to manipulate the data frame, or columns/rows of the data frame

- **cuts.py**: apply cutoffs to certain features corresponding to candidate reconstructed particle or tracks of the daughters of the candidate particle

- **plotting.py**: ROOT plotting of HIST, TH1F, TGraph, etc, as well as matplotlib plotting methods

- **common.py**: common imports used across the modules

--------------------------------------------------------------------------------
**Jupyter Notebooks**:

These notebooks are Monte Carlo analyses of forced decays of $D^{+}\rightarrow k^{-} \pi^{+} \pi^{+}$ and $\Lambda_c^{+}\rightarrow p k^{-} \pi^{+}$

- **MC_DNN**: Monte Carlo analysis, cuts, and machine learning applied.

- **MC_Dalitz**: Creation of Dalitz plots through TLorentzVectors of $D^{+}$ and $\Lambda_C^{+}$ using p_t, eta, phi, and m (from pdg https://pdg.lbl.gov/), confirmed $D^{+}$ Dalitz in accordance to CLEO paper (https://arxiv.org/pdf/0707.3060.pdf), extended to $\Lambda_C^{+}$

--------------------------------------------------------------------------------
