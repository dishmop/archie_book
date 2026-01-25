#!/usr/bin/env python3
"""Rename remaining files with special characters."""
import os
import shutil

folder = "/Users/diarmidcampbell/Desktop/Archies book project/archie book figures"

# Mapping of old filenames to new filenames
renames = {
    "13_2. A structure with Poisson's ratio.svg": "fig_13_02.svg",
    "13_7a_The Challenger disaster. (a) The aftermath of the explosion and (b) the join and 'O' ring seal.jpg": "fig_13_07a.jpg",
    "13_7b_The Challenger disaster. (b) the join and 'O' ring seal.jpg": "fig_13_07b.jpg",
    "1_12_It is curious that with a left-handed thread the left pedal of a bicycle pedal doesn't come loose.svg": "fig_01_12.svg",
    "2_3_Heaviside's circuit model of a cable, which now appears in every undergraduate course of electrical engineering.  The parameters per unit length are a resistance R, an inductance L, a capacitance C and a leakage conductance G.svg": "fig_02_03.svg",
    "3_3_The earth orbiting the moon and the moon orbiting the earth.  Note that the centre of gravity is actually within the radius of the Earth, but it's shown here outside the Earth for clarity.svg": "fig_03_03.svg",
    "3_9a_The components and resultant accelerations at four points on the earth's surface. (a) Accelerations relative to the earth due to the forces from the moon.svg": "fig_03_09a.svg",
    "3_9b_The components and resultant accelerations at four points on the earth's surface (b) accelerations resolved tangential and radial to the surface.svg": "fig_03_09b.svg",
    "3_9c_The components and resultant accelerations at four points on the earth's surface. (c) Tangential components are responsible for moving water on the surface of the earth.svg": "fig_03_09c.svg",
    "4_7_Crepuscular Rays in St Peter's Basilica, Rome (Wikipaedia).jpeg": "fig_04_07.jpeg",
    "5_6c_The flow around an airfoil with zero circulation (c) Velocity around the airfoil's surface from A to D and back to A.svg": "fig_05_06c.svg",
    "5_7c_The flow around an airfoil with circulation, c = 4.8 (c) Velocity around the airfoil's surface.png": "fig_05_07c.png",
    "6_2_Hertz's Apparatus.svg": "fig_06_02.svg",
    "6_3a_de Forest's investigation of the use of flames as a detector.png": "fig_06_03a.png",
    "6_3b_de Forest's investigation of the use of flames as a detector.png": "fig_06_03b.png",
    "6_3c_de Forest's investigation of the use of flames as a detector.png": "fig_06_03c.png",
    "7_1a_Schrodinger's cat- Simultaneously dead and alive.jpg": "fig_07_01a.jpg",
    "7_1b_Schrodinger's cat- Simultaneously dead and alive.png": "fig_07_01b.png",
    "9_10_The boiler chimney at the Cheddar's Lane Industrial Museum, Cambridge.jpg": "fig_09_10.jpg",
    '9_15_Flow round a cylinder spinning clockwise, depicting "back spin" of a ball moving from right to left. Relative to the ball, flow is from left to right.svg': "fig_09_15.svg",
    "9_20b_Trying to suck out a candle. (b) The vorticity moves to the left and the candle doesn't notice any change..png": "fig_09_20b.png",
    '9_3c_There is no pressure drop across parallel streamlines. (c) Where flow comes to rest we have a "stagnation point" S where the where the stagnation pressure ps = po + ½ρv2,where v is the flow velocity.svg': "fig_09_03c.svg",
}

os.chdir(folder)

for old_name, new_name in renames.items():
    if os.path.exists(old_name):
        try:
            os.rename(old_name, new_name)
            print(f"Renamed: {old_name[:40]}... -> {new_name}")
        except Exception as e:
            print(f"Error renaming {old_name[:40]}...: {e}")
    else:
        print(f"Not found: {old_name[:40]}...")

print("\nRemaining non-fig files:")
for f in sorted(os.listdir(".")):
    if not f.startswith("fig_") and not f.startswith("."):
        print(f"  {f}")
