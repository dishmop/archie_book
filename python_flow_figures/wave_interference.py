"""
Two-source wave interference pattern

Creates the classic interference pattern from two coherent point sources,
showing constructive and destructive interference.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def wave_interference(source1, source2, wavelength=1.0, amplitude=1.0, ngrid=800):
    """
    Compute interference pattern from two point sources.

    Parameters:
    - source1, source2: (x, y) positions of the two sources
    - wavelength: wavelength of the waves
    - amplitude: wave amplitude
    - ngrid: grid resolution
    """
    # Create grid
    x = np.linspace(-10, 10, ngrid)
    y = np.linspace(-10, 10, ngrid)
    X, Y = np.meshgrid(x, y)

    # Distance from each source
    r1 = np.sqrt((X - source1[0])**2 + (Y - source1[1])**2)
    r2 = np.sqrt((X - source2[0])**2 + (Y - source2[1])**2)

    # Wave number
    k = 2 * np.pi / wavelength

    # Waves from each source with 1/sqrt(r) decay (correct for 2D cylindrical waves)
    with np.errstate(divide='ignore', invalid='ignore'):
        wave1 = amplitude * np.cos(k * r1) / np.sqrt(r1 + 0.3)
        wave2 = amplitude * np.cos(k * r2) / np.sqrt(r2 + 0.3)

    # Superposition
    total = wave1 + wave2

    return X, Y, total


def plot_interference(X, Y, wave_field):
    """Plot the interference pattern in grayscale."""

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot as grayscale image
    # Normalize to 0-1 range
    vmax = np.percentile(np.abs(wave_field), 99)

    ax.imshow(wave_field, extent=[X.min(), X.max(), Y.min(), Y.max()],
              cmap='gray', vmin=-vmax, vmax=vmax, origin='lower')

    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    # Two sources positioned like in the original image
    # The original shows sources on the left side, waves propagating right
    source1 = (-5, 1.8)   # upper source
    source2 = (-5, -1.8)  # lower source

    # Wavelength - smaller wavelength gives more rings
    wavelength = 0.9

    # Compute interference with higher resolution for crisp lines
    X, Y, wave_field = wave_interference(source1, source2, wavelength=wavelength, ngrid=1200)

    # Plot
    fig, ax = plot_interference(X, Y, wave_field)

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/wave_interference_output.png',
                dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0)
    print("Saved wave_interference_output.png")
