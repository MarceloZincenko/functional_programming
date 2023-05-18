#Factorial Recursion
def fact(n):
    if n == 0: 
        return 1
    else: 
        return n*fact(n-1)
    
#Reductions
start = lambda s, e, d: s
end = lambda s, e, d: e
dist = lambda s, e, d: d
latitude = lambda lat, lon: lat
longitude = lambda lat, lon: lon

point = ((35.505665, -76.653664), (35.508335, -76.654999), 0.1731)

print(start(*point)) # * operator maps each element of the tuple to each argument of the function
print(end(*point))
print(dist(*point))
print(latitude(*start(*point)))
print(longitude(*start(*point)))