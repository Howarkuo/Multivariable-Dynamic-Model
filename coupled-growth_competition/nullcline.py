import numpy as np
import matplotlib.pyplot as plt

# Carrying capacities
Ka = 1000
Kb = 500

# Create an array of 'a' values to define the shading boundaries
a_vals = np.linspace(0, 1200, 400)

# Calculate the lines b = 1000 - a and b = 500 - a
# np.maximum(0, ...) ensures the shading doesn't drop below the x-axis
b_vals_Ka = np.maximum(0, Ka - a_vals)
b_vals_Kb = np.maximum(0, Kb - a_vals)

plt.figure(figsize=(8, 8))

# --- Shade the 3 Regions ---
# Region I: area above the a-nullcline (a + b > 1000)
plt.fill_between(a_vals, b_vals_Ka, 1200, color='#e0e0e0', alpha=0.6, label='Region I (Both decrease)')

# Region II: area between the nullclines (500 < a + b < 1000)
plt.fill_between(a_vals, b_vals_Kb, b_vals_Ka, color='#cce5ff', alpha=0.6, label='Region II (a increases, b decreases)')

# Region III: area below the b-nullcline (a + b < 500)
plt.fill_between(a_vals, 0, b_vals_Kb, color='#ffe6cc', alpha=0.6, label='Region III (Both increase)')


# --- Plot the Nullclines ---
a_line_Ka = np.linspace(0, Ka, 100)
a_line_Kb = np.linspace(0, Kb, 100)

# a-nullclines (Green)
plt.plot(a_line_Ka, Ka - a_line_Ka, color='green', linewidth=2.5, label='a-nullcline (a + b = 1000)')
plt.axvline(x=0, ymin=0, ymax=Ka/1200, color='green', linewidth=2.5) # Vertical axis portion

# b-nullclines (Purple)
plt.plot(a_line_Kb, Kb - a_line_Kb, color='purple', linewidth=2.5, label='b-nullcline (a + b = 500)')
plt.axhline(y=0, xmin=0, xmax=Ka/1200, color='purple', linewidth=2.5) # Horizontal axis portion


# --- Add Labels and Points ---
# Roman numerals marking the regions near the y-axis (matching the slides)
plt.text(40, 1050, 'I', fontsize=24, fontweight='bold', color='#333333')
plt.text(40, 600, 'II', fontsize=24, fontweight='bold', color='#333333')
plt.text(40, 150, 'III', fontsize=24, fontweight='bold', color='#333333')

# Equilibria points (Red dots)
equilibria = [(0, 0), (0, 500), (1000, 0)]
for pt in equilibria:
    plt.plot(pt[0], pt[1], 'ro', markersize=8)

# Format the graph
plt.xlim(-20, 1200)
plt.ylim(-20, 1200)
plt.xlabel('a', fontsize=14, loc='right')
plt.ylabel('b', fontsize=14, rotation=0, loc='top', labelpad=-20)
plt.title('Phase Plane Regions and Nullclines', fontsize=16)
plt.legend(loc='upper right', fontsize=9)

plt.show()