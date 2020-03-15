# PhysUnits  

This is a Python module aiming at easily representing and manipulating
numerical values that have an associated physical unit.  


### How to use  

All you have to do is declare your variable by calling the constructor:

    x = PhysUnit(3.25, 'm')

Then `x` represents 3.25m, and you can do all traditional operations
on `x` as if it was an `int` or `float`.  
Note that the unit is a string and then requires to be inside quotes.  
To have a list of available methods, try `help(PhysUnit)`.


### Examples  

You can start from the following minimal examples to understand the module.
    
    from PhysUnits import PhysUnit as pu
    x = pu(3.5, 'm')
    y = pu(0.5, 's')
    print(x/y)

The above should print `7 m.s^-1`.  

### Functionnalities

Here is a (probably not exhaustive) list of what you can do with PhysUnits.
+ All the arithmetic operations (`+, -, *, /, **`), if they make sense in the 
context.
For instance, `+` will generate an error if the variables you are trying
to sum do not have the same unit. But you can do `a + 5` if `a` is a PhysUnit
with no unit.  
Integer arithmetic (`%, //` etc.) is not supported, but please create an
issue if you think it should.
+ All the assignment operators associated with the above supported operations.
You can for instance do `a **= 2` to directly store in `a` the result of `a**2`.
+ All the comprarison operators (`>=, <=,>, <, ==, !=`) with the condition that
the two operands have the same unit.
+ Unary operators: `-, +, abs`.
+ The `print_Latex()` method does what its name tells: return the Latex code 
that represents your variable. It is a method, so to use it do `a.print_Latex()`.
If you want to get the string without printing it (for instance to export it in
a file), use `__str_Latex__` instead.
