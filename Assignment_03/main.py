# main.py
import matplotlib.pyplot as plt
import numpy as np
from network_rgg import network_rgg

def run_simulation():
    # Configuration
    POPULATION = 1000
    # Radius range: 0.01, 0.02, ... 0.10 [cite: 32]
    RADIU_LIST = [round(x * 0.01, 2) for x in range(1, 11)] 
    SIMULATIONS_PER_RADIUS = 50 [cite: 33]
    
    # Data storage
    # We will store the mean of the 50 simulations for each radius
    results_avg = []
    results_max = []
    results_min = []
    
    print(f"Starting simulations for N={POPULATION}...")

    for r in RADIU_LIST:
        print(f"Simulating Radius r = {r} ... ", end="")
        
        sum_avg_deg = 0
        sum_max_deg = 0
        sum_min_deg = 0
        
        for sim in range(SIMULATIONS_PER_RADIUS):
            net = network_rgg(POPULATION, r)
            avg_d, max_d, min_d = net.get_degree_stats()
            
            sum_avg_deg += avg_d
            sum_max_deg += max_d
            sum_min_deg += min_d
        
        # Calculate the average over the 50 simulations
        final_avg = sum_avg_deg / SIMULATIONS_PER_RADIUS
        final_max = sum_max_deg / SIMULATIONS_PER_RADIUS
        final_min = sum_min_deg / SIMULATIONS_PER_RADIUS
        
        results_avg.append(final_avg)
        results_max.append(final_max)
        results_min.append(final_min)
        
        print(f"Done. Avg Neigh: {final_avg:.2f}")

    # Plotting [cite: 30]
    
    # Plot 1: Average Neighbors vs Radius
    plt.figure(figsize=(10, 6))
    plt.plot(RADIU_LIST, results_avg, marker='o', color='blue', label='Average Degree')
    plt.title(f'RGG Analysis (N={POPULATION}): Average Neighbors vs Radius')
    plt.xlabel('Radius ($r_c$)')
    plt.ylabel('Average Number of Neighbors')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(RADIU_LIST)
    plt.legend()
    plt.savefig("rgg_average_degree.png")
    plt.show()

    # Plot 2: Min/Max Neighbors vs Radius
    plt.figure(figsize=(10, 6))
    plt.plot(RADIU_LIST, results_max, marker='^', color='red', label='Max Neighbors')
    plt.plot(RADIU_LIST, results_min, marker='v', color='green', label='Min Neighbors')
    plt.title(f'RGG Analysis (N={POPULATION}): Min/Max Neighbors vs Radius')
    plt.xlabel('Radius ($r_c$)')
    plt.ylabel('Number of Neighbors')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(RADIU_LIST)
    plt.legend()
    plt.savefig("rgg_min_max_degree.png")
    plt.show()
    
    print("\nSimulations complete. Plots saved.")

if __name__ == "__main__":
    run_simulation()