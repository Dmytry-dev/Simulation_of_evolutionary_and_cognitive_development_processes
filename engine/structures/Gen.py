#Dmytry-dev
#08.03.2026

class Morphogenes:
    def __init__(self, Name, Distribution, Condition, Action):
        self.M_name = Name
        self.D = Distribution
        self.C = Condition

        self.A = Action
        
class Actions:
    def __init__(self, Name, Action, Timer):
        self.A_name = Name
        self.A = Action
        self.T = Timer



class Informations:
    def __init__(self, Name):
        self.N = Name

class DNA:
    def __init__(self, Morphogens, Actions, Information):
        self.Mg = Morphogens
        self.Ac = Actions
        self.Inf = Information

        self.DNA_linker()

    def DNA_linker(self):
        for i in range(len(self.Mg)):
            Morphogen = self.Mg[i]
            for t in range(len(self.Ac)):
                Action = self.Ac[t]
                if Morphogen.A == Action.A_name:
                    Morphogen.A = Action
                    break