## The Rheological Behavior of Firn: Experimental Observations of Dislocation Creep via Grain Boundary Sliding 

*How does grain size, strain state, and microstructure influence the rheological behavior of ice compaction among glaciers and ice sheets?*

---

All code and data required to reproduce analyses presented in Furman and Goldsby, 2020 and Supporting Information (See <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/file/d/1SDf_7wlJxUR1KnFe6b0cDSVhVjYN7N4d/view?usp=sharing">Outputs (through Google Drive)</a>

### Introduction to Study
---

<a target="_blank" rel="noopener noreferrer" href="https://www.curf.upenn.edu/project/furman-daniel-experimental-ice-compaction">Project Description (through CURF)</a>

**Key Points**
*	Laboratory compaction tests were performed on ice powder samples of varying grain size, at eighty to ninety percent relative density. 
*	Two power law creep mechanisms emerged from mechanical testing: dislocation creep and dislocation-accommodated grain boundary sliding (disGBS).
*	The flow law predicts disGBS as predominately rate-limiting for solar and terrestrial cryospheres, a result compatible with natural microstructures. 

**Key Words** 
*	Firn, ice sheets, glaciers, densification, microstructure, grain-size-sensitivity, dislocation-accommodated grain boundary sliding, dislocation creep, field boundary hypothesis

**Plain Language Summary** 

Vast deposits of partially dense ice, or firn, form layers in the near-surface of glaciers and ice sheets, both on earth and in solar settings. To determine the flow properties for these regions, we produced and then deformed samples of ice powder in the laboratory. At larger stresses and coarse grain sizes, the rate of densification was found independent of grain size, matching the mechanism classically considered for the near-surface. At small stresses and fine grain sizes, we discovered a mechanism directly dependent on the grain size, meaning that layers composed of fine grains will flow more rapidly than previously considered. This grain-size-sensitivity carries implications for glaciological modeling and numerous other topics in the cryosphere sciences. 

### Workflow

---

The programming workflow is available in [`Firn_notebook.ipynb`](https://nbviewer.jupyter.org/github/daniel-furman/Furman-and-Goldsby/blob/master/Firn_notebook.ipynb), where each .py script is ran in an easy to follow sequence.


### Paper Figures

---

Figure 1: From (a) [Breant et al. (2017)](https://doi.org/10.5194/cp-13-833-2017) (their Figure 3) and (b) [Faria et al. (2014)](https://doi.org/10.1016/j.jsg.2013.11.003) (their Figure 7). <br><br>
Figure 2: `flow_law_fiting.py` <br><br>
Figure 3: `dens_multiweek.py` <br><br>
Figure 4: `mechanism_maps.py` <br><br>
Figure S1: Photographs taken in the laboratory and diagram made with PowerPoint <br><br>
Figure S2: `exp_confidence_intervals.py` <br><br>
Figure S3: Diagrams made with PowerPoint <br><br>
Figure S4: `field_modeling_2.py` <br><br>
Table 1: `flow_law_fitting.py` <br><br>
Table S1: `calc_dens_rates.py` <br><br>

### Data

---

Output from compaction tests (compaction*.csv) and pressure-density profiles (site-name*.csv) are contained in the data/ subfolder. 


### Requirements

---

Python dependencies are listed in a `requirements.txt` file, including the library version numbers. You can replicate the environment your codebase needs by using virtualenv:

```
# This creates the virtual environment
cd $PROJECT-PATH
virtualenv furman-and-goldsby
```
Then install the dependencies by referring to the requirements-py.txt:
```
# This installs the modules
pip install -r requirements.txt

# This activates the virtual environment
source furman-and-goldsby/bin/activate
```
