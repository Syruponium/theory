import numpy as np
import matplotlib.pyplot as plt

def simulate_nucleosynthesis(viscosity_factor):
    """
    Simulates elemental abundance based on the Syruponium viscosity.
    Standard Model assumes viscosity_factor = 0 (perfect fluid).
    V9.0 assumes a non-zero viscosity in the early 'stiff' phase.
    """
    # Baseline abundances (Simplified ratios)
    hydrogen = 0.75
    helium = 0.24
    
    # Standard prediction for Lithium-7 is usually ~3x higher than observed.
    # We model the 'Lithium Sink' as a function of Syruponic friction.
    standard_lithium = 1.5e-10 
    
    # In V9.0, Syruponic friction (viscosity) creates local 'vortices' 
    # that increase the probability of Lithium-7 destruction/conversion.
    # Efficiency of destruction is proportional to the fluid's 'grip'.
    destruction_efficiency = 1.0 + (viscosity_factor * 2.2) 
    
    observed_lithium = standard_lithium / destruction_efficiency
    
    return hydrogen, helium, observed_lithium

# Parameters for V9.0 (The 'Stiff' Syrup phase)
v9_viscosity = 0.9  # High viscosity in the early universe
h_v9, he_v9, li_v9 = simulate_nucleosynthesis(v9_viscosity)

# Parameters for Standard Model (The 'Empty' Vacuum)
std_viscosity = 0.0
h_std, he_std, li_std = simulate_nucleosynthesis(std_viscosity)

print(f"--- Syruponium V9.0 Results ---")
print(f"Hydrogen: {h_v9*100}%")
print(f"Helium:   {he_v9*100}%")
print(f"Lithium-7 Abundance Ratio: {li_v9:.2e}")
print(f"\nResult: V9.0 predicts a Lithium reduction of {((li_std-li_v9)/li_std)*100:.1f}%")
# Copyright (c) 2026 Syruponium. All rights reserved.
