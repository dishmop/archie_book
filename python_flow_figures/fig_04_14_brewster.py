"""
Fig 4.14 - Refracted and reflected rays with the direction of the electric field

Shows the Brewster angle phenomenon:
- Incident ray from upper left
- Reflected ray to upper right
- Refracted ray going into the material (below surface)
- Small arrows showing polarization direction (E-field)

At the Brewster angle, reflected and refracted rays are perpendicular (90°).
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyArrow
import matplotlib.patches as mpatches


def draw_ray_with_polarization(ax, start, end, pol_type='in_plane', color='black',
                                arrow_style='->', linewidth=1.5):
    """
    Draw a ray with polarization arrows.

    pol_type: 'in_plane' for arrows along ray direction (p-polarized)
              'out_of_plane' for dots/circles (s-polarized)
    """
    # Draw the main ray as an arrow
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=linewidth))

    # Calculate midpoint and perpendicular direction for polarization arrows
    mid = ((start[0] + end[0])/2, (start[1] + end[1])/2)

    # Unit vector along ray
    length = np.sqrt(dx**2 + dy**2)
    ux, uy = dx/length, dy/length

    # Perpendicular unit vector (for in-plane polarization shown perpendicular to ray)
    px, py = -uy, ux

    # Draw polarization indicator
    arrow_len = 0.15

    if pol_type == 'in_plane':
        # Double-headed arrow perpendicular to ray direction
        # This represents E-field oscillating in the plane of incidence
        p1 = (mid[0] - px*arrow_len, mid[1] - py*arrow_len)
        p2 = (mid[0] + px*arrow_len, mid[1] + py*arrow_len)

        # Draw double-headed arrow
        ax.annotate('', xy=p2, xytext=p1,
                    arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))

    return mid, (px, py)


def create_brewster_diagram():
    """Create a clear diagram of reflection and refraction at Brewster angle."""

    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the interface (horizontal line)
    ax.axhline(y=0, color='black', linewidth=2, xmin=0.05, xmax=0.95)

    # Angles (Brewster angle for glass n=1.5 is about 56.3 degrees)
    # At Brewster angle: tan(theta_B) = n2/n1
    n1, n2 = 1.0, 1.5
    theta_B = np.arctan(n2/n1)  # Brewster angle ~56.3 degrees
    theta_i = theta_B  # incident angle = Brewster angle
    theta_r = theta_i  # reflected angle = incident angle
    theta_t = np.arcsin(n1/n2 * np.sin(theta_i))  # Snell's law for refracted angle

    # Origin at interface
    origin = (0.5, 0)

    # Ray length
    ray_len = 0.35

    # Calculate ray endpoints
    # Incident ray (coming from upper left)
    inc_start = (origin[0] - ray_len*np.sin(theta_i),
                 origin[1] + ray_len*np.cos(theta_i))
    inc_end = origin

    # Reflected ray (going to upper right)
    ref_start = origin
    ref_end = (origin[0] + ray_len*np.sin(theta_r),
               origin[1] + ray_len*np.cos(theta_r))

    # Refracted ray (going into material, downward)
    trans_start = origin
    trans_end = (origin[0] + ray_len*np.sin(theta_t),
                 origin[1] - ray_len*np.cos(theta_t))

    # Draw rays with arrows
    lw = 2.0

    # Incident ray
    ax.annotate('', xy=inc_end, xytext=inc_start,
                arrowprops=dict(arrowstyle='->', color='black', lw=lw))

    # Reflected ray
    ax.annotate('', xy=ref_end, xytext=ref_start,
                arrowprops=dict(arrowstyle='->', color='black', lw=lw))

    # Refracted ray
    ax.annotate('', xy=trans_end, xytext=trans_start,
                arrowprops=dict(arrowstyle='->', color='black', lw=lw))

    # Add polarization arrows (double-headed, perpendicular to ray)
    arrow_len = 0.06

    def add_polarization_arrows(start, end, offset_frac=0.5):
        """Add a double-headed polarization arrow perpendicular to the ray."""
        # Point along the ray
        px = start[0] + offset_frac * (end[0] - start[0])
        py = start[1] + offset_frac * (end[1] - start[1])

        # Direction of ray
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = np.sqrt(dx**2 + dy**2)

        # Perpendicular direction
        perp_x = -dy / length
        perp_y = dx / length

        # Draw double-headed arrow
        ax.annotate('',
                    xy=(px + perp_x*arrow_len, py + perp_y*arrow_len),
                    xytext=(px - perp_x*arrow_len, py - perp_y*arrow_len),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))

    # Add polarization to each ray
    add_polarization_arrows(inc_start, inc_end, 0.35)
    add_polarization_arrows(inc_start, inc_end, 0.65)
    add_polarization_arrows(ref_start, ref_end, 0.4)
    add_polarization_arrows(ref_start, ref_end, 0.7)
    add_polarization_arrows(trans_start, trans_end, 0.4)
    add_polarization_arrows(trans_start, trans_end, 0.7)

    # Draw normal (dashed vertical line)
    ax.plot([origin[0], origin[0]], [-0.3, 0.4], 'k--', linewidth=1, alpha=0.5)

    # Add angle arcs
    arc_radius = 0.1

    # Incident angle arc
    theta_arc_i = np.linspace(np.pi/2, np.pi/2 + theta_i, 30)
    ax.plot(origin[0] + arc_radius*np.cos(theta_arc_i),
            origin[1] + arc_radius*np.sin(theta_arc_i), 'k-', linewidth=1)

    # Reflected angle arc
    theta_arc_r = np.linspace(np.pi/2 - theta_r, np.pi/2, 30)
    ax.plot(origin[0] + arc_radius*np.cos(theta_arc_r),
            origin[1] + arc_radius*np.sin(theta_arc_r), 'k-', linewidth=1)

    # Refracted angle arc
    theta_arc_t = np.linspace(-np.pi/2, -np.pi/2 + theta_t, 30)
    ax.plot(origin[0] + arc_radius*np.cos(theta_arc_t),
            origin[1] + arc_radius*np.sin(theta_arc_t), 'k-', linewidth=1)

    # Add labels - positioned away from the rays
    # Incident ray label - top left
    ax.text(inc_start[0] - 0.02, inc_start[1] + 0.02, 'Incident', fontsize=12, ha='right')

    # Reflected ray label - top right
    ax.text(ref_end[0] + 0.02, ref_end[1] + 0.02, 'Reflected', fontsize=12, ha='left')

    # Refracted ray label - bottom right
    ax.text(trans_end[0] + 0.02, trans_end[1] - 0.02, 'Refracted', fontsize=12, ha='left')

    # Style - tighter bounds around the diagram
    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(-0.35, 0.42)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout(pad=0.1)
    return fig, ax


if __name__ == "__main__":
    fig, ax = create_brewster_diagram()

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/fig_04_14_output.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved fig_04_14_output.png")
