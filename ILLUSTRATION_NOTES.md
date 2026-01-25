# Illustration Notes

Notes on specific figures that need attention or have additional context.

---

## Chapter 2 - Submarine Cables

### Possible Reference Sources

The following references from the end of Chapter 2 may be the original source for some illustrations:

1. **The Atlantic Cable**, Bern Dibner, Burndy Library Norwalk Conn. 1959
2. **The Theory of the Submarine Telegraph and Telephone Cable**, H.W. Malcolm, Benn Brothers, London, 1917

The 1917 book (Malcolm) is likely out of copyright and could be a valid source for historical diagrams.

**Action:** Check if any of the Chapter 2 figures (particularly Fig. 2.1, 2.2) originate from these references.

---

## Chapter 3 - Tides

### Possible Reference Sources

The following references from the end of Chapter 3 may be the original source for some illustrations:

1. **Erta Pater: an introduction to the Physics of the Earth**, F.D. Stacey and Paul M. Davis, Cambridge University Press
2. **Tides: A Scientific History**, D.E. Cartwright, Cambridge University Press

**Action:** Check if any of the Chapter 3 figures originate from these references.

---

## Chapter 5 - Flow Diagrams with Unknown Origin

### Possible Reference Source

The following reference from the end of Chapter 5 may be the original source for some illustrations:

1. **How do Wings Work?**, Holger Babinsky, IoP Physics Education 38 (6), 297, 2003

**Action:** Check if any of the Chapter 5 flow diagrams originate from this paper. If so, may need permission from IoP or Babinsky.

### Unknown Origin Figures

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

### Python Recreation Attempts

Attempts have been made to recreate these flow diagrams using Python (see `python_flow_figures/` directory).

#### Completed
- **fig_05_04** (Inclined flat plate) - Successfully recreated
- **fig_05_06c** (Velocity distribution) - Successfully recreated

#### In Progress / Attempted
- **fig_05_07a** (Airfoil with circulation) - Attempted but the airfoil shape from the book was difficult to recreate accurately in Python

#### Remaining Work

| Figure | Description | Estimated Difficulty |
|--------|-------------|---------------------|
| fig_05_05 | Rotating cylinder (Magnus effect) | Medium |
| fig_05_06a | Airfoil with zero circulation | Medium |
| fig_05_06b | Trailing edge zoom (zero circulation) | Easy (crop of 5.06a) |
| fig_05_07a | Airfoil with circulation (flat bottom) | Medium-Hard |
| fig_05_07b | Trailing edge zoom (with Kutta condition) | Easy (crop of 5.07a) |
| fig_05_07c | Velocity distribution (with circulation) | Medium |
| fig_05_08a | Airfoil with flap | Hard |
| fig_05_08b | Airfoil with different flap angle | Hard |
| fig_05_09 | Ground effect (airfoil + mirror image) | Medium |
| fig_05_12 | Sail/cambered plate | Medium |

**Note:** The main challenge with recreating the airfoil figures is matching the exact airfoil shape used in the original book. A simpler/standard airfoil shape (e.g., NACA profile) might be acceptable if the physics is correctly represented.

---

## Chapter 9 - Flow Diagrams

| Figure | Description | Status |
|--------|-------------|--------|
| fig_09_04a | Streamlines around cylinder (with arrows) | Red - Unknown origin |
| fig_09_04b | Gauge pressure around cylinder | Red - Unknown origin |
| fig_09_15 | Flow round spinning cylinder (backspin) | Red - Unknown origin |

These may be candidates for Python recreation as well.

---

## Low Resolution Images

The following images appear to be low resolution, blurry, or have other quality issues. They may need to be replaced with higher resolution versions.

### Critical - Need Replacement

| Figure | Dimensions | Issue |
|--------|-----------|-------|
| fig_04_08b.png | 102x180 | Very small - Fresnel diffraction diagram |
| fig_09_01a.jpg | 412x232 | Very low res & blurry - Dambusters plane |
| fig_10_03.png | 300x225 | Low res - Weather map, appears blocky |
| fig_11_01.jpg | 800x556 | Has watermarks ("sciencephotolibrary") |
| fig_11_05.png | 320x320 | Low res - Tippe top photo |
| fig_12_03.png | 680x510 | Has branding (University of Sussex logo) |
| fig_12_06a.png | nil | File may be corrupted (nil dimensions) |
| fig_12_06b.png | nil | File may be corrupted (nil dimensions) |
| fig_13_01a.jpg | 365x300 | Low res - Tacoma Narrows bridge |
| fig_13_08a.png | 38x113 | Extremely small - O-ring diagram |
| fig_13_08b.png | 38x113 | Extremely small - O-ring diagram |

### Borderline - May Need Replacement

| Figure | Dimensions | Issue |
|--------|-----------|-------|
| fig_03_01a.jpg | 640x426 | Borderline resolution - Normandy landings |
| fig_06_01a.png | 460x276 | Low res - Family listening to radio |
| fig_08_01.jpg | 350x525 | Low res - GPS device photo |
| fig_10_07b.png | 402x503 | Small but acceptable (line drawing) |
| fig_10_09a.png | 291x646 | Blocky/compressed - Hugh on bicycle |
| fig_10_11.png | 545x436 | Borderline - Gyrocompass diagram |
| fig_10_12a.png | 503x388 | Low res - Earth oblate spheroid |
| fig_13_06.png | 230x525 | Small but acceptable (line drawing) |

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

### Chapter 5

| Figure | Description | Python Script | Notes |
|--------|-------------|---------------|-------|
| fig_05_04.png | Potential flow round inclined flat plate | `fig_05_04_flat_plate.py` | Rainbow streamlines using elliptic coordinates |

All Python scripts are located in `/python_flow_figures/` directory.

---

## Other Notes

(Add additional illustration notes here as needed)
