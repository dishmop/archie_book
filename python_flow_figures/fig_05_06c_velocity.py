"""
Fig 5.6c - Velocity distribution around a Joukowski airfoil

This shows the velocity distribution for flow with ZERO CIRCULATION.
This represents the initial startup flow before the Kutta condition is established.
The velocity has a sharp discontinuity/singularity at the trailing edge because
the flow must wrap around the sharp trailing edge.

Computes and plots the surface velocity distribution as a function of
arc length along the airfoil surface, starting from the trailing edge.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def joukowski_airfoil_velocity(c=1.0, offset_x=-0.1, offset_y=0.15, alpha_deg=8, U=1.0,
                                n_points=500, use_kutta=False):
    """
    Compute velocity distribution on a Joukowski airfoil surface.

    Parameters:
    - c: Joukowski parameter (trailing edge at x = 2c)
    - offset_x: x-offset of circle center (negative = thicker airfoil)
    - offset_y: y-offset of circle center (positive = cambered airfoil)
    - alpha_deg: angle of attack in degrees
    - U: freestream velocity
    - n_points: number of points on the airfoil surface
    - use_kutta: if False, use zero circulation (shows trailing edge singularity)

    Returns:
    - s: arc length along the surface (starting from trailing edge, going around upper surface)
    - V: velocity magnitude at each point
    - x_airfoil, y_airfoil: airfoil coordinates
    """
    alpha = np.radians(alpha_deg)

    # Circle parameters
    center = offset_x + 1j * offset_y
    R = abs(c - center)  # radius so circle passes through z=c

    # Circulation
    if use_kutta:
        # Kutta condition: smooth flow at trailing edge
        beta = np.arcsin(offset_y / R)
        Gamma = 4 * np.pi * U * R * np.sin(alpha + beta)
    else:
        # Zero circulation - shows the trailing edge singularity
        Gamma = 0

    # Points on the circle (in zeta-plane)
    # The original figure appears to start near the leading edge stagnation point
    # and go around to show the trailing edge singularity in the middle

    # Trailing edge is at zeta = c
    theta_te = np.angle(c - center)

    # Leading edge is opposite the trailing edge (approximately)
    theta_le = theta_te + np.pi

    # Start slightly before the stagnation point (which is shifted by angle of attack)
    # and go counterclockwise around the whole airfoil
    # Stagnation point on circle is where flow velocity = 0
    # For zero circulation, stagnation points are at theta = alpha and theta = pi + alpha
    # (where alpha is angle of attack)

    # For zero circulation flow past the offset circle, stagnation points
    # are at theta = alpha and theta = pi + alpha (in the shifted frame)
    #
    # Original figure shows: low velocity -> stagnation -> peak -> decrease -> spike
    # This corresponds to going counterclockwise starting just before the
    # stagnation point near the leading edge

    # Stagnation on circle is where velocity on circle = 0
    # For flow at angle alpha, stagnations are at theta_center + alpha and theta_center + pi + alpha
    # where theta_center = angle from center to a reference point

    # Start slightly before the leading-edge-side stagnation
    # Go in the OPPOSITE direction (clockwise) to flip the curve
    # Don't do a full loop - stop before returning to trailing edge singularity
    theta_start = theta_le + alpha + 0.12
    theta_end = theta_start - 1.90*np.pi  # Stop well before completing full circle
    theta = np.linspace(theta_start, theta_end, n_points)
    zeta = center + R * np.exp(1j * theta)

    # Map to airfoil (z-plane) via Joukowski transform
    z = zeta + c**2 / zeta
    x_airfoil = np.real(z)
    y_airfoil = np.imag(z)

    # Compute velocity on the circle surface
    # Complex velocity in circle plane: dW/dζ
    # W(ζ) = U*exp(-iα)*(ζ - center) + U*exp(iα)*R²/(ζ - center) + iΓ/(2π)*log(ζ - center)
    zeta_shifted = zeta - center

    # dW/dζ for the flow around the offset circle
    dW_dzeta = (U * np.exp(-1j*alpha) -
                U * np.exp(1j*alpha) * R**2 / zeta_shifted**2 +
                1j * Gamma / (2*np.pi) / zeta_shifted)

    # Velocity in z-plane: dW/dz = (dW/dζ) / (dz/dζ)
    # dz/dζ = 1 - c²/ζ²
    dz_dzeta = 1 - c**2 / zeta**2

    # At trailing edge, dz/dζ = 0 (the Joukowski singularity)
    # The velocity should remain finite due to Kutta condition (dW/dζ also → 0)

    with np.errstate(divide='ignore', invalid='ignore'):
        dW_dz = dW_dzeta / dz_dzeta

    # Velocity magnitude
    V = np.abs(dW_dz)

    # Handle the trailing edge singularity
    # At trailing edge, use L'Hopital's rule or just interpolate
    te_idx = 0  # trailing edge is at start
    if not np.isfinite(V[te_idx]):
        V[te_idx] = 0  # stagnation at trailing edge (Kutta condition)
    if not np.isfinite(V[-1]):
        V[-1] = 0

    # Compute arc length along the airfoil
    dx = np.diff(x_airfoil)
    dy = np.diff(y_airfoil)
    ds = np.sqrt(dx**2 + dy**2)
    s = np.concatenate([[0], np.cumsum(ds)])

    return s, V, x_airfoil, y_airfoil, theta


def plot_velocity_distribution(s, V, U=1.0, V_max=3.5):
    """
    Plot velocity distribution matching the style of the original figure.
    """
    fig, ax = plt.subplots(figsize=(10, 7))

    # Clip velocity for display (the singularity goes to infinity)
    V_display = np.clip(V, 0, V_max)

    # Main velocity curve (blue, labeled "1")
    ax.plot(s, V_display, 'b-', linewidth=1.5)

    # Freestream velocity line (yellow, labeled "2")
    ax.axhline(y=U, color='gold', linewidth=1.5)

    total_length = s[-1]

    # Add "1" labels on the blue curve at positions matching original
    label_s_1 = [0.8, 1.5, 2.5, 3.5, 4.5, 7.5, 9.0]
    for ls in label_s_1:
        idx = np.argmin(np.abs(s - ls))
        if V_display[idx] < V_max * 0.9 and V_display[idx] > 0.3:
            ax.annotate('1', (s[idx], V_display[idx]), textcoords="offset points",
                       xytext=(5, 8), ha='center', fontsize=10, color='gold')

    # Add "2" labels on the yellow line
    s_labels_2 = [0.3, 1.8, 3.0, 4.2, 8.0, 10.2]
    for sl in s_labels_2:
        ax.annotate('2', (sl, U), textcoords="offset points",
                   xytext=(0, 5), ha='center', fontsize=10, color='gold')

    # Red numbered markers along x-axis (positions on airfoil)
    # Match original: 1,2,3 near start, 4,5,6 in middle, 7 at spike, 1 at end
    marker_data = [(0.2, '1'), (0.5, '2'), (0.7, '3'), (1.5, '4'),
                   (3.0, '5'), (4.2, '6'), (5.5, '7'), (10.3, '1')]
    for mp, label in marker_data:
        ax.annotate(label, (mp, -0.08), ha='center', fontsize=10, color='red')

    ax.set_xlabel('Distance', fontsize=12)
    ax.set_ylabel('Velocity', fontsize=12)
    ax.set_xlim(0, total_length * 1.02)
    ax.set_ylim(0, V_max + 0.2)
    ax.grid(True, alpha=0.3)
    ax.tick_params(direction='in')

    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    # Joukowski airfoil parameters to match Fig 5.6
    # Left side should stay more level (around 1.0-1.2) before the spike
    # Less thickness and lower angle gives flatter velocity distribution
    c = 1.5  # scale to get airfoil from about -3 to 3
    offset_x = -0.15  # moderate thickness
    offset_y = 0.12   # some camber
    alpha_deg = 6     # lower angle for flatter upper surface velocity
    U = 1.0

    # Compute velocity distribution with ZERO CIRCULATION
    # This shows the startup flow before Kutta condition is established
    s, V, x_airfoil, y_airfoil, theta = joukowski_airfoil_velocity(
        c=c, offset_x=offset_x, offset_y=offset_y, alpha_deg=alpha_deg, U=U,
        n_points=1000, use_kutta=False)

    # Scale distance to match original figure (0 to ~11)
    s = s / s[-1] * 10.5

    # Don't clip - let the plot function handle display
    # The trailing edge singularity should show as a spike

    # Plot with capped display
    fig, ax = plot_velocity_distribution(s, V, U, V_max=3.5)

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/fig_05_06c_output.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved fig_05_06c_output.png")

    # Also save a diagnostic plot showing the airfoil shape
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(x_airfoil, y_airfoil, 'b-', linewidth=2)
    ax2.set_aspect('equal')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('Joukowski Airfoil Shape')
    ax2.grid(True, alpha=0.3)
    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/fig_05_06c_airfoil.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved fig_05_06c_airfoil.png")
