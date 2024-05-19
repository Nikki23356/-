from sympy import symbols, Eq, nsolve

n = symbols('x1')
equation = [Eq(5+n, 2)]
firstAns = [0]
decision = nsolve(equation, (n, ), firstAns)
print(f"n = {decision[0]}")