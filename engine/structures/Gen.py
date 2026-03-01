#Dmytry-dev
#27.02.2026

class Morphogenes:
    def __init__(self, Name, Distribution, Condition, Timer, Action_name):
        self.M_name = Name
        self.D = Distribution
        self.C = Condition
        self.T = Timer

        self.A_name = Action_name
        self.A_obj = None

        self.Morphogen_structure = {"Morphogen": self.M_name, "Distribution": self.D, "Timer": self.T,"Condition": self.C, "Action name": self.A_name, "Action object": self.A_obj}

class Actions:
    def __init__(self, Name, Action):
        self.A_name = Name
        self.A = Action


class Information:
    def __init__(self, Name):
        self.N = Name

class Genes:
    def __init__(self, Morphogens, Actions, Timers, Information):
        self.Mg = Morphogens
        self.Ac = Actions
        self.Tm = Timers
        self.Inf = Information

        self.DNA = [self.Mg, self.Ac, self.Tm, self.Inf]

        self.DNA_linker()

    def DNA_linker(self):
        for i in range(len(self.Mg)):
            Morphogen = self.Mg[i]
            for t in range(len(self.Ac)):
                Action = self.Ac[t]
                if Morphogen.A_name == Action.A_name:
                    Morphogen.A_obj = Action
                    break