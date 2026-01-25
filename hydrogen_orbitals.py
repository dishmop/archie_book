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
    """
    m = k  # Bessel order = number of nodal diameters
    j_mn = BESSEL_ZEROS[m][n - 1]  # n-th zero of J_m

    # Radial part: Bessel function
    R = jv(m, j_mn * r)

    # Angular part: cosine for nodal diameters
    Theta = np.cos(m * theta)

    return R * Theta


def get_normalization(n, k):
    """Get normalization factor for a mode."""
    r_test = np.linspace(0.001, 1, 100)
    theta_test = np.linspace(0, 2 * np.pi, 100)
    R, T = np.meshgrid(r_test, theta_test)
    Z_test = membrane_mode(R, T, n, k)
    return np.max(np.abs(Z_test))


def create_membrane_surface(n, k, num_r=80, num_theta=160):
    """
    Generate the 3D surface mesh for a membrane vibration mode.
    """
    r = np.linspace(0, 1, num_r)
    theta = np.linspace(0, 2 * np.pi, num_theta)
    R, Theta = np.meshgrid(r, theta)

    Z = membrane_mode(R, Theta, n, k)
    norm = get_normalization(n, k)
    Z = Z / norm * 0.35

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    return X, Y, Z


def add_polar_grid(fig, n, k, num_circles=15, num_spokes=24, row=None, col=None):
    """
    Add polar grid lines (concentric circles and radial spokes) to the surface.
    """
    norm = get_normalization(n, k)
    line_color = 'rgb(0, 0, 0)'
    line_width = 2.5
    # Small offset to lift lines above surface
    z_offset = 0.005

    # Concentric circles (constant r)
    for r_val in np.linspace(0.08, 1.0, num_circles):
        theta_pts = np.linspace(0, 2 * np.pi, 200)
        z_pts = membrane_mode(r_val, theta_pts, n, k) / norm * 0.35 + z_offset

        x_pts = r_val * np.cos(theta_pts)
        y_pts = r_val * np.sin(theta_pts)

        trace = go.Scatter3d(
            x=x_pts, y=y_pts, z=z_pts,
            mode='lines',
            line=dict(color=line_color, width=line_width),
            showlegend=False,
            hoverinfo='skip'
        )
        if row is not None and col is not None:
            fig.add_trace(trace, row=row, col=col)
        else:
            fig.add_trace(trace)

    # Radial spokes (constant theta)
    for theta_val in np.linspace(0, 2 * np.pi, num_spokes, endpoint=False):
        r_pts = np.linspace(0, 1, 100)
        z_pts = membrane_mode(r_pts, theta_val, n, k) / norm * 0.35 + z_offset

        x_pts = r_pts * np.cos(theta_val)
        y_pts = r_pts * np.sin(theta_val)

        trace = go.Scatter3d(
            x=x_pts, y=y_pts, z=z_pts,
            mode='lines',
            line=dict(color=line_color, width=line_width),
            showlegend=False,
            hoverinfo='skip'
        )
        if row is not None and col is not None:
            fig.add_trace(trace, row=row, col=col)
        else:
            fig.add_trace(trace)


def create_single_mode_figure(n, k):
    """
    Create a Plotly figure for a single membrane mode with polar grid lines.
    """
    X, Y, Z = create_membrane_surface(n, k)

    fig = go.Figure()

    # Surface with grayscale shading
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        surfacecolor=Z,
        colorscale=[
            [0.0, 'rgb(80, 80, 80)'],
            [0.3, 'rgb(140, 140, 140)'],
            [0.5, 'rgb(190, 190, 190)'],
            [0.7, 'rgb(220, 220, 220)'],
            [1.0, 'rgb(255, 255, 255)']
        ],
        showscale=False,
        lighting=dict(
            ambient=0.6,
            diffuse=0.5,
            specular=0.15,
            roughness=0.8
        ),
        lightposition=dict(x=50, y=50, z=100)
    ))

    # Add polar grid lines
    add_polar_grid(fig, n, k, num_circles=15, num_spokes=24)

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


def create_2x2_figure():
    """
    Create a 2x2 grid of the four modes from the original image.
    """
    modes = [
        (1, 0, "n=1, k=0"),
        (2, 0, "n=2, k=0"),
        (1, 1, "n=1, k=1"),
        (2, 1, "n=2, k=1"),
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
                    [0.0, 'rgb(80, 80, 80)'],
                    [0.3, 'rgb(140, 140, 140)'],
                    [0.5, 'rgb(190, 190, 190)'],
                    [0.7, 'rgb(220, 220, 220)'],
                    [1.0, 'rgb(255, 255, 255)']
                ],
                showscale=False,
                lighting=dict(
                    ambient=0.6,
                    diffuse=0.5,
                    specular=0.15,
                    roughness=0.8
                ),
                lightposition=dict(x=50, y=50, z=100)
            ),
            row=row, col=col
        )

        # Add polar grid lines (15 circles, 24 spokes)
        add_polar_grid(fig, n, k, num_circles=15, num_spokes=24, row=row, col=col)

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

    fig = create_2x2_figure()
    fig.write_html("hydrogen_orbitals_combined.html")
    print("Saved: hydrogen_orbitals_combined.html")

    modes = [(1, 0), (2, 0), (1, 1), (2, 1)]
    for n, k in modes:
        fig = create_single_mode_figure(n, k)
        filename = f"orbital_n{n}_k{k}.html"
        fig.write_html(filename)
        print(f"Saved: {filename}")

    print("\nDone! Open the HTML files in a browser.")
    fig = create_2x2_figure()
    fig.show()
