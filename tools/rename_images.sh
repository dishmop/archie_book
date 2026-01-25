#!/bin/bash
# Image Renaming Script for OUP Book Submission
# This script renames images from long descriptive names to short fig_CC_NN format

cd "/Users/diarmidcampbell/Desktop/Archies book project/archie book figures"

# Create backup directory
mkdir -p "../archie_book_figures_backup"
cp -r . "../archie_book_figures_backup/"

echo "Backup created in archie_book_figures_backup/"
echo "Starting rename process..."

# Chapter 1
mv "1_1_hydraulic-capstan-c-and-a-musker-ltd-1901-ef69b9.jpg" "fig_01_01.jpg" 2>/dev/null
mv "1_2_With rope over a single-wheel pulley.  A net full of fish would be too heavy to lift.svg" "fig_01_02.svg" 2>/dev/null
mv "1_3_Wrap the rope around a rotating cylinder and it becomes easy to lift heavy loads.svg" "fig_01_03.svg" 2>/dev/null
mv "1_4_A rope round a rotating cylinder making contact around a small arc dθ, the tension increases by a small amount dT on account of friction.svg" "fig_01_04.svg" 2>/dev/null
mv "1_5a_Forces and velocities on a locked wheel. (a) Car moving forward with velocity v.svg" "fig_01_05a.svg" 2>/dev/null
mv "1_5b_Forces and velocities on a locked wheel. (b) diagram showing the road moving relative to the wheel.svg" "fig_01_05b.svg" 2>/dev/null
mv "1_6_(a) Frictional and centrifugal force on a turning car.svg" "fig_01_06a.svg" 2>/dev/null
mv "1_6_(b) The forces if the hand brake is applied.svg" "fig_01_06b.svg" 2>/dev/null
mv "1_7_The principle of Ackerman steering. All wheels rotate round the same point. This cyclist is borderline safe in this illustration.svg" "fig_01_07.svg" 2>/dev/null
mv "1_8_The Geometry of Ackerman steering.  The linkage creates the angles shown in Fig 1.7.svg" "fig_01_08.svg" 2>/dev/null
mv "1_9a_The Ackerman design isn't perfect but it works pretty well.  Ideally x will always be equal to x0, but this only happens exactly at φ=48 degrees.svg" "fig_01_09a.svg" 2>/dev/null
mv "1_9b_The Ackerman design isn't perfect but it works pretty well.  Ideally x will always be equal to x0, but this only happens exactly at φ=48 degrees.svg" "fig_01_09b.svg" 2>/dev/null
mv "1_10_(a)  φ = 16.png" "fig_01_10a.png" 2>/dev/null
mv "1_10_(b) φ = 48.png" "fig_01_10b.png" 2>/dev/null
mv "1_11_An epicyclic or planetary gear.jpg" "fig_01_11.jpg" 2>/dev/null
mv "1_12_It is curious that with a left-handed thread the left pedal of a bicycle pedal doesn't come loose.svg" "fig_01_12.svg" 2>/dev/null
mv "1_13_The right side bicycle pedal.svg" "fig_01_13.svg" 2>/dev/null
mv "1_14a_Exaggerated clearance between the crank and pedal threads.svg" "fig_01_14a.svg" 2>/dev/null
mv "1_14b_Exaggerated clearance between the crank and pedal threads.svg" "fig_01_14b.svg" 2>/dev/null
mv "1_14c_Exaggerated clearance between the crank and pedal threads.svg" "fig_01_14c.svg" 2>/dev/null
mv "1_15a_The R-L circuit model of a dynamo and the voltage generated for slow and fast cycling.svg" "fig_01_15a.svg" 2>/dev/null
mv "1_15b_The R-L circuit model of a dynamo and the voltage generated for slow and fast cycling.svg" "fig_01_15b.svg" 2>/dev/null

# Chapter 2
mv "2_1a_A sub-ocean cable.jpg" "fig_02_01a.jpg" 2>/dev/null
mv "2_1b_A sub-ocean cable.webp" "fig_02_01b.webp" 2>/dev/null
mv "2_2_The Great Eastern setting out from Ireland trailing the Cable. The pulses were broadened significantly on arrival and Kelvin explained this by treating the cable as a distributed R-C circuit.  About six to eight words per minute could be sent.jpg" "fig_02_02.jpg" 2>/dev/null
mv "2_3_Heaviside's circuit model of a cable, which now appears in every undergraduate course of electrical engineering.  The parameters per unit length are a resistance R, an inductance L, a capacitance C and a leakage conductance G.svg" "fig_02_03.svg" 2>/dev/null
mv "2_4_The input and output voltage of a rectangular unit pulse lasting 0.1 seconds. A 1 volt input voltage for 0.1 seconds (red) and the result at the far end of the cable (blue).png" "fig_02_04.png" 2>/dev/null
mv "2_5_A typical received signal (1922 Scientific American).jpg" "fig_02_05.jpg" 2>/dev/null
mv "2_6_The calculated decay length in metres for an ADSL line as a function of frequency,  . The decay length is the distance at which the signal whill have dropped to 37% of its original amplitude.png" "fig_02_06.png" 2>/dev/null
mv "2_7_The electrostatics of a charge and a conducting sphere.svg" "fig_02_07.svg" 2>/dev/null
mv "2_8_Current flowing from a sphere in an infinite conducting medium.png" "fig_02_08.png" 2>/dev/null
mv "2_9a_A cow.jpg" "fig_02_09a.jpg" 2>/dev/null
mv "2_9b a cow equivalent circuit.png" "fig_02_09b.png" 2>/dev/null
mv "2_9c_a human with legs together.png" "fig_02_09c.png" 2>/dev/null

# Chapter 3
mv "3_1a_The Normandy landings.   Note that the tide is very low.JPG" "fig_03_01a.jpg" 2>/dev/null
mv "3_1b_The Normandy landings.   Note that the tide is very low.jpg" "fig_03_01b.jpg" 2>/dev/null
mv "3_2_The centrifugal:centripetal force debate.png" "fig_03_02.png" 2>/dev/null
mv "3_3_The earth orbiting the moon and the moon orbiting the earth.  Note that the centre of gravity is actually within the radius of the Earth, but it's shown here outside the Earth for clarity.svg" "fig_03_03.svg" 2>/dev/null
mv "3_4_Bulge in levels of water as due to the difference in forces experienced on either side of the earth.svg" "fig_03_04.svg" 2>/dev/null
mv "3_5_Three masses initially in contact and after a time t.svg" "fig_03_05.svg" 2>/dev/null
mv "3_6_The pressure gradient in curved stream-lines.svg" "fig_03_06.svg" 2>/dev/null
mv "3_7_Distances between the earth and moon used to calculate the height of tides using pressure.svg" "fig_03_07.svg" 2>/dev/null
mv "3_8_Distances between the earth and moon used to calculate the height of tides using acceleration. The accelerations at P and O with the vector distances are shown.svg" "fig_03_08.svg" 2>/dev/null
mv "3_9a_The components and resultant accelerations at four points on the earth's surface. (a) Accelerations relative to the earth due to the forces from the moon.svg" "fig_03_09a.svg" 2>/dev/null
mv "3_9b_The components and resultant accelerations at four points on the earth's surface (b) accelerations resolved tangential and radial to the surface.svg" "fig_03_09b.svg" 2>/dev/null
mv "3_9c_The components and resultant accelerations at four points on the earth's surface. (c) Tangential components are responsible for moving water on the surface of the earth.svg" "fig_03_09c.svg" 2>/dev/null
mv "3_10_The acceleration is balanced by gravity at a slope ψ.png" "fig_03_10.png" 2>/dev/null

# Chapter 4
mv "4_1_Slinky spring.jpg" "fig_04_01.jpg" 2>/dev/null
mv "4_2_The Wren Library.jpg" "fig_04_02.jpg" 2>/dev/null
mv "4_3_Speckled laser light.jpg" "fig_04_03.jpg" 2>/dev/null
mv "4_4_Crepuscular rays at sunset.jpg" "fig_04_04.jpg" 2>/dev/null
mv "4_5_Cloud Shadows imaged from above (NASA photograph).jpg" "fig_04_05.jpg" 2>/dev/null
mv "4_6_Anticrepuscular rays (Wikipedia).jpg" "fig_04_06.jpg" 2>/dev/null
mv "4_7_Crepuscular Rays in St Peter's Basilica, Rome (Wikipaedia).jpeg" "fig_04_07.jpeg" 2>/dev/null
mv "4_8a_Fresnel theory. (a) Plane waves of light can be represented by a number of point sources along the wavefront.svg" "fig_04_08a.svg" 2>/dev/null
mv "4_8b_Fresnel theory.(b) Diffraction through an aperture.png" "fig_04_08b.png" 2>/dev/null
mv "4_10_The polarisation pattern around the sun.jpeg" "fig_04_10.jpeg" 2>/dev/null
mv "4_11_Laser light multiply scattered by particles gives rise to a random distribution of intensity.png" "fig_04_11.png" 2>/dev/null
mv "4_12_The Mexican Hat function.png" "fig_04_12.png" 2>/dev/null
mv "4_13_Variation of energy intensity with distance from the origin.png" "fig_04_13.png" 2>/dev/null
mv "4_14_Refracted and reflected rays with the direction of the electric field.png" "fig_04_14.png" 2>/dev/null

# Chapter 5
mv "5_1a_The Airbus 380.jpeg" "fig_05_01a.jpeg" 2>/dev/null
mv "5_1b_The Airbus 380.jpeg" "fig_05_01b.jpeg" 2>/dev/null
mv "5_2a_Flow around a flat sheet for the case of zero viscosity. (a) the flow underneath the sheet is forced to curve but the flow above is unaltered.svg" "fig_05_02a.svg" 2>/dev/null
mv "5_2b_Flow around a flat sheet for the case of zero viscosity. (b)  pressure distribution along the dotted line (ABC), showing high pressure under the sheet which generates lift.svg" "fig_05_02b.svg" 2>/dev/null
mv "5_3a_Flow around a flat sheet with viscosity. (a) The flow underneath and above the sheet is forced to curve.svg" "fig_05_03a.svg" 2>/dev/null
mv "5_3b_Flow around a flat sheet with viscosity(b)  Pressure distribution along the dotted line (ABC), showing high pressure under the sheet and low pressure above the sheet, which generates more lift.svg" "fig_05_03b.svg" 2>/dev/null
mv "5_4_Potential flow round a sheet. Lift and drag are zero.png" "fig_05_04.png" 2>/dev/null
mv "5_5_Flow round a rotating cylinder.svg" "fig_05_05.svg" 2>/dev/null
mv "5_6a_The flow around an airfoil with zero circulation (a), overview of the flow.svg" "fig_05_06a.svg" 2>/dev/null
mv "5_6b_The flow around an airfoil with zero circulation. (b) Close-up of the trailing edge noting that the flow is unrealistic.svg" "fig_05_06b.svg" 2>/dev/null
mv "5_6c_The flow around an airfoil with zero circulation (c) Velocity around the airfoil's surface from A to D and back to A.svg" "fig_05_06c.svg" 2>/dev/null
mv "5_7a_The flow around an airfoil with circulation, c = 4.8 (a), overview of the flow.png" "fig_05_07a.png" 2>/dev/null
mv "5_7b_The flow around an airfoil with circulation, c = 4.8 (b) Close-up of the trailing edge noting that the discontinuity has disappeared.png" "fig_05_07b.png" 2>/dev/null
mv "5_7c_The flow around an airfoil with circulation, c = 4.8 (c) Velocity around the airfoil's surface.png" "fig_05_07c.png" 2>/dev/null
mv "5_8a_Flow around a wing with a flap with (a), c =0.png" "fig_05_08a.png" 2>/dev/null
mv "5_8b_Flow around a wing with a flap with (b) c = 6.1.png" "fig_05_08b.png" 2>/dev/null
mv "5_9_Streamlines in the ground effect.png" "fig_05_09.png" 2>/dev/null
mv "5_10a_A boat sailing into the wind. (a) a boat moving with velocity v against a wind with velocity w.svg" "fig_05_10a.svg" 2>/dev/null
mv "5_10b_A boat sailing into the wind. (b) The velocity of the wind relative to the boat vw_b is obtained by vector subtraction.svg" "fig_05_10b.svg" 2>/dev/null
mv "5_10c_A boat sailing into the wind. (c) the wind moving around the curved sail generates a force f normal to the sail with components fv in the direction of the boat velocity and fk, which is a force resisted by the keel.svg" "fig_05_10c.svg" 2>/dev/null
mv "5_11a_A boat sailing downwind faster than the wind (a) the boat moves with velocity v with a wind with velocity w.svg" "fig_05_11a.svg" 2>/dev/null
mv "5_11b_A boat sailing downwind faster than the wind (b) The velocity of the wind relative to the boat vw_b is obtained by vector subtraction.svg" "fig_05_11b.svg" 2>/dev/null
mv "5_11c_A boat sailing downwind faster than the wind (c) Even though the boat is moving faster than the wind, there is still a force in the direction of the boat.svg" "fig_05_11c.svg" 2>/dev/null
mv "5_12_Potential flow round a sail.png" "fig_05_12.png" 2>/dev/null

# Chapter 6
mv "6_1a_The wireless, then and now.avif" "fig_06_01a.avif" 2>/dev/null
mv "6_1b_The wireless, then and now.webp" "fig_06_01b.webp" 2>/dev/null
mv "6_2_Hertz's Apparatus.svg" "fig_06_02.svg" 2>/dev/null
mv "6_3a_de Forest's investigation of the use of flames as a detector.png" "fig_06_03a.png" 2>/dev/null
mv "6_3b_de Forest's investigation of the use of flames as a detector.png" "fig_06_03b.png" 2>/dev/null
mv "6_3c_de Forest's investigation of the use of flames as a detector.png" "fig_06_03c.png" 2>/dev/null
mv "6_4a_The triode valve.jpg" "fig_06_04a.jpg" 2>/dev/null
mv "6_4b_The triode valve.png" "fig_06_04b.png" 2>/dev/null
mv "6_5a_The basic triode valve. (a) Principal components, anode, heated cathode and wire mesh.svg" "fig_06_05a.svg" 2>/dev/null
mv "6_5b_The basic triode valve. (b) Analysis using image charges.svg" "fig_06_05b.svg" 2>/dev/null
mv "6_6_A complete triode amplifier.svg" "fig_06_06.svg" 2>/dev/null

# Chapter 7
mv "7_1a_Schrodinger's cat- Simultaneously dead and alive.jpg" "fig_07_01a.jpg" 2>/dev/null
mv "7_1b_Schrodinger's cat- Simultaneously dead and alive.png" "fig_07_01b.png" 2>/dev/null
mv "7_2_price of petrol.svg" "fig_07_02.svg" 2>/dev/null
mv "7_3_log vapour pressure plotted against 1:T.png" "fig_07_03.png" 2>/dev/null
mv "7_4a_Electrons moving around an atom exhibit a characteristic wave function. (a) For a single atom, this is a sinewave whose half wavelength is the diameter of the orbit.svg" "fig_07_04a.svg" 2>/dev/null
mv "7_4b_Electrons moving around an atom exhibit a characteristic wave function. (b) For a molecule or metallic bond, the electrons have access to a wider volume hence the wavelength is longer.svg" "fig_07_04b.svg" 2>/dev/null
mv "7_5_drum.jpg" "fig_07_05a.jpg" 2>/dev/null
mv "7_5_drum.png" "fig_07_05b.png" 2>/dev/null

# Chapter 8
mv "8_1_garmin-gps-38.jpg" "fig_08_01.jpg" 2>/dev/null
mv "8_2_Two satellites A and B. Circles are shown on the surface of the Earth, the perimeters of which have equal signal arrival times from each of the satellites.png" "fig_08_02.png" 2>/dev/null
mv "8_3_gps projection.svg" "fig_08_03.svg" 2>/dev/null
mv "8_4_A solution on a plane for three satellites.  The three solid circles show constant arrival times for three satellites.  Two solutions are possible.jpeg" "fig_08_04.jpeg" 2>/dev/null

# Chapter 9
mv "9_1a_Barnes Wallis and his Dambusters.jpg" "fig_09_01a.jpg" 2>/dev/null
mv "9_1b_Mohne_Dam_Breached.jpg" "fig_09_01b.jpg" 2>/dev/null
mv "9_2_The pressure gradient in curved streamlines.svg" "fig_09_02.svg" 2>/dev/null
mv "9_3a_There is no pressure drop across parallel streamlines. (a) the pressure in the side passage at B is the same as the flow pressure at A.svg" "fig_09_03a.svg" 2>/dev/null
mv "9_3b_There is no pressure drop across parallel streamlines. (b) the pressure at the exit of a tube at B is the same as the pressure inside the tube at A and also the same as the outside pressure at C.svg" "fig_09_03b.svg" 2>/dev/null
mv 9_3c_There\ is\ no\ pressure\ drop\ across\ parallel\ streamlines.\ \(c\)\ Where\ flow\ comes\ to\ rest\ we\ have\ a\ \"stagnation\ point\"\ S\ where\ the\ where\ the\ stagnation\ pressure\ ps\ =\ po\ +\ ½ρv2,where\ v\ is\ the\ flow\ velocity.svg "fig_09_03c.svg" 2>/dev/null
mv "9_4a_Streamlines around a cylinder. (a) The arrows show the direction of the pressure gradient due to centrifugal force.png" "fig_09_04a.png" 2>/dev/null
mv "9_4b_Streamlines around a cylinder. (b) The gauge pressure around the cylinder; red is positive blue is negative.png" "fig_09_04b.png" 2>/dev/null
mv "9_5a_A diagram of pitot-static tube.svg" "fig_09_05a.svg" 2>/dev/null
mv "9_5b_a pitot-static tube under an aircraft wing.webp" "fig_09_05b.webp" 2>/dev/null
mv "9_6a_The Coanda effect blowing over a sheet of paper. (a) For flow in a straight line the pressures at A and B are the same. Flow over a curved surfa. As we saw in Figure 2, this result in a region of low pressure which pulls the flow downwards.svg" "fig_09_06a.svg" 2>/dev/null
mv "9_6b_The Coanda effect blowing over a sheet of paper. (b) the resulting flow follows the surface. With curved streamlines, the pressure at A is lower than at B, causing lift.svg" "fig_09_06b.svg" 2>/dev/null
mv "9_7a_Examples of the Coanda effect. (a) a ping-pong ball levitated using a hairdryer.jpg" "fig_09_07a.jpg" 2>/dev/null
mv "9_7a_Examples of the Coanda effect. (b) a representation of the flow showing the curved streamlines with the centre line of the original flow shown dashed.jpg" "fig_09_07b.jpg" 2>/dev/null
mv "9_7c_Examples of the Coanda effect. (c) Water being curved by a spoon.jpg" "fig_09_07c.jpg" 2>/dev/null
mv "9_7d_Examples of the Coanda effect. (d) The same effect is responsible for dribbly teapots.jpg" "fig_09_07d.jpg" 2>/dev/null
mv "9_8_A steam injector .svg" "fig_09_08.svg" 2>/dev/null
mv "9_9a_A sand casting.  (a) Church bells are commonly fabricated using sand casting.jpg" "fig_09_09a.jpg" 2>/dev/null
mv "9_9b_A sand casting. (b) molten iron is poured into a mould created from sand, but care is needed to prevent entrainment of air from the sand into the molten metal which affects the quality of the finished product.webp" "fig_09_09b.webp" 2>/dev/null
mv "9_10_The boiler chimney at the Cheddar's Lane Industrial Museum, Cambridge.jpg" "fig_09_10.jpg" 2>/dev/null
mv "9_11a_(a) An illustration of a furnace and chimney. (b) The weight of hot air in the chimney is much less than the equivalent column outside.jpg" "fig_09_11a.jpg" 2>/dev/null
mv "9_11b_(b) The weight of hot air in the chimney is much less than the equivalent column outside.svg" "fig_09_11b.svg" 2>/dev/null
mv "9_12a_(a) Two cylinders in a wide flow.svg" "fig_09_12a.svg" 2>/dev/null
mv "9_12b_(b) Two cylinders in a jet.svg" "fig_09_12b.svg" 2>/dev/null
mv "9_13a_(a) A perfume atomiser.jpg" "fig_09_13a.jpg" 2>/dev/null
mv "9_13b_(b) Entrainment draws liquid out of vessel.png" "fig_09_13b.png" 2>/dev/null
mv "9_13c_(c) Low pressure in Vena Contracta (Bernoulli) draws liquid out of the vessel.png" "fig_09_13c.png" 2>/dev/null
mv "9_14a_Examples of levitation. (a) A ball in a funnel.png" "fig_09_14a.png" 2>/dev/null
mv "9_14b_Examples of levitation. (b) a disc levitated using a vacuum cleaner blowing through a hole in a second disc.svg" "fig_09_14b.svg" 2>/dev/null
mv "9_14c_Examples of levitation. (c) a circular card lifted by blowing through a cotton reel.svg" "fig_09_14c.svg" 2>/dev/null
mv "9_14d_Examples of levitation. (d) the flow lines.svg" "fig_09_14d.svg" 2>/dev/null
mv 9_15_Flow\ round\ a\ cylinder\ spinning\ clockwise,\ depicting\ \"back\ spin\"\ of\ a\ ball\ moving\ from\ right\ to\ left.\ Relative\ to\ the\ ball,\ flow\ is\ from\ left\ to\ right.svg "fig_09_15.svg" 2>/dev/null
mv "9_16a_(a) The Bosphorus runs between the Mediterranean and the Black Sea.svg" "fig_09_16a.svg" 2>/dev/null
mv "9_16b_(b) Cross-section through the Bosphorus.png" "fig_09_16b.png" 2>/dev/null
mv "9_17_Kilimanjaro.jpg" "fig_09_17.jpg" 2>/dev/null
mv "9_18a_(a) a fast-moving river.avif" "fig_09_18a.avif" 2>/dev/null
mv "9_18b_(b) It is easier to move from B to A by going along the bank first.png" "fig_09_18b.png" 2>/dev/null
mv "9_18c_(c) An array of vortices can be averaged to give a surface current and vice-versa..png" "fig_09_18c.png" 2>/dev/null
mv "9_19a_Blowing out a candle. (a) We start with potential flow.png" "fig_09_19a.png" 2>/dev/null
mv "9_19b_Blowing out a candle. (b) Vorticity forms an eddy.png" "fig_09_19b.png" 2>/dev/null
mv "9_19c_Blowing out a candle. (c) This produces a jet of air.png" "fig_09_19c.png" 2>/dev/null
mv "9_20a_Trying to suck out a candle. (a) We start Fig.18 (a), potential flow with the velocities reversed.png" "fig_09_20a.png" 2>/dev/null
mv "9_20b_Trying to suck out a candle. (b) The vorticity moves to the left and the candle doesn't notice any change..png" "fig_09_20b.png" 2>/dev/null

# Chapter 10
mv "10_1_Eric Laithwaite giving his 1974 Royal Institution Christmas Lectures.png" "fig_10_01.png" 2>/dev/null
mv "10_2a_(a) A trolley is moving along.svg" "fig_10_02a.svg" 2>/dev/null
mv "10_2a_(b) In time t the trolley has move.png" "fig_10_02b.png" 2>/dev/null
mv "10_3_A depression crossing north Britain.gif" "fig_10_03.gif" 2>/dev/null
mv "10_4_Does water go down a plughole in the opposite direction in Australia.png" "fig_10_04.png" 2>/dev/null
mv "10_5a_(a) Jean Bernard Léon Foucault's pendulum experiment in the Pantheon, Paris, in.jpg" "fig_10_05a.jpg" 2>/dev/null
mv "10_5a_(b) A pendulum swinging from a point, P, directly above the North pole will swing in a fixed plane while rotates below it. To an observer on the earth, the swing of the pendulum will appear to turn.svg" "fig_10_05b.svg" 2>/dev/null
mv "10_6a_Gyroscopic precession. (a) A spinning bicycle wheel supported on a string does not fall down, as expected intuitively, but precesses around a vertical axis.png" "fig_10_06a.png" 2>/dev/null
mv "10_6b_Gyroscopic precession. (b) a side view of the bicycle wheel and its axle. The string pushes up with a force mg exactly equal to the weight of the wheel. The resulting moment mgd is responsible for the gyroscopic effect.svg" "fig_10_06b.svg" 2>/dev/null
mv "10_7a_A disc spinning in a rotating frame. (a) A rigid frame rotating at angular velocity Ω contains a disc spinning with angular velocity ω. The spin axis of the disc is at right angles to the spin axis of the frame.png" "fig_10_07a.png" 2>/dev/null
mv "10_7b_A disc spinning in a rotating frame. (b) a point, P, on the perimeter of the disc has velocity ω × r.png" "fig_10_07b.png" 2>/dev/null
mv "10_8_The use of angular momentum to describe the gyroscopic effect.png" "fig_10_08.png" 2>/dev/null
mv "10_9a_A bicycle fitted with a reverse spinning wheel used to demonstrate that gyroscopic effects are not significant.png" "fig_10_09a.png" 2>/dev/null
mv "10_9b_A bicycle fitted with a reverse spinning wheel used to demonstrate that gyroscopic effects are not significant.png" "fig_10_09b.png" 2>/dev/null
mv "10_10a_A stone bouncing on water. The force f is off-centre and without the gyroscopic effect of the spinning stone, it would tip over.png" "fig_10_10a.png" 2>/dev/null
mv "10_10b_A stone bouncing on water. The force f is off-centre and without the gyroscopic effect of the spinning stone, it would tip over.png" "fig_10_10b.png" 2>/dev/null
mv "10_11_The Gyrocompass. A spinning disc will try to align itself to spin axis of the earth.png" "fig_10_11.png" 2>/dev/null
mv "10_12a_The earth is an oblate spheroid and it is shown here with an inscribed sphere.png" "fig_10_12a.png" 2>/dev/null
mv "10_12b_The earth is an oblate spheroid and it is shown here with an inscribed sphere.png" "fig_10_12b.png" 2>/dev/null
mv "10_13_The bulge on the earth is represented by discrete masses. Forces on these masses depend on their distance to the moon.png" "fig_10_13.png" 2>/dev/null
mv "10_14a_A gyroscope on a cone of height h and radius a.jpg" "fig_10_14a.jpg" 2>/dev/null
mv "10_14b_A gyroscope on a cone of height h and radius a.jpg" "fig_10_14b.jpg" 2>/dev/null
mv "10_14c_A gyroscope on a cone of height h and radius a.png" "fig_10_14c.png" 2>/dev/null
mv "10_15a_(a) A gyroscope overhanging a shelf.png" "fig_10_15a.png" 2>/dev/null
mv "10_15b_(b) a sideview showing a weight (in red) to stop the stand from tipping over when the gyroscope is vertical.png" "fig_10_15b.png" 2>/dev/null
mv "10_15c_(c) the same weight prevents tipping when the gyroscope is horizontal and precessing.png" "fig_10_15c.png" 2>/dev/null

# Chapter 11
mv "11_1_The moon came to be after a rogue Mars-sized planet (called Theia) collided with the Earth.jpg" "fig_11_01.jpg" 2>/dev/null
mv "11_2_A coupled pair of pendulums.png" "fig_11_02.png" 2>/dev/null
mv "11_3a_(a) mode 1, ω=√(ωo2–k).png" "fig_11_03a.png" 2>/dev/null
mv "11_3b_(b) mode 2, ω=√(ωo2+k).png" "fig_11_03b.png" 2>/dev/null
mv "11_3c_(c) The sum of modes 1 and 2.png" "fig_11_03c.png" 2>/dev/null
mv "11_4_A coupled pendulum experiment with string and coins.jpg" "fig_11_04.jpg" 2>/dev/null
mv "11_5_Tippe top.png" "fig_11_05.png" 2>/dev/null

# Chapter 12
mv "12_1_Stonehenge.jpg" "fig_12_01.jpg" 2>/dev/null
mv "12_2_The Earth at three points of its orbit A, B and C at time intervals.svg" "fig_12_02.svg" 2>/dev/null
mv "12_3_Sunrise, noon and sunset around the winter solstice.png" "fig_12_03.png" 2>/dev/null
mv "12_4_An illustration of the sun orbiting the earth (an earth-centred frame of reference is convenient for this analysis).svg" "fig_12_04.svg" 2>/dev/null
mv "12_5_The equation of time.svg" "fig_12_05.svg" 2>/dev/null
mv "12_6a_Determining the time of sunrise and sunset. (a) a view of the Earth at the winter solstice (northern hemisphere)" "fig_12_06a.png" 2>/dev/null
mv "12_6b_Determining the time of sunrise and sunset. (b) a view down from the North Pole showing the section at latitude L as a circle of radius r" "fig_12_06b.png" 2>/dev/null

# Chapter 13
mv "13_1a_Well-known engineering failures. (a) The Tacoma Narrows Bridge.jpg" "fig_13_01a.jpg" 2>/dev/null
mv "13_1b_Well-known engineering failures. (b) the De Havilland Comet aircraft.webp" "fig_13_01b.webp" 2>/dev/null
mv "13_2. A structure with Poisson's ratio.svg" "fig_13_02.svg" 2>/dev/null
mv "13_3_The variation of energy of an atom with distance from its neighbour.svg" "fig_13_03.svg" 2>/dev/null
mv "13_4a_(a) Stresses on a unit cube (z perpendicular to the page).svg" "fig_13_04a.svg" 2>/dev/null
mv "13_4b_(b) hydrostatic stress occurs when the stresses on all faces are equal.svg" "fig_13_04b.svg" 2>/dev/null
mv "13_4c_(c) and (d) pure shear with σz = 0.svg" "fig_13_04c.svg" 2>/dev/null
mv "13_4d_(d) pure shear with σz = 0.svg" "fig_13_04d.svg" 2>/dev/null
mv "13_5ab. A rod of length L subject to an axial force.svg" "fig_13_05.svg" 2>/dev/null
mv "13_6_A climber on a rope.png" "fig_13_06.png" 2>/dev/null
mv "13_7a_The Challenger disaster. (a) The aftermath of the explosion and (b) the join and 'O' ring seal.jpg" "fig_13_07a.jpg" 2>/dev/null
mv "13_7b_The Challenger disaster. (b) the join and 'O' ring seal.jpg" "fig_13_07b.jpg" 2>/dev/null
mv "13_8a_The O ring seal, (a) the gap widens to allow initial blow past the gap.png" "fig_13_08a.png" 2>/dev/null
mv "13_8b_The O ring seal (b) Higher pressure squashes the O ring.png" "fig_13_08b.png" 2>/dev/null
mv "13_9_Cupid stringing his bow  .jpg" "fig_13_09.jpg" 2>/dev/null
mv "13_10_An arrow when released is subject to a high axial force and it will bend. But if the natural frequency is just right then the vibrating arrow will clear the bow and will go straight.png" "fig_13_10.png" 2>/dev/null

echo "Rename complete!"
echo ""
echo "Files renamed. Checking results..."
ls -1 | head -30
echo "..."
echo "Total files: $(ls -1 | wc -l)"
