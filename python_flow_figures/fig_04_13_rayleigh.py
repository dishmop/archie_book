"""
Fig 4.13 - Probability of energy/intensity vs radius

Shows the Rayleigh distribution: P(r) ∝ r * exp(-2r²/σ²)
This is the probability of finding a given intensity at radius r
from the origin in a 2D random walk (speckle pattern).
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def rayleigh_distribution(r, sigma=1.0):
    """
    Probability distribution P(r) ∝ r * exp(-2r²/σ²)
    """
    return r * np.exp(-2 * r**2 / sigma**2)


if __name__ == "__main__":
    # Create radius values
    r = np.linspace(0, 3, 500)

    # Compute probability
    sigma = 1.0
    P = rayleigh_distribution(r, sigma)

    # Normalize for display - reduce peak height to match original
    P = P / np.max(P) * 0.6

    # Create figure matching the style of the original - wider aspect ratio
    fig, ax = plt.subplots(figsize=(12, 5))

    # Plot the curve
    ax.plot(r, P, 'k-', linewidth=2)

    # Style to match original - simple axes with labels
    ax.set_xlabel('Radius', fontsize=16)
    ax.set_ylabel('Probability', fontsize=16)

    # Remove top and right spines, keep left and bottom
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # Remove tick marks but keep axis lines
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits - reduce vertical space
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 0.75)

    plt.tight_layout()

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/fig_04_13_output.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved fig_04_13_output.png")
