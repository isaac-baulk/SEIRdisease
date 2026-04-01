# Assesment 2 - The SEIR model for disease transmission

This implements the SEIR disease transmission model using two mathematical approaches: a **Stochastic Agent-Based Model (monte carlo)** built in C++ and a **Deterministic Compartmental Model (ODE)** built in Python. 

The C++ backend is bound to Python using `pybind11`.

## Project Structure

```text
seir_project/                   
├── bindings/                # Pybind11 C++ bindings
│   └── bindings.cpp         
├── include/                 # C++ header files
│   ├── agent.h
│   ├── lattice.h
│   └── mcsim.h
├── scripts/                 # python scripts
│   ├── ODE_model.py 
│   ├── comparison.py    
│   └── follow_agents.py      
├── src/                     # C++ Source files
│   ├── agent.cpp
│   ├── lattice.cpp
│   ├── main.cpp
│   └── mcsim.cpp 
├── setup.py                 # Python build script for Pybind11
├── .gitignore               
└── README.md                
```

## Prerequisites

To compile and run this project, you will need:
* A C++17 compatible compiler
* Python 3.7+
* The following Python packages:
  ```bash
  pip install pybind11 numpy scipy matplotlib setuptools
  ```

## Compilation & Installation

This project uses `setup.py` to handle the compilation of the C++ program automatically.

1. Clone this repository and navigate to the root directory.
2. Install the bound C++ module using pip:
   ```bash
   pip install -e .
   ```

## Usage

Once installed, navigate to the `scripts/` directory to run the visualizations.

### 1. Compare Models
To run both the monte carlo and ODE simulations and compare their results:
```bash
cd scripts
python3 comparison.py
```

### 2. Track Agents on Lattice (using monte carlo model)
To render a a scatter plot animation of the agents moving across the lattice:
```bash
cd scripts
python3 follow_agents.py
```
### 3. Diamond Princess Test Case
To test the two models against a historical disease outbreak:

```bash
cd scripts
python3 diamondprincess.py
```
This script uses data from the COVID-19 outbreak on the Diamond Princess cruise ship in 2020 to compare the two SEIR models against real data for disease transmission.

### Optional: Use Monte Carlo Model in C++ 
`src/main.cpp` gives an example use of the monte carlo model in C++. To compile:

```bash
g++ -std=c++17 src/*.cpp -o main
```

