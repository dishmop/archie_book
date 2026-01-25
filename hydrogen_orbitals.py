"""
Vibration modes of a circular membrane (drum head).
Shows displacement surfaces for different mode numbers.

Based on the wave equation solution using Bessel functions:
z(r, θ, t) = J_m(k_{m,n} r) * cos(m*θ) * cos(ω t)

Where:
- m = number of nodal diameters (angular nodes)
- n = which zero of the Bessel function J_m (radial mode number)
- J_m is the Bessel function of order m
- k_{m,n} = j_{m,n} / a where j_{m,n} is the n-th zero of J_m

The original image uses notation (n, k) where:
- n corresponds to radial mode (which Bessel zero)
- k corresponds to angular mode (Bessel order m)
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.special import jv  # Bessel functions of the first kind


# Zeros of Bessel functions J_m(x) = 0
# j_{m,n} is the n-th positive zero of J_m
# Index: BESSEL_ZEROS[m][n-1] gives j_{m,n}
BESSEL_ZEROS = {
    0: [2.4048, 5.5201, 8.6537, 11.7915],   # Zeros of J_0
    1: [3.8317, 7.0156, 10.1735, 13.3237],  # Zeros of J_1
    2: [5.1356, 8.4172, 11.6198, 14.7960],  # Zeros of J_2
}


def membrane_mode(r, theta, n, k):
    """
    Calculate the displacement of a circular membrane for mode (n, k).

    Using the image's notation:
    - n = radial mode number (which zero of Bessel function, n=1,2,3...)
    - k = angular mode number (number of nodal diameters, k=0,1,2...)

    The displacement is:
    z(r, θ) = J_k(j_{k,n} * r/a) * cos(k * θ)

    where j_{k,n} is the n-th zero of J_k, and a=1 (unit radius).
    """
    m = k  # Bessel order = number of nodal diameters
    j_mn = BESSEL_ZEROS[m][n - 1]  # n-th zero of J_m

    # Radial part: Bessel function
    R = jv(m, j_mn * r)

    # Angular part: cosine for nodal diameters
    Theta = np.cos(m * theta)

    return R * Theta


def create_membrane_surface(n, k, num_r=60, num_theta=120):
    """
    Generate the 3D surface mesh for a membrane vibration mode.

    Parameters:
    - n: radial mode number (1, 2, 3, ...)
    - k: angular mode number / nodal diameters (0, 1, 2, ...)
    - num_r: number of radial points
    - num_theta: number of angular points

    Returns X, Y, Z arrays for the surface.
    """
    # Create polar coordinate grid
    r = np.linspace(0, 1, num_r)
    theta = np.linspace(0, 2 * np.pi, num_theta)
    R, Theta = np.meshgrid(r, theta)

    # Calculate displacement
    Z = membrane_mode(R, Theta, n, k)

    # Normalize and scale for good visualization
    Z = Z / np.max(np.abs(Z)) * 0.35

    # Convert to Cartesian
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    return X, Y, Z


def create_single_mode_figure(n, k, show_wireframe=True):
    """
    Create a Plotly figure for a single membrane mode.
    """
    X, Y, Z = create_membrane_surface(n, k)

    fig = go.Figure()

    # Surface with grayscale shading based on height
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        surfacecolor=Z,  # Color by height
        colorscale=[
            [0.0, 'rgb(40, 40, 40)'],      # Dark gray for low points
            [0.25, 'rgb(100, 100, 100)'],
            [0.5, 'rgb(180, 180, 180)'],   # Mid gray
            [0.75, 'rgb(220, 220, 220)'],
            [1.0, 'rgb(255, 255, 255)']    # White for high points
        ],
        showscale=False,
        lighting=dict(
            ambient=0.7,
            diffuse=0.4,
            specular=0.1,
            roughness=0.9
        ),
        lightposition=dict(x=0, y=0, z=100)
    ))

    if show_wireframe:
        # Add wireframe grid lines
        add_wireframe(fig, n, k)

    # Layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, showbackground=False),
            yaxis=dict(visible=False, showbackground=False),
            zaxis=dict(visible=False, showbackground=False),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.4),
            camera=dict(
                eye=dict(x=1.3, y=1.3, z=0.9),
                up=dict(x=0, y=0, z=1)
            )
        ),
        paper_bgcolor='white',
        margin=dict(l=0, r=0, t=40, b=0),
        title=dict(
            text=f"n={n}, k={k}",
            x=0.5,
            font=dict(size=18, color='black')
        ),
        width=600,
        height=500
    )

    return fig


def add_wireframe(fig, n, k, num_r_lines=10, num_theta_lines=24, row=None, col=None):
    """
    Add wireframe grid lines to the figure.
    """
    # Concentric circles (constant r)
    for r_val in np.linspace(0.1, 1.0, num_r_lines):
        theta_pts = np.linspace(0, 2 * np.pi, 100)
        r_pts = np.full_like(theta_pts, r_val)
        z_pts = membrane_mode(r_pts, theta_pts, n, k)
        z_pts = z_pts / np.max(np.abs(membrane_mode(
            np.linspace(0.01, 1, 50)[:, np.newaxis],
            np.linspace(0, 2*np.pi, 50)[np.newaxis, :],
            n, k
        ))) * 0.35

        x_pts = r_val * np.cos(theta_pts)
        y_pts = r_val * np.sin(theta_pts)

        trace = go.Scatter3d(
            x=x_pts, y=y_pts, z=z_pts,
            mode='lines',
            line=dict(color='rgba(30, 30, 30, 0.6)', width=1.5),
            showlegend=False,
            hoverinfo='skip'
        )
        if row is not None and col is not None:
            fig.add_trace(trace, row=row, col=col)
        else:
            fig.add_trace(trace)

    # Radial lines (constant theta)
    for theta_val in np.linspace(0, 2 * np.pi, num_theta_lines, endpoint=False):
        r_pts = np.linspace(0, 1, 50)
        theta_pts = np.full_like(r_pts, theta_val)
        z_pts = membrane_mode(r_pts, theta_pts, n, k)
        z_pts = z_pts / np.max(np.abs(membrane_mode(
            np.linspace(0.01, 1, 50)[:, np.newaxis],
            np.linspace(0, 2*np.pi, 50)[np.newaxis, :],
            n, k
        ))) * 0.35

        x_pts = r_pts * np.cos(theta_val)
        y_pts = r_pts * np.sin(theta_val)

        trace = go.Scatter3d(
            x=x_pts, y=y_pts, z=z_pts,
            mode='lines',
            line=dict(color='rgba(30, 30, 30, 0.6)', width=1.5),
            showlegend=False,
            hoverinfo='skip'
        )
        if row is not None and col is not None:
            fig.add_trace(trace, row=row, col=col)
        else:
            fig.add_trace(trace)


def create_2x2_figure():
    """
    Create a 2x2 grid of the four modes from the original image:
    - (n=1, k=0): fundamental mode, simple dome
    - (n=2, k=0): second radial mode, one nodal circle
    - (n=1, k=1): first angular mode, one nodal diameter
    - (n=2, k=1): combined mode, one nodal diameter + one nodal circle
    """
    # The four modes to display
    modes = [
        (1, 0, "n=1, k=0"),   # Top-left
        (2, 0, "n=2, k=0"),   # Top-right
        (1, 1, "n=1, k=1"),   # Bottom-left
        (2, 1, "n=2, k=1"),   # Bottom-right
    ]

    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{'type': 'scene'}, {'type': 'scene'}],
               [{'type': 'scene'}, {'type': 'scene'}]],
        subplot_titles=[m[2] for m in modes],
        horizontal_spacing=0.02,
        vertical_spacing=0.08
    )

    positions = [(1, 1), (1, 2), (2, 1), (2, 2)]

    for idx, (n, k, label) in enumerate(modes):
        row, col = positions[idx]
        X, Y, Z = create_membrane_surface(n, k)

        # Add surface
        fig.add_trace(
            go.Surface(
                x=X, y=Y, z=Z,
                surfacecolor=Z,
                colorscale=[
                    [0.0, 'rgb(40, 40, 40)'],
                    [0.25, 'rgb(100, 100, 100)'],
                    [0.5, 'rgb(180, 180, 180)'],
                    [0.75, 'rgb(220, 220, 220)'],
                    [1.0, 'rgb(255, 255, 255)']
                ],
                showscale=False,
                lighting=dict(
                    ambient=0.7,
                    diffuse=0.4,
                    specular=0.1,
                    roughness=0.9
                ),
                lightposition=dict(x=0, y=0, z=100)
            ),
            row=row, col=col
        )

        # Add wireframe
        add_wireframe(fig, n, k, num_r_lines=8, num_theta_lines=20, row=row, col=col)

    # Common scene settings
    scene_settings = dict(
        xaxis=dict(visible=False, showbackground=False),
        yaxis=dict(visible=False, showbackground=False),
        zaxis=dict(visible=False, showbackground=False),
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=0.4),
        camera=dict(
            eye=dict(x=1.3, y=1.3, z=0.9),
            up=dict(x=0, y=0, z=1)
        )
    )

    fig.update_layout(
        scene=scene_settings,
        scene2=scene_settings,
        scene3=scene_settings,
        scene4=scene_settings,
        paper_bgcolor='white',
        height=900,
        width=1000,
        title=dict(
            text="Circular Membrane Vibration Modes",
            x=0.5,
            font=dict(size=20)
        ),
        margin=dict(l=20, r=20, t=80, b=20)
    )

    return fig


if __name__ == "__main__":
    print("Generating circular membrane vibration modes...")
    print()
    print("Mode notation (n, k):")
    print("  n = radial mode number (which zero of Bessel function)")
    print("  k = number of nodal diameters (Bessel function order)")
    print()

    # Create combined 2x2 figure
    fig = create_2x2_figure()
    fig.write_html("hydrogen_orbitals_combined.html")
    print("Saved: hydrogen_orbitals_combined.html")

    # Create individual figures
    modes = [(1, 0), (2, 0), (1, 1), (2, 1)]
    for n, k in modes:
        fig = create_single_mode_figure(n, k)
        filename = f"orbital_n{n}_k{k}.html"
        fig.write_html(filename)
        print(f"Saved: {filename}")

    print()
    print("Done! Open the HTML files in a browser.")

    # Show the combined figure
    fig = create_2x2_figure()
    fig.show()
