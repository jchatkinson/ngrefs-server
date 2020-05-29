from sympy import *
import json

Tr, As, fy, pS = symbols('T_r A_s f_y phi_s')
expr1 = pS * As * fy
eq1 = Eq(Tr, expr1)
expr2 = expr1.subs(pS, 0.85).subs(As, 1.00).subs(fy, 58)
expr3 = expr2.evalf()

# A custom equation class 
class CalcEquation():
    def __init__(self, name, description, equality):
        self.name = name
        self.desc = description
        self.expr = equality

    def __repr__(self):
        return "<CalcEquation {0} - {1}: {2}>".format(self.name, self.desc, self.expr)

    def define_steps(self, replacements): 
        # print the base equation, then
        # print the base equation with variable substitution, then
        # print the solution
        expr2 = self.expr
        for _from, _to in replacements:
            with evaluate(False):
                expr2 = expr2.replace(_from,_to)
        
        expr3 = self.expr   
        for _from, _to in replacements:
            expr3 = expr3.subs(_from,_to)

        return self.expr, expr2, expr3

    def print_steps(self, replacements):
        e1, e2, e3 = self.define_steps(replacements)
        pprint(e1)
        pprint(e2)
        pprint(e3)

    def latex_list(self, replacements):
        e1, e2, e3 = self.define_steps(replacements)
        return [latex(e1), latex(e2), latex(e3)]
    
    def full_list(self, replacements):
        steps = ["{0} - {1}".format(self.name, self.desc)]
        steps.extend(self.latex_list(replacements))
        return steps


e = CalcEquation('Tensile Strength','Calculate the tensile strength of the rebar', eq1)
print(e)
replacements = [(pS,0.85),(fy,58),(As,3.14)]
e.print_steps(replacements)

mystr = e.full_list(replacements)
print(json.dumps(mystr))
