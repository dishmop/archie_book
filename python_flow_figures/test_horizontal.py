"""Test horizontal flow past horizontal plate - should have horizontal streamlines far from plate."""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def test_horizontal_plate():
    a = 2.0  # half-length of plate
    c = a / 2  # Joukowski parameter so plate spans -a to a
    U = 1.0

    # Grid
    x = np.linspace(-4, 4, 500)
    y = np.linspace(-5, 5, 500)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y

    # Inverse Joukowski
    with np.errstate(invalid='ignore'):
        disc = z**2 - 4*c**2
        sqrt_disc = np.sqrt(disc)
        zeta_plus = (z + sqrt_disc) / 2
        zeta_minus = (z - sqrt_disc) / 2
        zeta = np.where(np.abs(zeta_plus) > np.abs(zeta_minus), zeta_plus, zeta_minus)

    # Complex potential for horizontal flow
    with np.errstate(invalid='ignore', divide='ignore'):
        W = U * zeta + U * c**2 / zeta

    psi = np.imag(W)

    # Mask plate
    on_plate = (np.abs(Y) < 0.1) & (np.abs(X) <= a)
    psi[on_plate] = np.nan

    # Plot
    fig, ax = plt.subplots(figsize=(10, 12))
    psi_valid = psi[np.isfinite(psi)]
    levels = np.linspace(np.percentile(psi_valid, 2), np.percentile(psi_valid, 98), 40)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(levels)))

    for level, color in zip(levels, colors):
        ax.contour(X, Y, psi, levels=[level], colors=[color], linewidths=1.0)

    # Draw plate
    ax.plot([-a, a], [0, 0], 'k-', linewidth=3)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal')
    ax.set_title('Horizontal flow past horizontal plate - streamlines should be horizontal at edges')

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/test_horizontal.png',
                dpi=150, bbox_inches='tight')
    print("Saved test_horizontal.png")


if __name__ == "__main__":
    test_horizontal_plate()
