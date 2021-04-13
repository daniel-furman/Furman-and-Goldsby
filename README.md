## The Rheological Behavior of Firn: Experimental Observations of Grain Size Sensitivity and Application to Ice Sheet Deformation

*How does grain size, strain state, and microstructure influence the rheological behavior of ice compaction among glaciers and ice sheets?*

**[`Firn_notebook.ipynb`](https://nbviewer.jupyter.org/github/daniel-furman/Furman-and-Goldsby/blob/master/Firn_notebook.ipynb)**

 
Experimental results | Flow model for Antarctica (densification rate)
:-------------------------------------------:|:------------------------------:
![](data/exp-interv.png) | ![](data/map.png)


**Key Points**
* Constant stress laboratory experiments were performed on H20 ice powder samples with roughly uniform grain size varying from 5 to 550 micrometers (µm) in radius. 
*	Two rheologically-distinct creep regimes emerged, characterized by their grain size sensitivity and stress dependence: dislocation creep (n ~ 3.7, p ~ 0) and disGBS (n ~ 1.6, p ~ 0.9). 
*	Flow laws resolved the disGBS mechanism as predominantly rate-limiting for natural conditions, such as in glaciers and ice sheets.  

### Data

---

Output from compaction tests (compaction*.csv) and pressure-density profiles (site-name*.csv) are contained in the data/ subfolder. 


### Paper Figures

---

Figure 1: From (a) [Breant et al. (2017)](https://doi.org/10.5194/cp-13-833-2017) (their Figure 3) and (b) [Faria et al. (2014)](https://doi.org/10.1016/j.jsg.2013.11.003) (their Figure 7). <br><br>
Figure 2: Photographs taken in the laboratory and diagram made with PowerPoint <br><br>
Figure 3: `flow_law_fiting.py` <br><br>
Figure 4: `mechanism_maps.py` <br><br>
Table S1: `calc_dens_rates.py` <br><br>

### Workflow

---

The programming workflow is available in [`Firn_notebook.ipynb`](https://nbviewer.jupyter.org/github/daniel-furman/Furman-and-Goldsby/blob/master/Firn_notebook.ipynb), where each .py script is ran in an easy to follow sequence.

