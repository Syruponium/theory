# Syruponium V8: A Refractive Alternative to Cold Dark Matter

Syruponium V8 is a gravitationally and thermally coupled condensate model designed to address galaxy cluster lensing offsets through microphysical refractive mechanisms rather than collisionless dark matter particles.

## 🌌 Key Concept
Unlike ΛCDM, Syruponium V8 treats the cosmic vacuum as a superfluid medium. Local energetic flux ($\Phi$) from baryons causes a density depletion in the condensate, modifying the effective refractive index. This tracks lensing centroids to baryonic energy sources rather than invisible mass concentrations.

### Scientific Highlights
* **Technical Naturalness:** Dimensionless coupling constants ($g \approx 10^{-32}$) remain stable against 1-loop radiative corrections.
* **Predictive Power:** Explains the "Bullet Cluster" offset and predicts unique spectral signatures.
* **Falsifiability:** Predicts a wavelength-dependent (chromatic) shift in gravitational deflection, violating the GR achromatic principle.

## 📊 Simulation Results
The following figures demonstrate the core predictions of the V8 model.

### 1. Thermal Lensing Correlation
<img src="results/fig1_lensing_residual_map.png" width="800" alt="Lensing Residual Map">
*Figure 1: Spatial correlation between thermal flux contours and Syruponium-induced lensing residuals.*

### 2. Centroid Relaxation
<img src="results/fig2_centroid_relaxation_curve.png" width="800" alt="Centroid Relaxation Curve">
*Figure 2: Temporal decay of the lensing centroid offset post-collision, governed by the healing timescale.*

### 3. Chromatic Signature
<img src="results/fig3_chromatic_shift_correlation.png" width="800" alt="Chromatic Signature">
*Figure 3: Predicted arcsecond shift between NIR and Radio frequencies as a function of local flux.*

## 🔭 Observation Proposals
A formal **JWST + ALMA Observing Proposal** is located in the `/proposals` directory. This pilot program is designed to search for the $0.01''$ chromatic signature in high-redshift mergers like *El Gordo*.

## 📂 Repository Structure
* `/theory`: Mathematical foundation and Lagrangian derivations.
* `/proposals`: Technical justifications for telescope time allocation.
* `/results`: High-resolution simulation outputs and figures.
* `/scripts`: Python tools for reproducibility.

## 🛠 Usage
To reproduce the simulation outputs, navigate to the scripts directory and run:
`python syruponium_v8_sim.py`

## License
Licensed under the [MIT License](LICENSE).
