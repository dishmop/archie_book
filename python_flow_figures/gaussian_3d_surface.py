"""
3D Gaussian surface plot with rainbow coloring

Creates a bell-shaped surface colored by height from violet (low) to red (high).
Uses a single surface with discrete face colors for proper rendering.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap, BoundaryNorm


def gaussian_3d(x, y, amplitude=1.0, sigma=1.0):
    """2D Gaussian function."""
    r_sq = x**2 + y**2
    return amplitude * np.exp(-r_sq / (2 * sigma**2))


def plot_gaussian_surface(sigma=1.0, amplitude=1.5, n_bands=15, ngrid=200):
    """
    Plot a 3D Gaussian surface with discrete rainbow color bands.
    Uses a single surface with quantized colors for proper z-ordering.
    """
    # Create grid
    x = np.linspace(-2.5, 2.5, ngrid)
    y = np.linspace(-2.5, 2.5, ngrid)
    X, Y = np.meshgrid(x, y)

    # Compute Gaussian
    Z = gaussian_3d(X, Y, amplitude=amplitude, sigma=sigma)

    # Create figure
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Create discrete colormap
    base_cmap = plt.cm.rainbow
    colors = [base_cmap(i / (n_bands - 1)) for i in range(n_bands)]
    discrete_cmap = ListedColormap(colors)

    # Create boundaries for discrete colors
    boundaries = np.linspace(0, amplitude, n_bands + 1)
    norm = BoundaryNorm(boundaries, discrete_cmap.N)

    # Compute face colors based on Z values
    # For plot_surface, we need colors for each face (ngrid-1 x ngrid-1)
    Z_faces = (Z[:-1, :-1] + Z[1:, :-1] + Z[:-1, 1:] + Z[1:, 1:]) / 4
    face_colors = discrete_cmap(norm(Z_faces))

    # Plot single surface with face colors
    surf = ax.plot_surface(X, Y, Z, facecolors=face_colors,
                           linewidth=0, antialiased=False,
                           rstride=1, cstride=1, shade=False)

    # Adjust view angle to match the original image
    ax.view_init(elev=30, azim=45)

    # Remove axes for cleaner look
    ax.set_axis_off()

    # Set aspect ratio
    ax.set_box_aspect([1, 1, 0.8])

    # Adjust limits
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(0, amplitude * 1.1)

    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    fig, ax = plot_gaussian_surface(sigma=0.9, amplitude=1.8, n_bands=15, ngrid=300)

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/gaussian_3d_output.png',
                dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0)
    print("Saved gaussian_3d_output.png")
