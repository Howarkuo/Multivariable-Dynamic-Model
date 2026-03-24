import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the competition model based on the coupled differential equations
def competition_model(populations, t, mu, lambda_, Ka, Kb):
    a, b = populations
    # Equations from page 5 & 7
    dadt = mu * a * (1 - (a + b) / Ka)
    dbdt = lambda_ * b * (1 - (a + b) / Kb)
    return [dadt, dbdt]

# Set the parameters from the slides (page 6 & 7)
mu = 0.2          # Growth rate of species a
lambda_ = 0.5     # Growth rate of species b
Ka = 1000         # Carrying capacity of species a
Kb = 500          # Carrying capacity of species b

# Initial populations (page 7)
initial_populations = [50, 50] # a(0)=50, b(0)=50

# Time points to simulate (from t=0 to t=100)
t = np.linspace(0, 100, 1000)

# Solve the differential equations
solution = odeint(competition_model, initial_populations, t, args=(mu, lambda_, Ka, Kb))

# Extract the results for a and b
a_pop = solution[:, 0]
b_pop = solution[:, 1]

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(t, a_pop, label='a', color='#1f77b4', linewidth=2.5) # Blue line for a
plt.plot(t, b_pop, label='b', color='#ff7f0e', linewidth=2.5) # Orange line for b

# Formatting the graph to match the slide
plt.xlabel('Time', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.title('The dynamics of competition between two species', fontsize=14)
plt.xlim(0, 100)
plt.ylim(0, 1200)
plt.legend(loc='upper right')
plt.grid(False) # The slide graph doesn't have an inner grid

# Show the plot
plt.show()