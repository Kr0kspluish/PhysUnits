class InhomogenousError(Exception):
    
    '''An exception when trying forbidden operations between inhomogeneous
    PhysUnit expressions'''
    
    pass

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
                    try:
                        self.unit[s[0]] += 1
                    except KeyError:
                        self.unit[s[0]] = 1
                else: 
                    self.unit[s[0]] = int(s[1])
        
        else:
            raise TypeError("The unit should be a string or a dictionnary")

    def __str__(self, latex=False):
        
        l = []

        for k in self.unit.keys():
            s = k
            if self.unit[k] != 1:
                s += '^' + str(self.unit[k])
            l.append(s)

        return str(self.val) + '.'.join(l)


    def __repr__(self):
        
        l = []
        for k in self.unit.keys():
            s = k
            if self.unit[k] != 1:
                s += '^' + str(self.unit[k])
            l.append(s)

        return self.__class__.__name__ + '(' + self.val.__repr__() + ',\'' + '.'.join(l) + '\')'

### Operations on PhysUnit

# Binary operators 

    def __add__(self, other):
        
        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for + must have the same unit.")
                return -1
            else:
                return self.__class__(self.val+other.val, dict(self.unit))

        else:
            print("Erreur de type") #TODO vraie erreur

    def __radd__(self, other):
        
        return self + other

    def __sub__(self, other):
        
        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for - must have the same unit.")
            else:
                return self.__class__(self.val-other.val, dict(self.unit))
        else:
            print("Erreur de type") #TODO vraie erreur
            return -1

    def __rsub__(self, other):
        
        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for - must have the same unit.")
            else:
                return self.__class__(other.val-self.val, dict(self.unit))
        else:
            print("Erreur de type") #TODO vraie erreur
            return -1

    def __mul__(self, other):
        
        if isinstance(other, self.__class__):
            new_unit = dict(self.unit)
            for k in other.unit.keys():
                if k in new_unit.keys():
                    if new_unit[k] == -other.unit[k]:
                        del(new_unit[k])
                    else:
                        new_unit[k] += other.unit[k]
                else:
                    new_unit[k]=other.unit[k]
            return self.__class__(self.val*other.val, new_unit)

        else:
            return self.__class__(self.val*other, dict(self.unit))

    def __rmul__(self, other):
        
        return other*self

    def __truediv__(self, other):
        
        if isinstance(other, self.__class__):
            new_unit = dict(self.unit)
            for k in other.unit.keys():
                if k in new_unit.keys():
                    if new_unit[k] == other.unit[k]:
                        del(new_unit[k])
                    else:
                        new_unit[k] -= other.unit[k]
                else:
                    new_unit[k]=-other.unit[k]
            return self.__class__(self.val/other.val, new_unit)

        else:
            return self.__class__(self.val/other, dict(self.unit))

    def __rtruediv__(self, other):

        if isinstance(other, self.__class__):
            new_unit = dict(other.unit)
            for k in other.unit.keys():
                if k in new_unit.keys():
                    if new_unit[k] == self.unit[k]:
                        del(new_unit[k])
                    else:
                        new_unit[k] -= self.unit[k]
                else:
                    new_unit[k]=-self.unit[k]
            return self.__class__(other.val/self.val, new_unit)

        else:
            return self.__class__(other/self.val, dict([(k, -self.unit[k]) for k in self.unit.keys()]))

    def __pow__(self, other):
        
        return self.__class__(self.val**other, dict([(k,self.unit[k]*other) for k in self.unit.keys()]))

# Comparison operators
    
    def __lt__(self, other):

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val < other.val

    def __gt__(self, other):

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val > other.val

    def __le__(self, other):

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val <= other.val

    def __ge__(self, other):

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val >= other.val

    def __eq__(self, other):

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val == other.val

    def __ne__(self, other):

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val != other.val

# Assignment operators

    def __iadd__(self, other):
        print("Not implemented yet")
        pass #TODO

    def __isub__(self, other):
        print("Not implemented yet")
        pass #TODO

    def __imul__(self, other):
        print("Not implemented yet")
        pass #TODO

    def __idiv__(self, other):
        print("Not implemented yet")
        pass #TODO
    
    def __ipow__(self, other):
        print("Not implemented yet")
        pass #TODO
    
# Unary operators

    def __neg__(self):
        
        return self.__class__(-self.val, self.unit)

    def __pos__(self):

        return self.__class__(+self.val, self.unit)

    def __abs__(self):

        return self.__class__(abs(self.val), self.unit)


