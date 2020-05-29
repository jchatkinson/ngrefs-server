from sympy import symbols, Eq, evaluate, Equality

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
        steps = [u'{0} - {1}'.format(self.name, self.desc)]
        steps.append(self.latex_list(replacements))



# A group of 1 or more CalcEquations, which can be evaluated into a complete solution
class CalcSolution():
    def __init__(self, name, description, *args):
        self.name = name
        self.desc = description
        self.eqns = 

# Concrete Design Equations
# class Concrete():
#     def __init__(self, code):
#         self.code = code
#         self.ACI = 'aci'
#         self.NBCC = 'nbcc'
#         if code == self.ACI:
#             self.pshear = 0.6
#             self.pflexure = 0.9
#             self.pconcrete = 0.6
#             self.psteel = 0.85
#         else:
#             self.pshear = 0.65
#             self.pflexure = 0.85
#             self.pconcrete = 0.65
#             self.psteel = 0.85        

#     def beta1(self,fc):
#         if self.code == self.ACI:
#             return 0.003
#         else:
#             return 0.97 - 0.0025*fc
    
#     def alpha1(self,fc):
#         if self.code == self.ACI:
#             return 0.003
#         else:
#             return 0.85 - 0.0015*fc

#     def BeamFlexure():
#         Mr, bw, h, d, As, fc, fy = symbols('Mr bw h d As fc fy')
#         eq1 = Eq(Mr, )
#         eqn = CalcEquation('Mr','Moment Capacity of Rectangular Beam', )