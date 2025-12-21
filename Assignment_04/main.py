# main.py
import matplotlib.pyplot as plt
import numpy as np
import random
from network_rgg import network_rgg
from random_walker import random_walker

def run_comparison():
    # Parameters from assignment
    POPULATION = 1000  # [cite: 10]
    RADII = [0.07, 0.08, 0.09, 0.10] # [cite: 11]
    NUM_SIMULATIONS = 20 # Averaging to get smooth curves
    MAX_STEPS = 6000 # Enough to reach ~95%
    STEP_INTERVAL = 50 # [cite: 12]
    
    # Dictionary to store results: radius -> list of coverage % per interval
    # Initialize with zeros
    steps_x = list(range(0, MAX_STEPS + 1, STEP_INTERVAL))
    final_results = {r: np.zeros(len(steps_x)) for r in RADII}

    print(f"Comparing RGG Random Walks for radii: {RADII}")
    print(f"Nodes: {POPULATION}, Simulations per radius: {NUM_SIMULATIONS}")

    for r in RADII:
        print(f"Processing r = {r}...")
        valid_sims_count = 0
        
        while valid_sims_count < NUM_SIMULATIONS:
            # 1. Construct Network
            net = network_rgg(POPULATION, r)
            
            # We strictly need a connected graph (or giant component) 
            # so the walker isn't trapped in a small island.
            if not net.is_connected():
                continue # Retry generation if not connected

            # 2. Random Walk
            start_node = random.choice(net.nodes)
            rw = random_walker(net, start_node)
            
            # Record t=0
            current_sim_data = [rw.get_coverage()]
            
            # Walk
            for s in range(1, MAX_STEPS + 1):
                rw.next_step()
                if s % STEP_INTERVAL == 0:
                    current_sim_data.append(rw.get_coverage())
            
            # Add to accumulator
            final_results[r] += np.array(current_sim_data)
            valid_sims_count += 1
            
        # Calculate Average
        final_results[r] /= NUM_SIMULATIONS

    # Plotting [cite: 12]
    plt.figure(figsize=(12, 7))
    
    colors = ['red', 'orange', 'green', 'blue']
    
    for i, r in enumerate(RADII):
        plt.plot(steps_x, final_results[r], label=f'r_c = {r}', color=colors[i], linewidth=2)

    # 95% Target Line 
    plt.axhline(y=0.95, color='black', linestyle='--', alpha=0.5, label='95% Target')

    plt.title(f'Random Walker Coverage vs Network Density (N={POPULATION})')
    plt.xlabel('Number of Steps')
    plt.ylabel('Network Coverage (%)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plt.savefig("rgg_coverage_comparison.png")
    plt.show()
    print("Comparison complete. Plot saved.")

if __name__ == "__main__":
    run_comparison()