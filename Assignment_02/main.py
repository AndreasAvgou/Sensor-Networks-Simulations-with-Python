# main.py
import matplotlib.pyplot as plt
import numpy as np
from network_rgg import network_rgg
from random_walker import random_walker
import random

def run_simulation():
    # Configuration per assignment
    POPULATION = 1000
    RC = 0.08
    NUM_SIMULATIONS = 50
    MAX_STEPS = 4500  # Sufficient steps to reach >90% coverage
    STEP_INTERVAL = 50 # Record data every 50 steps
    
    # Store results: coverage_data[step_index] = list of coverages for that step across sims
    # Steps to record: 0, 50, 100, 150 ... MAX_STEPS
    steps_x = list(range(0, MAX_STEPS + 1, STEP_INTERVAL))
    coverage_results = {step: [] for step in steps_x}
    
    print(f"Starting {NUM_SIMULATIONS} simulations...")
    
    for sim in range(NUM_SIMULATIONS):
        # 1. Create Network
        net = network_rgg(POPULATION, RC)
        
        # Ensure network is connected (or valid enough for walk)
        # With r=0.08 and N=1000, it is extremely likely to be connected.
        # If not connected, the walker might get stuck in a small component.
        # We perform the walk regardless to match standard experimental conditions.
        
        # 2. Initialize Walker at random node
        start_node = random.choice(net.nodes)
        rw = random_walker(net, start_node)
        
        # 3. Walk
        # Record coverage at step 0
        coverage_results[0].append(rw.get_coverage())
        
        for s in range(1, MAX_STEPS + 1):
            rw.next_step()
            
            if s % STEP_INTERVAL == 0:
                coverage_results[s].append(rw.get_coverage())
        
        if (sim + 1) % 10 == 0:
            print(f"Simulation {sim + 1}/{NUM_SIMULATIONS} completed.")

    # 4. Process Data (Calculate Mean)
    mean_coverage = []
    for step in steps_x:
        avg = np.mean(coverage_results[step])
        mean_coverage.append(avg)
        
    # Find step where coverage crosses 0.9 (90%)
    target_step = None
    for i, cov in enumerate(mean_coverage):
        if cov >= 0.9:
            target_step = steps_x[i]
            break
            
    print(f"\nApproximate steps to reach 90% coverage: {target_step}")

    # 5. Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(steps_x, mean_coverage, label='Average Coverage', color='gray', linewidth=2)
    
    # Add horizontal line for 90%
    plt.axhline(y=0.9, color='r', linestyle='--', label='90% Target')
    
    plt.title(f'Random Walker Coverage on RGG (N={POPULATION}, r={RC})\nAverage of {NUM_SIMULATIONS} Simulations')
    plt.xlabel('Number of Steps')
    plt.ylabel('Fraction of Network Covered')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.ylim(0, 1.05)
    
    plt.savefig("rw_coverage_plot.png")
    plt.show()

if __name__ == "__main__":
    run_simulation()