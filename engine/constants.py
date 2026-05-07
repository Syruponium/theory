"""
SMP_CONSTANTS_V1.py
Master constant definitions for the Syruponium Matrix Protocol Engine.
Reference: /docs/theory/constants.md
"""

# Matrix Fundamentals
P_LIMIT = 1e34              # Pa
RHO_MATRIX = 1.32e17        # kg/m^3
S_M = 1.0                   # Normalized Surface Tension

# Phase & Thermal
T_SNAP = 13.84              # Kelvin
ETA_SUPERFLUID = 0.0        # Zero viscosity
ETA_RIGID = 2.91e-12        # Pa.s
ALPHA_RIGID = float('inf')  # Instant heat distribution

# Propagation & Resistance
C_EARLY = 275166362.9       # m/s
A_PIONEER = 8.74e-10        # m/s^2
K_COUPLING = 2.91e-14       # s^-1

# Expansion & Matter Creation
LAMBDA_SMP = 2.62e-39       # dV/dm
DM_DT = 2.62e-66            # kg/(m^3.s)

# Gravitational Coupling (Relative to standard G)
G_EFF_HIGH = 1.187          # Superfluid (+18.7%)
G_EFF_LOW = 0.813           # Rigid (-18.7%)

# Quantum & Density
ALPHA_DEVIATION = 8.95e-2
F_PBH = 3e-6
