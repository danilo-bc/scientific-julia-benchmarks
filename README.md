# Scientific Julia Benchmarks
A few scenarios focused on comparing Julia with Python and similar languages for modeling workloads, specially discrete systems.

# Quick start
- Open a terminal in a benchmark scenario, run "make" or any scenario individually
    - i.e., `python <script_name.py>` for Python, `julia <script_name.jl>` for Julia, etc.

# Requirements
## Python

Python requirements are in file "requirements.txt"

## Julia

Uses `BenchmarkTools` present by default.

# Scenarios
- pi_calculation_monte_carlo
    - Calculate "pi" using 10^7 Monte Carlo iterations
