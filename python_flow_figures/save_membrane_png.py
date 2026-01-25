"""
Save the membrane vibration modes figure as a PNG image.
Uses kaleido for static image export from Plotly.
"""

import subprocess
import sys

# First ensure kaleido is installed
try:
    import kaleido
except ImportError:
    print("Installing kaleido for PNG export...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kaleido"])

from hydrogen_orbitals import create_2x2_figure

def save_as_png(filename="membrane_modes.png", scale=2):
    """
    Save the 2x2 membrane modes figure as a PNG.

    Parameters:
    - filename: output filename
    - scale: resolution multiplier (2 = 2x resolution)
    """
    print("Creating figure...")
    fig = create_2x2_figure()

    print(f"Saving to {filename}...")
    fig.write_image(filename, scale=scale, width=900, height=800)

    print(f"Done! Saved as {filename}")
    return filename

if __name__ == "__main__":
    save_as_png("membrane_modes.png", scale=2)
