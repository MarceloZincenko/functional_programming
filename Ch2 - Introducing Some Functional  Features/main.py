#Functions as first class objects
def example(a, b, **kw):
    return a*b

type(example)
example.__code__.co_varnames
example.__code__.co_argcount

#Not pure function
global_adjustment = 2
def some_function(a, b, t):
 return a+b*t+global_adjustment

print(some_function(1,2,3))

#max() as high order function
year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003,30.66), (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5), (2008, 32.84), (2009, 33.02), (2010, 32.92)]
print(max(year_cheese, key=lambda yc: yc[1]))

#other way to do it unwrap(process(wrap(structure)))
print(max(map(lambda yc: (yc[1],yc), year_cheese))[1])