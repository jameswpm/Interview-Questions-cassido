""""
Given an array of logs and variable assignments, return a list of all unused variables.

Examples:

> findUnused(["a = 1", "b = a", "c = 2", "log(b)"]);
> ["c"]

> findUnused(["a = 1", "b = a", "c = 2", "log(c)"]);
> ["a", "b"]
"""

import re

def findLogPattern(variable):
    log = re.search(r"log\(([a-zA-Z])\)", variable)
    if log is not None:

        return log.group(1)
    return None

def findUnused(variables: list) -> list:
    # for each element of the array, it should check if it is logged and if so, check if it was assigned before and to which variable
    unused_vars = []
    logged_variables = map(findLogPattern, variables)
    for logged_var in list(logged_variables):
        if logged_var is None:
            continue
        for variable in variables:
            assign = re.search(r"([A-Za-z]{1}) = ([0-9a-zA-Z])", variable)
            if assign is not None:
                # variable name
                var_name = assign.group(1)
                var_value = assign.group(2)
                if var_name == logged_var:
                    if var_name in unused_vars: unused_vars.remove(var_name)
                    if var_value in unused_vars: unused_vars.remove(var_value)
                    continue                
                # if var_value == logged_var:
                #     if var_value in unused_vars: unused_vars.remove(var_value)
                #     continue
                unused_vars.append(var_name)

    print(unused_vars)
    return unused_vars



if __name__ == "__main__":
    assert findUnused(["a = 1", "b = a", "c = 2", "log(b)"]) == ['c']
    assert findUnused(["a = 1", "b = a", "c = 2", "log(c)"]) == ['a', 'b']
    assert findUnused(["m = 3", "n = m", "o = n", "log(m)"]) == ['n', 'o']
    assert findUnused(["x = 5", "y = x", "z = 10", "log(z)", "log(y)"]) == []
    assert findUnused(["a = 1", "b = 2", "c = 3", "d = c", "log(d)", "log(a)"]) == ['b']