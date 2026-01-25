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

## Other Notes

(Add additional illustration notes here as needed)
