import pulp

class ConstraintOptimizer:
    def __init__(self):
        self.prob = pulp.LpProblem('GenericLP', pulp.LpMaximize)
        self.variables = {}

    def add_variable(self, name, lowbound=0, upbound=None, cat='Continuous'):
        """Add a variable to the LP model.

        Args:
            name: Variable name as a string.
            lowbound: Lower bound (default 0). Use ``None`` for no bound.
            upbound: Upper bound (default ``None`` for no bound).
            cat: Variable category – ``'Continuous'``, ``'Integer'`` or ``'Binary'``.
        Returns:
            The created :class:`pulp.LpVariable` instance.
        """
        var = pulp.LpVariable(name, lowBound=lowbound, upBound=upbound, cat=cat)
        self.variables[name] = var
        return var

    def var(self, name):
        """Convenient accessor for a previously added variable.

        This mirrors the API shown in the README examples, allowing
        ``optimizer.var('x')`` instead of ``optimizer.variables['x']``.
        """
        try:
            return self.variables[name]
        except KeyError as e:
            raise KeyError(f"Variable '{name}' not defined. Did you forget to call add_variable?") from e

    def add_constraint(self, constraint_name, expression):
        """Add a constraint expression to the model.

        The ``expression`` should be a valid PuLP inequality (e.g.
        ``x + y <= 10``).
        """
        self.prob += expression, constraint_name

    def set_objective(self, objective_expr):
        """Set the objective function for the LP.

        ``objective_expr`` is a PuLP linear expression.
        """
        self.prob += objective_expr, "Objective"

    def solve(self):
        """Solve the LP and return a mapping of variable names to values.

        Returns:
            dict: ``{variable_name: value, ...}``
        """
        self.prob.solve()
        return {name: var.varValue for name, var in self.variables.items()}
