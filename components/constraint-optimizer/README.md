# Constraint Optimizer

## Purpose
Provide a generic utility to formulate and solve linear programming problems using PuLP.

## Technologies
Python, PuLP

## Installation 
Create a virtual environment in the project folder

```bash
python -m venv .venv

# Activate the environment
# macOS / Linux
source .venv/bin/activate
# Windows (cmd)
.venv\Scripts\activate.bat
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```
Install required libraries
```bash
# (Optional) Upgrade pip inside the venv
python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Usage

The component can be used programmatically as shown below **or** through its command‑line helper `test.py`.

### Programmatic usage

```python
from constraint_optimizer import ConstraintOptimizer

# Example: maximize 3x + 5y subject to 2x + y <= 10, x + 2y <= 8, x, y >= 0
optimizer = ConstraintOptimizer()
optimizer.add_variable('x', lowbound=0)
optimizer.add_variable('y', lowbound=0)
optimizer.add_constraint('c1', 2 * optimizer.var('x') + optimizer.var('y') <= 10)
optimizer.add_constraint('c2', optimizer.var('x') + 2 * optimizer.var('y') <= 8)
optimizer.set_objective(3 * optimizer.var('x') + 5 * optimizer.var('y'))
solution = optimizer.solve()
print(solution)
```

### Command‑line usage

```bash
# After installing dependencies in a virtual environment
python test.py sample_data.json
```

The script reads the specified JSON file, builds the optimization model, solves it, and prints the solution as a dictionary.

