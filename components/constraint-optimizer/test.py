import json
import sys
from constraint_optimizer import ConstraintOptimizer


def load_problem(json_path: str) -> ConstraintOptimizer:
    """Load a JSON definition of a linear programming problem.

    The JSON format follows ``sample_data.json`` and includes:
    - ``coefficients``: mapping of variable name to objective coefficient
    - ``bounds``: mapping of variable name to ``[low, high]`` (``null`` means no bound)
    - ``constraints``: list of objects with ``name`` and ``expression`` strings
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    optimizer = ConstraintOptimizer()

    # Add variables with bounds
    bounds = data.get("bounds", {})
    for var_name, bound_pair in bounds.items():
        low, high = bound_pair
        # default lowbound to 0 if None, as typical LP non‑negativity
        low = low if low is not None else 0
        optimizer.add_variable(var_name, lowbound=low, upbound=high)

    # Define objective function
    coeffs = data.get("coefficients", {})
    objective_expr = sum(coeff * optimizer.variables[name] for name, coeff in coeffs.items())
    optimizer.set_objective(objective_expr)

    # Add constraints
    for constraint in data.get("constraints", []):
        name = constraint.get("name")
        expr_str = constraint.get("expression")
        # Evaluate the expression string in a namespace where variable names
        # resolve to PuLP variable objects.
        local_vars = optimizer.variables.copy()
        expr = eval(expr_str, {}, local_vars)
        optimizer.add_constraint(name, expr)

    return optimizer


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python test.py <path_to_problem_json>")
        sys.exit(1)

    problem_path = sys.argv[1]
    optimizer = load_problem(problem_path)
    solution = optimizer.solve()
    print(json.dumps(solution, indent=2))


if __name__ == "__main__":
    main()
