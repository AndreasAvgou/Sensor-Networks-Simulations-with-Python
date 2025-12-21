# main.py
import matplotlib.pyplot as plt
import numpy as np
from network_rgg import network_rgg

def run_simulation_batch(radius_list, population=1000, runs_per_radius=50):
    """
    Runs the simulation for a list of radii.
    Returns lists of connected and not_connected counts.
    """
    connected_counts = []
    not_connected_counts = []
    
    print(f"Starting simulation for population: {population}")
    
    for r in radius_list:
        connected = 0
        not_connected = 0
        
        print(f"  Testing radius r = {r:.3f} ... ", end="", flush=True)
        
        for i in range(runs_per_radius):
            # Create the network
            net = network_rgg(population, r)
            
            # Check connectivity
            if net.is_connected():
                connected += 1
            else:
                not_connected += 1
        
        connected_counts.append(connected)
        not_connected_counts.append(not_connected)
        print(f"Conn: {connected}, Not Conn: {not_connected}")
        
    return connected_counts, not_connected_counts

def plot_results(radii, connected, not_connected, title):
    """
    Plots the results similar to the PDF example.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(radii, connected, label='Connected', color='blue', marker='o')
    plt.plot(radii, not_connected, label='Not Connected', color='red', marker='x')
    
    plt.xlabel('Radius (r)')
    plt.ylabel('Number of Simulations')
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    # --- STEP 1: Coarse Simulation (0.01 to 0.10) ---
    # According to the assignment [cite: 10]
    
    # Generate radii: 0.01, 0.02, ... 0.10
    coarse_radii = [round(x * 0.01, 2) for x in range(1, 11)]
    
    c_counts, nc_counts = run_simulation_batch(coarse_radii)
    
    # Plot Step 1
    plot_results(coarse_radii, c_counts, nc_counts, 
                 "Connectivity vs Radius (Coarse Search)")

    # --- STEP 2: Refined Simulation (3 decimal places) ---
    # The assignment asks to study the behavior where the change happens 
    
    # Find the interval where the graph switches from mostly unconnected to connected
    start_r = 0.0
    end_r = 0.1
    
    # Heuristic: Find first r where connected > 0 and last r where not_connected > 0
    for i, r in enumerate(coarse_radii):
        if c_counts[i] > 0 and start_r == 0.0:
            start_r = coarse_radii[max(0, i-1)] # Start one step before
        if nc_counts[i] == 0 and end_r == 0.1:
            end_r = r
            break
            
    print(f"\nPhase transition detected between {start_r} and {end_r}.")
    print("Running refined simulation with 3 decimal places...")
    
    # Create finer steps (e.g., 0.002 increments) within the transition zone
    # np.linspace or arange can be used. Let's use 0.002 steps.
    refined_radii = np.arange(start_r, end_r + 0.002, 0.002)
    
    c_counts_fine, nc_counts_fine = run_simulation_batch(refined_radii)
    
    # Plot Step 2
    plot_results(refined_radii, c_counts_fine, nc_counts_fine, 
                 "Connectivity vs Radius (Refined Search)")