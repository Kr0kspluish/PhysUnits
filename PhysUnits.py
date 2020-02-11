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

        return str(self.val) + ' ' + '.'.join(l)


    def __repr__(self):
        
        l = []
        for k in self.unit.keys():
            s = k
            if self.unit[k] != 1:
                s += '^' + str(self.unit[k])
            l.append(s)

        return self.__class__.__name__ + '(' + self.val.__repr__() + ',\'' + '.'.join(l) + '\')'

    def print_Latex(self):
        '''Prints a string that can directly be copy-pasted within LaTeX code'''

        l = []
        for k in self.unit.keys():
            s = k
            if self.unit[k] != 1:
                s_count = str(self.unit[k])
                s += ('^' if len(s_count) == 1 else '^{') + s_count + ('}' if len(s_count) != 1 else '')
            l.append(s)

        print(self.val.__repr__() + '\\cdot '.join(l))


### Operations on PhysUnit

# Binary operators 

    def __add__(self, other):
        '''Returns self + other. 
        Only supported between instances of PhysUnit.'''
        
        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for + must have the same unit.")
            else:
                return self.__class__(self.val+other.val, dict(self.unit))

        else:
            raise TypeError("Operation + forbidden between {} and {}.".format(self.__class__.__name__, other.__class__.__name__))

    def __radd__(self, other):
        '''Returns other + self.
        See __add__ for compatibility with other classes.'''

        return self + other

    def __sub__(self, other):
        '''Returns self - other. 
        Only supported between instances of PhysUnit.''' 

        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for - must have the same unit.")
            else:
                return self.__class__(self.val-other.val, dict(self.unit))
        else:
            raise TypeError("Operation - forbidden between {} and {}.".format(self.__class__.__name__, other.__class__.__name__))

    def __rsub__(self, other):
        '''Returns other - self.
        See __sub__ for compatibility with other classes.'''
        
        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for - must have the same unit.")
            else:
                return self.__class__(other.val-self.val, dict(self.unit))
        else:
            raise TypeError("Operation - forbidden between {} and {}.".format(other.__class__.__name__, self.__class__.__name__))

    def __mul__(self, other):
        '''Returns self * other.
        other can be another PhysUnit or any numerical constant.'''
        
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
        '''Returns other * self.
        See __mul__ for compatibility with other classes.'''
        
        return other*self

    def __truediv__(self, other):
        '''Returns self / other.
        other can be another PhysUnit or any numerical constant.'''
        
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
        '''Returns other / self.
        See __truediv__ for compatibility with other classes.'''

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
        '''Returns self**other.
        other should be a numerical constant.'''
        
        return self.__class__(self.val**other, dict([(k,self.unit[k]*other) for k in self.unit.keys()]))

# Comparison operators
    
    def __lt__(self, other):
        '''Returns self < other'''

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val < other.val

    def __gt__(self, other):
        '''Returns self > other'''

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val > other.val

    def __le__(self, other):
        '''Returns self <= other'''

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val <= other.val

    def __ge__(self, other):
        '''Returns self >= other'''

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val >= other.val

    def __eq__(self, other):
        '''Returns self == other'''

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val == other.val

    def __ne__(self, other):
        '''Returns self != other'''

        if self.unit != other.unit:
            raise InhomogenousError("Operands must have the same unit for comparison.")
        else:
            return self.val != other.val

# Assignment operators

    def __iadd__(self, other):
        '''Implements self += other'''

        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for + must have the same unit.")
            else:
                self.val += other.val

        else:
            raise TypeError("Operation + forbidden between {} and {}.".format(self.__class__.__name__, other.__class__.__name__))

        return self

    def __isub__(self, other):
        '''Implements self -= other'''

        if isinstance(other, self.__class__):

            if self.unit != other.unit:
                raise InhomogenousError("Operands for - must have the same unit.")
            else:
                self.val-=other.val
        else:
            raise TypeError("Operation - forbidden between {} and {}.".format(self.__class__.__name__, other.__class__.__name__))

        return self

    def __imul__(self, other):
        '''Implements self *= other'''

        if isinstance(other, self.__class__):
            
            for k in other.unit.keys():
                if k in self.unit.keys():
                    if self.unit[k] == -other.unit[k]:
                        del(self.unit[k])
                    else:
                        self.unit[k] += other.unit[k]
                else:
                    self.unit[k]=other.unit[k]
            
            self.val*=other.val

        else:
            self.val*=other

        return self
    
    def __idiv__(self, other):
        '''Implements self /= other'''
        
        if isinstance(other, self.__class__):
            for k in other.unit.keys():
                if k in self.unit.keys():
                    if self.unit[k] == other.unit[k]:
                        del(self.unit[k])
                    else:
                        self.unit[k] -= other.unit[k]
                else:
                    self.unit[k]=-other.unit[k]
            self.val/=other.val

        else:
            self.val/=other

        return self
    
    def __ipow__(self, other):
        '''Implements self **= other'''
        
        self.val**=other
        if other == 0:
            self.unit = dict()
        else:
            for k in self.unit.keys():
                self.unit[k] *= other
        
        return self


# Unary operators

    def __neg__(self):
        '''Returns -self'''

        return self.__class__(-self.val, self.unit)

    def __pos__(self):
        '''Returns +self'''

        return self.__class__(+self.val, self.unit)

    def __abs__(self):
        '''Returns abs(self)'''

        return self.__class__(abs(self.val), self.unit)
