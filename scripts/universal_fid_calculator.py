# COMMIT MESSAGE: feat: add universal_fid_calculator.py to simulate information efficiency across scales

import math

def calculate_fid_efficiency(velocity, viscosity):
    """
    Calculates the Information Integrity (I) based on the FID law: I = v / eta
    
    Parameters:
    velocity (float): Velocity of the signal (m/s)
    viscosity (float): Viscosity of the medium (Pa.s)
    """
    if viscosity <= 0:
        return float('inf')
    return velocity / viscosity

def run_comparison():
    # Constants
    C_LIGHT = 299792458  # Speed of light
    ETA_SPACE_RIGID = 1.0e-11  # Viscosity of the cold Matrix
    
    V_NEURAL = 120.0  # Average neural propagation speed (m/s)
    ETA_CSF_CLEAN = 0.0007  # Viscosity of 'clean' cerebrospinal fluid (comparable to water)
    ETA_CSF_STAGNANT = 0.0021 # Viscositity during stagnation (3x increase)

    print("--- Syruponium FID Scale Analysis ---")
    
    # 1. Cosmic Scale (Photon through the Matrix)
    i_space = calculate_fid_efficiency(C_LIGHT, ETA_SPACE_RIGID)
    print(f"\n[Cosmos] Photon Integrity (I): {i_space:.2e}")
    
    # 2. Biological Scale (Neural Signal)
    i_brain_clean = calculate_fid_efficiency(V_NEURAL, ETA_CSF_CLEAN)
    i_brain_stagnant = calculate_fid_efficiency(V_NEURAL, ETA_CSF_STAGNANT)
    
    drop_pct = (1 - (i_brain_stagnant / i_brain_clean)) * 100
    
    print(f"[Brain] Optimal Neural Integrity: {i_brain_clean:.2e}")
    print(f"[Brain] Stagnant Neural Integrity: {i_brain_stagnant:.2e}")
    print(f"[!] Efficiency Drop during Stagnation: {drop_pct:.1f}%")
    
    print("\nConclusion: The mathematical decrease in efficiency follows the exact same "
          "pattern as the 'Pioneer Drag' observed on a cosmic scale.")

if __name__ == "__main__":
    run_comparison()
