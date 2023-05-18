import math 
#Common wrapping functions
fst = lambda x: x[0]
snd = lambda x: x[1]

#all() and any() functions
def isprime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return not any(p==0 for p in range(3,int(math.sqrt(n))+1,2))

someset = set([3,4,5,6,7,8,9,10])
print(all(isprime(x) for x in someset))
print(not all(isprime(x) for x in someset))
print(any(not isprime(x) for x in someset))

#using zip
xi = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
yi = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]
print(list(zip( xi, yi )))

#What happens where then are no arguments at all?
a = zip()
print(zip())
print(list(a))

#What happens where there's only one argument?
b = zip( (1,2,3) )
print(list(b))

#What happens when the sequences are different lengths?
c = list(zip((1, 2, 3), ('a', 'b')))
print(list(c))
