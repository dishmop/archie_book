"""
Fig 5.4 - Potential flow around an inclined flat plate

CORRECT APPROACH:
1. Work in plate-aligned coordinates where plate is on x-axis from -a to a
2. Far-field flow is horizontal in PHYSICAL coords, which means it comes at angle α
   in plate coords (since plate is tilted by α)
3. Use Joukowski with angle +α (not -α) to get ψ∞ = U*(x sinα + y cosα) = U*y_physical
4. Rotate back to physical coordinates for plotting

The key insight: W = U*exp(iα)*ζ + U*exp(-iα)*c²/ζ gives far-field ψ = U*y_physical.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator


def compute_flow_in_plate_coords(a=2.0, alpha_deg=28, U=1.0, ngrid=800):
    """
    Compute stream function in plate-aligned coordinates.

    The plate is horizontal (on x-axis from -a to a).
    The far-field flow, when viewed in physical coords, is horizontal.
    In plate coords, this means streamlines tilt at angle α.
    """
    c = a / 2  # Joukowski parameter
    alpha = np.radians(alpha_deg)

    # Large grid to allow for rotation
    x = np.linspace(-10, 10, ngrid)
    y = np.linspace(-10, 10, ngrid)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y

    # Use elliptic coordinates which naturally handle the flat plate geometry
    # For a plate from -a to a on the x-axis:
    # Elliptic coords (μ, ν) defined by: x = a*cosh(μ)*cos(ν), y = a*sinh(μ)*sin(ν)
    #
    # Inverse: given (x, y), find (μ, ν)
    # r1 = sqrt((x+a)² + y²), r2 = sqrt((x-a)² + y²)
    # cosh(μ) = (r1 + r2)/(2a), cos(ν) = (r1 - r2)/(2a)

    r1 = np.sqrt((X + a)**2 + Y**2)
    r2 = np.sqrt((X - a)**2 + Y**2)

    # Elliptic coordinate μ (radial-like, μ=0 on plate)
    cosh_mu = np.clip((r1 + r2) / (2*a), 1.0, None)
    mu = np.arccosh(cosh_mu)

    # Elliptic coordinate ν (angular, 0 to π above plate, -π to 0 below)
    cos_nu = np.clip((r1 - r2) / (2*a), -1.0, 1.0)
    nu = np.arccos(cos_nu)
    # Make ν negative below the x-axis for continuity
    nu = np.where(Y < 0, -nu, nu)

    # For horizontal flow (in physical coords) past an inclined plate:
    # After rotation, we want ψ → U*y_physical at infinity
    # y_physical = x*sin(α) + y*cos(α) in plate coords
    #
    # The stream function that:
    # 1. Has plate (μ=0) as streamline ψ=0
    # 2. Has stagnation points at plate edges (ν=0 and ν=π)
    # 3. Gives horizontal flow at infinity after rotation
    #
    # ψ = U*a*sinh(μ)*sin(ν + α)
    #
    # At plate edges (μ→0): ψ → 0 regardless of ν (since sinh(0)=0)
    # So the stagnation streamline ψ=0 runs along the PLATE, not through its tips.
    #
    # For stagnation points AT the tips, we need ψ=0 to approach the tips from the flow.
    # This requires a different formulation. The stagnation streamline in physical
    # coords is ψ = U*y_stagnation where y_stagnation is the y-value of incoming flow
    # that hits the plate.
    #
    # Actually, for an inclined flat plate in uniform flow, stagnation points ARE at
    # the plate edges, and the stagnation streamline ψ=ψ_stag connects them.
    # The value ψ_stag is NOT zero - it's the streamline that arrives at the plate.

    psi = U * a * np.sinh(mu) * np.sin(nu + alpha)

    return X, Y, psi


def rotate_to_physical_coords(X_plate, Y_plate, psi_plate, a, alpha_deg, ngrid_out=600):
    """
    Rotate from plate-aligned coords to physical coords.

    Plate coords: plate is horizontal
    Physical coords: plate is tilted at angle α (upper-left to lower-right for α > 0)

    Transform: x_phys = x_plate*cos(α) - y_plate*sin(α)
               y_phys = x_plate*sin(α) + y_plate*cos(α)

    To find ψ at physical point (x_p, y_p), we find the corresponding plate coords:
               x_plate = x_phys*cos(α) + y_phys*sin(α)
               y_plate = -x_phys*sin(α) + y_phys*cos(α)
    """
    alpha = np.radians(alpha_deg)
    cos_a, sin_a = np.cos(alpha), np.sin(alpha)

    # Physical coordinate grid
    x_phys = np.linspace(-4, 4, ngrid_out)
    y_phys = np.linspace(-5, 5, ngrid_out)
    X_phys, Y_phys = np.meshgrid(x_phys, y_phys)

    # Find corresponding plate coordinates
    X_plt = X_phys * cos_a + Y_phys * sin_a
    Y_plt = -X_phys * sin_a + Y_phys * cos_a

    # Interpolate
    x_vals = X_plate[0, :]
    y_vals = Y_plate[:, 0]

    # Interpolate - psi_plate should have no NaN now
    interp = RegularGridInterpolator((y_vals, x_vals), psi_plate,
                                      bounds_error=False, fill_value=0.0)

    points = np.stack([Y_plt.ravel(), X_plt.ravel()], axis=-1)
    psi_phys = interp(points).reshape(X_phys.shape)

    return X_phys, Y_phys, psi_phys


def plot_flow(X, Y, psi, a, alpha_deg, n_lines=40):
    """Plot with rainbow-colored streamlines."""
    alpha = np.radians(alpha_deg)
    cos_a, sin_a = np.cos(alpha), np.sin(alpha)

    fig, ax = plt.subplots(figsize=(10, 12))

    psi_valid = psi[np.isfinite(psi)]
    # We want the plate (around y=0, psi≈0) to be in the BLUE region
    # Rainbow colormap: violet(0) -> blue(0.2) -> cyan(0.4) -> green(0.5) -> yellow(0.7) -> red(1)
    #
    # Strategy: use full data range for levels, but stretch/shift the colormap
    # so that psi=0 maps to blue while keeping full color range

    # Get the actual data range
    psi_max_data = np.percentile(psi_valid, 99)
    psi_min_data = np.percentile(psi_valid, 1)

    # Create evenly spaced levels with psi=0 as one of them
    # All other streamlines should be evenly spaced around psi=0
    interval = (psi_max_data - psi_min_data) / n_lines
    # Generate levels going negative from 0
    levels_negative = np.arange(0, psi_min_data - interval, -interval)[1:][::-1]  # exclude 0, will add it back
    # Generate levels going positive from 0
    levels_positive = np.arange(0, psi_max_data + interval, interval)[1:]  # exclude 0
    # Combine: negative levels + psi=0 + positive levels
    levels = np.concatenate([levels_negative, [0.0], levels_positive])

    # For each level, compute what color it should get
    # We want: psi_min_data -> violet (0), psi=0 -> blue (0.2), psi_max_data -> red (1)
    # This requires a non-linear mapping
    #
    # Simple approach: linearly interpolate in two segments
    # Segment 1: psi_min to 0 maps to color 0 to 0.2
    # Segment 2: 0 to psi_max maps to color 0.2 to 1.0

    color_fracs = np.zeros(len(levels))
    for i, lev in enumerate(levels):
        if lev <= 0:
            # Map [psi_min, 0] to [0, 0.2]
            color_fracs[i] = 0.2 * (lev - psi_min_data) / (0 - psi_min_data) if psi_min_data != 0 else 0.2
        else:
            # Map [0, psi_max] to [0.2, 1.0]
            color_fracs[i] = 0.2 + 0.8 * (lev - 0) / (psi_max_data - 0) if psi_max_data != 0 else 0.2

    # Rainbow colormap
    colors = plt.cm.rainbow(color_fracs)

    for level, color in zip(levels, colors):
        cs = ax.contour(X, Y, psi, levels=[level], colors=[color], linewidths=1.5, linestyles='solid')

    # Draw the inclined plate
    # Plate endpoints in plate coords: (-a, 0) and (a, 0)
    # In physical coords: (-a*cos α, -a*sin α) and (a*cos α, a*sin α)
    p1 = np.array([-a * cos_a, -a * sin_a])
    p2 = np.array([a * cos_a, a * sin_a])

    # Plate direction and normal
    dx, dy = p2 - p1
    length = np.hypot(dx, dy)
    nx, ny = -dy/length, dx/length

    thickness = 0.07
    corners = np.array([
        p1 - thickness * np.array([nx, ny]),
        p2 - thickness * np.array([nx, ny]),
        p2 + thickness * np.array([nx, ny]),
        p1 + thickness * np.array([nx, ny]),
    ])
    ax.fill(corners[:, 0], corners[:, 1], 'white', edgecolor='black', linewidth=1.5, zorder=10)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_aspect('equal')
    ax.tick_params(direction='in', labelsize=11)

    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    plate_half_length = 2.0
    plate_angle = -25  # degrees, negative = upper-left to lower-right (like original)

    # Step 1: Compute in plate coordinates
    X_plate, Y_plate, psi_plate = compute_flow_in_plate_coords(
        a=plate_half_length, alpha_deg=plate_angle, U=1.0, ngrid=800)

    # Step 2: Rotate to physical coordinates
    X_phys, Y_phys, psi_phys = rotate_to_physical_coords(
        X_plate, Y_plate, psi_plate, plate_half_length, plate_angle, ngrid_out=600)

    # Step 3: Plot
    fig, ax = plot_flow(X_phys, Y_phys, psi_phys, plate_half_length, plate_angle, n_lines=50)

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/fig_05_04_output.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved fig_05_04_output.png")
