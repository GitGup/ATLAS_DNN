# ATLAS_DNN

**ATLAS Group at Berkeley**

**Author**: Written by Gurpreet (Gup) Singh (gupsingh@berkeley.edu)

--------------------------------------------------------------------------------
**Purpose**: 

Lambda SPG MC vs Sherpa2211_Wjets.MC16e.700340.27.root

Create a method of seperating Sherpa221_Wjets light slice background and $\Lambda_c^{+}$ signal. $\Lambda_c^{+}$ has distinct dalitz structure that we can take advantage of. Sherpa background has complicated stucture. Difficulties separating the signals because Lambda and D mesons look similar. The proton tracks may look like pion tracks as they have have similar track momenta. The kaon tracks are usually distinguishable but may also be interperated as a pion in the sherpa background. The separating power must come from something deeper than the kinematic properties of the daughter particle tracks, hence dalitz information). We assume three hypothesis for when we create TLorentzVectors to then compute the invariant mass combinations that give us the dalitz information which will then be used when training the machine learning model.

Monte Carlo Forced Decays: $D^{+}\rightarrow k^{-} \pi^{+} \pi^{+}$ and $\Lambda_c^{+}\rightarrow p k^{-} \pi^{+}$
(these were used for testing)
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

- **MC_DNN**: Building of the machine learning model and pre processing of data, creating of TLorentzVectors, and analysis of results.

- **MC_Dalitz**: Creation of Dalitz plots through TLorentzVectors of $D^{+}$ and $\Lambda_C^{+}$ using p_t, eta, phi, and m (from pdg https://pdg.lbl.gov/), confirmed $D^{+}$ Dalitz in accordance to CLEO paper (https://arxiv.org/pdf/0707.3060.pdf), extended to $\Lambda_C^{+}$

--------------------------------------------------------------------------------
