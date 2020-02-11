# PhysUnits

This is a Python module aiming at easily representing and manipulating
numerical values that have an associated physical unit.  

### How to use

All you have to do is declare your variable by calling the constructor:

    x = PhysUnit(3.25, 'm')

Then `x` represents 3.25m, and you can do all traditional operations
on `x` as if it was an `int` or `float`.  
Notice that the unit is a string and then requires to be inside quotes.  
To have a list of available methods, try `help(PhysUnit)`

### Examples

You can start from the following minimal examples to understand the module.

    x = PhysUnit(3.5, 'm')
    y = PhysUnit(0.5, 's')
    print(x/y)

The above should print `7m.s^-1`.
