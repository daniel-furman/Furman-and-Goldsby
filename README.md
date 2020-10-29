## The Rheological Behavior of Firn Creep: Experimental Observations of disGBS

*How does grain size, strain state, and microstructure influence the rheological behavior of ice compaction among glaciers and ice sheets?*

---

All code and data required to reproduce analyses presented in [Furman and Goldsby, 2020](https://drive.google.com/file/d/19Kfke9_6qqI7a9NjR6NazxbAyYyM4JCL/view?usp=sharing) and [Supporting Information](https://drive.google.com/file/d/1SDf_7wlJxUR1KnFe6b0cDSVhVjYN7N4d/view?usp=sharing).


### Workflow

---

The programming workflow is available in [`Firn_notebook.ipynb`](https://nbviewer.jupyter.org/github/daniel-furman/Furman-and-Goldsby/blob/master/Firn_notebook.ipynb), where each .py script is ran in an easy to follow sequence.


### Figures

---

Figure 1: Figures from (a) [Breant et al. (2017)](https://doi.org/10.5194/cp-13-833-2017) (their Figure 3) and (b) [Faria et al. (2014)](https://doi.org/10.1016/j.jsg.2013.11.003) (their Figure 7). <br><br>
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


### Abstract 

---

Firn densifies through a number of processes at the near-surface of glaciers and ice sheets, with two plastic creep mechanisms previously identified: diffusion and dislocation creep. Here, we performed a series of compaction experiments at nominally constant stress (0.3 – 1.4 MPa) with samples synthesized over a range of grain size (5 – 550 um) at constant temperature (233 K). Measurements of creep rate varied over two orders of magnitude, analyzed via the power-law relationship between strain rate, stress, and grain diameter.

Rates were found directly dependent on grain size with decreasing stress and grain size, resolved to n = 1.6 and p = 0.9, and independent of grain size with increasing stress and grain size, resolved to n = 3.7. We show that the grain-size-sensitivity was induced via dislocation-accommodated grain boundary sliding (disGBS), predicted as predominately rate-limiting across terrestrial and solar cryospheres. 


### Plain Language Summary

---

Vast deposits of partially dense ice, or firn, form layers in the near-surface of glaciers and ice sheets, both on earth and in solar settings. To determine the flow properties for these regions, we produced and then deformed samples of ice powder in the laboratory. 

At larger stresses and coarse grain sizes, the rate of densification was found independent of grain size, matching the mechanism classically considered for the near-surface. At small stresses and fine grain sizes, we discovered a mechanism directly dependent on the grain size, meaning that layers composed of fine grains will flow more rapidly than previously considered. This grain-size-sensitivity carries implications for glaciological modeling and numerous other topics in the cryosphere sciences. 
