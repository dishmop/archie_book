"""
Fig 5.7a - Flow around an airfoil with circulation

Uses uniform flow + doublet + vortex to create flow around a lifting body.
The doublet creates a closed streamline (body shape), and the vortex adds circulation.
The drawn airfoil shape is matched to the flow's stagnation streamline.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path


def compute_flow(U=1.0, kappa=4.0, Gamma=8.0, ngrid=600):
    """
    Compute stream function for uniform flow + doublet + vortex.

    Parameters:
    - U: freestream velocity
    - kappa: doublet strength (controls body size)
    - Gamma: circulation (positive = counterclockwise = lift up)
    """
    # Grid
    x = np.linspace(-4, 4, ngrid)
    y = np.linspace(-3, 5, ngrid)
    X, Y = np.meshgrid(x, y)

    r_sq = X**2 + Y**2
    r = np.sqrt(r_sq)

    # Stream function components:
    # Uniform flow: ψ = U*y
    # Doublet at origin: ψ = -κ*y/(2π*r²)
    # Vortex at origin: ψ = Γ/(2π)*ln(r)

    with np.errstate(divide='ignore', invalid='ignore'):
        psi = U * Y - kappa * Y / (2 * np.pi * r_sq) + Gamma / (2 * np.pi) * np.log(r)

    # The body boundary is where ψ = ψ_stagnation
    # For a cylinder with circulation, there's a stagnation point
    # Find it and mask interior

    # Stagnation streamline value: at the stagnation point on the body surface
    # For uniform flow + doublet + vortex, stagnation occurs where velocity = 0
    # This happens at r = a = sqrt(κ/(2πU)) for the doublet-only case
    a = np.sqrt(kappa / (2 * np.pi * U))

    # With circulation, stagnation point moves. Find ψ on the body (r = a)
    # At y = 0, x = -a (rear stagnation for zero circulation):
    # With circulation, it shifts. Let's use ψ at the rear of the body
    psi_body = Gamma / (2 * np.pi) * np.log(a)  # ψ on r=a, y=0

    # Mask interior (where r < a, approximately)
    inside = r < a * 0.95
    psi[inside] = np.nan

    return X, Y, psi, a, psi_body


def get_body_shape_from_streamline(U, kappa, Gamma, n_points=200):
    """
    Find the body shape by tracing the stagnation streamline.
    """
    a = np.sqrt(kappa / (2 * np.pi * U))

    # For a cylinder with circulation, the body is still approximately circular
    # but we can trace the actual streamline

    theta = np.linspace(0, 2*np.pi, n_points)
    # Start with circle of radius a
    x_body = a * np.cos(theta)
    y_body = a * np.sin(theta)

    return x_body, y_body


def create_flat_bottom_airfoil(chord=4.0, max_thickness=0.6, n_points=200):
    """
    Create an airfoil shape with curved top and flat bottom.
    This shape will be drawn on top of the flow field.
    """
    # Upper surface (from trailing edge to leading edge)
    t = np.linspace(0, 1, n_points // 2)
    x_upper = chord/2 - chord * t  # from chord/2 to -chord/2

    # Elliptical upper surface
    y_upper = max_thickness * np.sqrt(np.maximum(0, 1 - (x_upper / (chord/2))**2))

    # Lower surface (from leading edge to trailing edge)
    x_lower = -chord/2 + chord * t  # from -chord/2 to chord/2

    # Nearly flat - just slight curve at leading edge
    le_blend = np.exp(-((x_lower + chord/2) / (chord/6))**2)
    y_lower = -0.05 * max_thickness * le_blend

    # Combine
    x_airfoil = np.concatenate([x_upper, x_lower[1:]])
    y_airfoil = np.concatenate([y_upper, y_lower[1:]])

    return x_airfoil, y_airfoil


def compute_flow_around_airfoil(chord=4.0, thickness=0.6, camber=0.1, U=1.0, ngrid=600):
    """
    Compute flow around an airfoil using Joukowski transform.
    Allows for cambered (asymmetric) airfoils.
    """
    # Parameters for Joukowski circle
    # The circle center offset controls camber and thickness
    c = chord / 4  # Joukowski parameter

    # Offset to create camber (y-offset) and thickness (x-offset)
    # More y-offset = more camber (curved top, flatter bottom)
    # More negative x-offset = thicker leading edge
    offset_x = -0.15 * c  # more thickness for rounder leading edge
    offset_y = 0.30 * c   # more camber for flatter bottom appearance

    center = offset_x + 1j * offset_y
    R = abs(c - center)  # radius so circle passes through z=c

    # Grid
    x = np.linspace(-4, 4, ngrid)
    y = np.linspace(-3, 5, ngrid)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y

    # Inverse Joukowski: z = ζ + c²/ζ => ζ = (z ± sqrt(z² - 4c²))/2
    with np.errstate(invalid='ignore'):
        disc = z**2 - 4*c**2
        sqrt_disc = np.sqrt(disc)

        zeta_plus = (z + sqrt_disc) / 2
        zeta_minus = (z - sqrt_disc) / 2

        # Choose correct branch
        zeta = np.where(np.abs(zeta_plus - center) > np.abs(zeta_minus - center),
                        zeta_plus, zeta_minus)

    # Circulation for Kutta condition
    alpha = 0  # angle of attack
    beta = np.arcsin(offset_y / R)
    Gamma = 4 * np.pi * U * R * np.sin(alpha + beta)

    # Complex potential
    with np.errstate(invalid='ignore', divide='ignore'):
        zeta_shifted = zeta - center
        W = (U * np.exp(-1j*alpha) * zeta_shifted +
             U * np.exp(1j*alpha) * R**2 / zeta_shifted +
             1j * Gamma / (2*np.pi) * np.log(zeta_shifted))

    psi = np.imag(W)

    # Mask inside
    inside = np.abs(zeta - center) < R * 0.98
    psi[inside] = np.nan

    # Get airfoil shape from Joukowski mapping
    theta = np.linspace(0, 2*np.pi, 300)
    zeta_circle = center + R * np.exp(1j * theta)
    z_airfoil = zeta_circle + c**2 / zeta_circle
    x_airfoil = np.real(z_airfoil)
    y_airfoil = np.imag(z_airfoil)

    return X, Y, psi, x_airfoil, y_airfoil


def plot_flow(X, Y, psi, x_body, y_body, n_lines=50):
    """Plot with rainbow-colored streamlines."""

    fig, ax = plt.subplots(figsize=(10, 10))

    psi_valid = psi[np.isfinite(psi)]
    psi_max_data = np.percentile(psi_valid, 99)
    psi_min_data = np.percentile(psi_valid, 1)

    # Create evenly spaced levels with psi=0 as one of them
    interval = (psi_max_data - psi_min_data) / n_lines
    levels_negative = np.arange(0, psi_min_data - interval, -interval)[1:][::-1]
    levels_positive = np.arange(0, psi_max_data + interval, interval)[1:]
    levels = np.concatenate([levels_negative, [0.0], levels_positive])

    # Color mapping: psi=0 in blue region
    color_fracs = np.zeros(len(levels))
    for i, lev in enumerate(levels):
        if lev <= 0:
            color_fracs[i] = 0.2 * (lev - psi_min_data) / (0 - psi_min_data) if psi_min_data != 0 else 0.2
        else:
            color_fracs[i] = 0.2 + 0.8 * (lev - 0) / (psi_max_data - 0) if psi_max_data != 0 else 0.2

    colors = plt.cm.rainbow(color_fracs)

    for level, color in zip(levels, colors):
        ax.contour(X, Y, psi, levels=[level], colors=[color], linewidths=1.5, linestyles='solid')

    # Draw the airfoil
    ax.fill(x_body, y_body, 'white', edgecolor='black', linewidth=1.5, zorder=10)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 5)
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_aspect('equal')
    ax.tick_params(direction='in', labelsize=11)

    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    # Use Joukowski mapping for proper flow calculation
    # Adjust parameters to get a shape closer to the original
    X, Y, psi, x_airfoil, y_airfoil = compute_flow_around_airfoil(
        chord=4.0,
        thickness=0.6,
        camber=0.2,
        U=1.0,
        ngrid=600
    )

    fig, ax = plot_flow(X, Y, psi, x_airfoil, y_airfoil, n_lines=50)

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/fig_05_07a_output.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved fig_05_07a_output.png")
