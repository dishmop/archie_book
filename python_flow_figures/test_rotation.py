"""
Test rotation approach properly.

If I have flow past a horizontal plate with ψ = U*y far from the plate,
and I want to tilt the PLATE while keeping the flow horizontal at infinity,
I should NOT rotate the solution.

Instead, I should compute flow at angle α to a horizontal plate, which gives
the streamlines going diagonally past the plate, then the plate appears
inclined when viewed from the horizontal.

Actually, let me think about this differently:

Original figure shows:
- Flow horizontal at infinity (streamlines horizontal far from plate)
- Plate inclined (upper-left to lower-right)
- Streamlines curve around the plate

This is flow past an inclined plate. The far-field is STILL uniform horizontal flow.

If I rotate coordinates by angle α:
- Original horizontal streamline y = const becomes the curve x*sin(α) + y*cos(α) = const
- That's NOT a horizontal line!

So rotating the coordinate system does NOT give horizontal streamlines at infinity.

The correct approach: compute the flow in coordinates where the plate is horizontal,
but the FAR-FIELD FLOW is horizontal in the ORIGINAL (unrotated) coordinates.

In plate-aligned coordinates (rotated by α), the far-field flow comes at angle α
from the horizontal (plate direction).

So I need: flow at angle α past a horizontal plate. NOT flow parallel to a horizontal plate.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def flow_at_angle_past_horizontal_plate(a=2.0, alpha_deg=28, U=1.0, ngrid=600):
    """
    Flow at angle alpha past a horizontal plate.

    Far-field velocity is (U*cos(α), U*sin(α)) - NOT horizontal.
    But we want FAR-FIELD HORIZONTAL, plate inclined.

    That means: in plate coordinates, far-field comes at angle α.
    """
    c = a / 2
    alpha = np.radians(alpha_deg)

    x = np.linspace(-4, 4, ngrid)
    y = np.linspace(-5, 5, ngrid)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y

    # Inverse Joukowski
    with np.errstate(invalid='ignore'):
        disc = z**2 - 4*c**2
        sqrt_disc = np.sqrt(disc)
        zeta = np.where(np.abs(z + sqrt_disc) > np.abs(z - sqrt_disc),
                        (z + sqrt_disc)/2, (z - sqrt_disc)/2)

    # Flow at angle α past circle:
    # W(ζ) = U*exp(-iα)*ζ + U*exp(iα)*c²/ζ
    with np.errstate(invalid='ignore', divide='ignore'):
        W = U * np.exp(-1j*alpha) * zeta + U * np.exp(1j*alpha) * c**2 / zeta

    psi = np.imag(W)

    # Mask
    on_plate = (np.abs(Y) < 0.1) & (np.abs(X) <= a)
    psi[on_plate] = np.nan

    return X, Y, psi


def flow_correctly(a=2.0, alpha_deg=28, U=1.0, ngrid=600):
    """
    Correctly compute flow where:
    - Far field is HORIZONTAL (ψ → U*y_physical)
    - Plate is inclined at angle α

    Key: work in plate-aligned coordinates where plate is horizontal.
    The physical y-direction (vertical) becomes y*cos(α) - x*sin(α) in plate coords.
    So ψ_∞ = U * (y*cos(α) - x*sin(α)) = U * (-x*sin(α) + y*cos(α)) in plate coords.

    Wait, that's still not U*y_physical. Let me redo the coordinate transform.

    Physical coords: (x_p, y_p) with y_p vertical, x_p horizontal.
    Plate coords: (x, y) where plate lies along x-axis, rotated by α from physical.

    Transform: x_p = x*cos(α) - y*sin(α)
               y_p = x*sin(α) + y*cos(α)

    So y_p = x*sin(α) + y*cos(α).

    At infinity, ψ = U*y_p = U*(x*sin(α) + y*cos(α)) in plate coords.

    Now, decompose the far-field velocity in plate coords:
    u = ∂ψ/∂y = U*cos(α)  (along plate)
    v = -∂ψ/∂x = -U*sin(α)  (normal to plate, into lower half)

    So the flow approaches at angle -α to the plate (coming from below-left if α > 0).

    Actually, wait. Let me be more careful.
    ψ = U*y_p = U*(x*sin α + y*cos α)
    u = ∂ψ/∂y = U*cos α  (velocity in +y direction in plate coords, i.e., perpendicular to plate going up)
    v = -∂ψ/∂x = -U*sin α  (velocity in +x direction in plate coords, i.e., along plate going left)

    Hmm, this gives velocity (-U sin α, U cos α) in plate coords, which has magnitude U
    and points at angle 90° - α from plate direction. That's angle α from vertical, i.e.,
    the flow is coming from the left, tilted down by α from horizontal in physical coords.
    Wait no, that's not horizontal either.

    Let me reconsider. In physical coordinates, horizontal flow means ψ = U*y_p.
    I want to express this stream function in plate coordinates.

    Given the rotation: (x_p, y_p) -> (x, y) where
        x = x_p*cos α + y_p*sin α
        y = -x_p*sin α + y_p*cos α

    Inverting:
        x_p = x*cos α - y*sin α
        y_p = x*sin α + y*cos α

    So ψ = U*y_p = U*(x*sin α + y*cos α) in plate coordinates.

    The complex potential whose imaginary part is this:
    Let z = x + iy (plate coords). Then
    ψ = U*(sin α * Re(z) + cos α * Im(z)) = U * Im(z*exp(iα))
    So W = U*z*exp(iα) works for uniform flow.

    But this doesn't satisfy the plate boundary condition (ψ = const on plate).
    We need the plate from -a to a to be a streamline.

    For the plate on y=0 from x=-a to x=a:
    ψ = U*x*sin α on the plate, which varies with x. So the plate isn't a streamline of uniform flow!

    This means potential flow past an inclined plate in uniform flow
    has the plate NOT as a single streamline. The flow splits at both ends.
    """
    c = a / 2
    alpha = np.radians(alpha_deg)

    x = np.linspace(-4, 4, ngrid)
    y = np.linspace(-5, 5, ngrid)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y

    # The stream function that gives horizontal flow at infinity AND
    # makes the plate a streamline.
    #
    # Uniform flow part: ψ_uniform = U*y_physical = U*(x*sin α + y*cos α)
    # Perturbation part: must cancel to make plate a streamline
    #
    # For a plate from -a to a on the x-axis, we need:
    # ψ(x, 0) = U*x*sin α + ψ_pert(x, 0) = const for |x| < a
    #
    # The perturbation for flow perpendicular to a plate is:
    # W_pert = -i*V*sqrt(z² - a²) gives ψ_pert = -V * Im(i*sqrt(z² - a²))
    #
    # Actually let's use the Joukowski result directly.
    # For flow at angle α past a horizontal plate, W = U*exp(-iα)*ζ + U*exp(iα)*c²/ζ
    # where ζ is the circle-plane coordinate.
    #
    # At infinity: W → U*exp(-iα)*z (since ζ → z for large z with Joukowski)
    # So ψ∞ = U*Im(exp(-iα)*z) = U*Im((cos α - i sin α)*(x + iy))
    #       = U*(y*cos α - x*sin α)
    #
    # But I want ψ∞ = U*(x*sin α + y*cos α)!
    #
    # These are different. For the Joukowski formula, the far-field flow is at angle α,
    # meaning velocity in direction (cos α, sin α). But for physical horizontal flow past
    # an inclined plate, the velocity is (1, 0).
    #
    # The Joukowski formula for angle α gives ψ∞ = U*(-x sin α + y cos α)
    # Physical horizontal flow gives ψ∞ = U*y_p = U*(x sin α + y cos α)
    #
    # The difference is in the sign of the x term.
    # Joukowski angle α: ψ = -Ux sin α + Uy cos α = U*Im(z*exp(-iα))
    # Physical horizontal: ψ = Ux sin α + Uy cos α = U*Im(z*exp(iα))
    #
    # So for physical horizontal flow, I need angle -α in the Joukowski formula!

    with np.errstate(invalid='ignore'):
        disc = z**2 - 4*c**2
        sqrt_disc = np.sqrt(disc)
        zeta = np.where(np.abs(z + sqrt_disc) > np.abs(z - sqrt_disc),
                        (z + sqrt_disc)/2, (z - sqrt_disc)/2)

    # Use angle -α in Joukowski to get horizontal far-field
    with np.errstate(invalid='ignore', divide='ignore'):
        W = U * np.exp(1j*alpha) * zeta + U * np.exp(-1j*alpha) * c**2 / zeta

    psi = np.imag(W)

    # Verify: at infinity, W → U*exp(iα)*z, so
    # ψ∞ = U*Im(exp(iα)*z) = U*Im((cos α + i sin α)*(x + iy))
    #    = U*(sin α * x + cos α * y) = U*y_physical ✓

    on_plate = (np.abs(Y) < 0.1) & (np.abs(X) <= a)
    psi[on_plate] = np.nan

    return X, Y, psi


if __name__ == "__main__":
    a = 2.0
    alpha = 28

    X, Y, psi = flow_correctly(a, alpha)

    fig, ax = plt.subplots(figsize=(10, 12))
    psi_valid = psi[np.isfinite(psi)]
    levels = np.linspace(*np.percentile(psi_valid, [2, 98]), 40)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(levels)))

    for level, color in zip(levels, colors):
        ax.contour(X, Y, psi, levels=[level], colors=[color], linewidths=1.0)

    ax.plot([-a, a], [0, 0], 'k-', linewidth=3)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('plate-aligned x')
    ax.set_ylabel('plate-aligned y')
    ax.set_aspect('equal')
    ax.set_title(f'Flow with horizontal far-field, plate horizontal in these coords\n'
                 f'Streamlines should tilt down-right at {alpha}° at infinity')

    plt.savefig('/Users/diarmidcampbell/Desktop/Archies book project/python_flow_figures/test_correct.png',
                dpi=150, bbox_inches='tight')
    print("Saved test_correct.png")
