# Illustration Notes

Notes on specific figures that need attention or have additional context.

---

## Chapter 5 - Flow Diagrams with Unknown Origin

Several flow diagrams in Chapter 5 have unknown origins from "the original manuscript". These are currently marked as **Red** status.

### Figures Needing Replacement

| Figure | Description | Status |
|--------|-------------|--------|
| fig_05_04 | Potential flow round a sheet | Red - Unknown origin |
| fig_05_05 | Flow round a rotating cylinder | Red - Unknown origin |
| fig_05_06a | Airfoil with zero circulation (overview) | Red - Unknown origin |
| fig_05_06b | Trailing edge close-up (zero circulation) | Red - Unknown origin |
| fig_05_06c | Velocity around airfoil surface | Red - Unknown origin |
| fig_05_07a | Airfoil with circulation (overview) | Red - Unknown origin |
| fig_05_07b | Trailing edge close-up (with circulation) | Red - Unknown origin |
| fig_05_07c | Velocity around airfoil surface (circulation) | Red - Unknown origin |
| fig_05_08a | Flow around wing with flap (c=0) | Red - Unknown origin |
| fig_05_08b | Flow around wing with flap (c=6.1) | Red - Unknown origin |
| fig_05_09 | Streamlines in ground effect | Red - Unknown origin |
| fig_05_12 | Potential flow round a sail | Red - Unknown origin |

---

## Recently Replaced Figures (Pending Hugh's Review)

The following figures have been replaced with self-created Python versions. These need Hugh's review to confirm they are acceptable replacements.

### Chapter 4

| Figure | Description | Python Script | Notes |
|--------|-------------|---------------|-------|
| fig_04_09.png | Two-source wave interference pattern | `wave_interference.py` | Grayscale interference pattern from two coherent point sources |
| fig_04_12.png | 3D Gaussian surface ("Mexican Hat") | `gaussian_3d_surface.py` | Rainbow-colored 3D surface with discrete color bands |
| fig_04_13.png | Rayleigh distribution (Probability vs Radius) | `fig_04_13_rayleigh.py` | P(r) ∝ r × exp(-2r²/σ²) curve |
| fig_04_14.png | Brewster angle / refraction diagram | `fig_04_14_brewster.py` | Shows incident, reflected, and refracted rays with polarization arrows |

### Chapter 7

| Figure | Description | Python Script | Notes |
|--------|-------------|---------------|-------|
| fig_07_05.png | Lowest four oscillation modes for 2D membrane (drum skin) | | Self-created replacement |

All Python scripts are located in `/python_flow_figures/` directory.

