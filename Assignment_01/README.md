# Assignment 1: RGG Connectivity Threshold

This project investigates the critical radius ($r_c$) required for a Random Geometric Graph (RGG) of 1000 nodes to become fully connected.

## 🎯 Objective
To find the radius $r_c$ where the probability of the graph being connected transitions from 0 to 1 (Phase Transition).

## 📂 Files
* `network_rgg.py`: Graph generation and BFS connectivity check.
* `main.py`: Runs a coarse search ($0.01-0.10$) followed by a refined search (3 decimal precision).
* `node.py`, `distribution.py`: Helper classes.

## 📊 Output
* **Coarse Plot**: Connectivity counts for steps of 0.01.
* **Refined Plot**: Detailed view of the transition zone (e.g., $0.040 - 0.060$).
