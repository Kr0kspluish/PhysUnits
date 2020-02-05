class PhysUnit:
    
    def __init__(self, val, unit):

        self.val = val
        if isinstance(unit, dict):
            self.unit = dict(unit)

        elif isinstance(unit, str):
            self.unit = dict()
            for u in unit.split('.'):
                s = u.split('^')
                if len(s) == 1:
                    self.unit[s[0]] = 1 #TODO gérer les 'km.km' par ex
                else: 
                    self.unit[s[0]] = int(s[1])

        #TODO erreur si ce n'est aucun des deux

    def __str__(self):
        pass #TODO

    def __repr__(self):
        pass #TODO

### Operations on PhysUnit

# Binary operators 

    def __add__(self, other):
        pass #TODO (on ne peut ajouter que des PhysUnits entre eux, et s'ils ont la même unité)

    def __radd__(self, other):
        pass #TODO

    def __sub__(self, other):
        pass #TODO

    def __rsub__(self, other):
        pass #TODO

    def __mul__(self, other):
        pass #TODO (on peut multiplier par un autre PhysUnit ou une constante)

    def __rmul__(self, other):
        pass #TODO

    def __truediv__(self, other):
        pass #TODO

    def __rtruediv__(self, other):#TODO check que ça existe
        pass #TODO

    def __pow__(self, other):
        pass #TODO (l'exposant doit être une constante)

#TODO opérations arithmétiques (floordiv, mod) ?

# Comparison operators
    
    def __lt__(self, other):
        pass #TODO

    def __gt__(self, other):
        pass #TODO

    def __le__(self, other):
        pass #TODO

    def __ge__(self, other):
        pass #TODO

    def __eq__(self, other):
        pass #TODO

    def __ne__(self, other):
        pass #TODO

# Assignment operators

    def __iadd__(self, other):
        pass #TODO

    def __isub__(self, other):
        pass #TODO

    def __imul__(self, other):
        pass #TODO

    def __idiv__(self, other):
        pass #TODO
    
    def __ipow__(self, other):
        pass #TODO
    
# Unary Operators

    def __neg__(self, other):
        pass #TODO

    def __pos__(self, other):
        pass #TODO

    def __invert__(self, other):
        pass #TODO
