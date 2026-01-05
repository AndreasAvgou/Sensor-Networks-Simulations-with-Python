# Sensor Networks Simulations with Python

This repository contains a collection of Python simulations The projects focus on **Random Geometric Graphs (RGG)**, analyzing their connectivity, node degree properties, and the behavior of Random Walkers within them.

## Project Structure

The repository is organized into four main assignments/exercises:

1.  **Connectivity Analysis (`Assignment_01`)**:
    * Determines the critical radius ($r_c$) for network connectivity.
    * Performs coarse and refined simulations around the phase transition.

2.  **Degree Metrics Analysis (`Assignment_02a`)**:
    * Analyzes Average, Minimum, and Maximum node degrees.
    * Studies the relationship between radius ($r$) and network density.

3.  **Random Walker - Single Run (`Assignment_02_Ex1`)**:
    * Simulates a single Random Walker on a graph.
    * Calculates steps required to achieve 90% network coverage.

4.  **Random Walker - Comparison (`Assignment_02_Ex3`)**:
    * Compares walker efficiency across different network densities ($r=0.07$ to $0.10$).
    * Visualizes how higher density leads to faster coverage.

## Prerequisites

All projects require **Python 3.x** and the following libraries for data processing and plotting:

```bash
pip install matplotlib numpy
```

## How to Run

Navigate to the specific assignment folder and run the main.py script:


```bash
cd Assignment_01
python main.py
```
