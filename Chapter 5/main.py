# Format ((x1,y1), (x2,y2), distance)
tuples = (((37.54901619777347, -76.33029518659048), (37.840832, -76.273834), 17.7246), ((37.840832, -76.273834), (38.331501, -76.459503), 30.7382), ((38.331501, -76.459503), (38.845501, -76.537331), 31.0756), ((36.843334, -76.298668), (37.549, -76.331169), 42.3962), ((37.549, -76.331169), (38.330166, -76.458504), 47.2866), ((38.330166, -76.458504), (38.976334, -76.473503), 38.8019))

# Get the max and min distance

#using max and a defined function
def by_dist(leg: tuple) -> float:
    lat, lon, dist = leg
    return dist

long, short = max(tuples, key=by_dist), min(tuples, key=by_dist)
print(long, short)

#using lambda function
long, short = max(tuples, key=lambda leg: leg[2]), min(tuples, key=lambda leg: leg[2])

#Convert miles to statue miles
start = lambda x: x[0]
end = lambda x: x[1]
d = lambda x: x[2]
statute_miles = tuple(map(lambda x: (start(x), end(x), d(x)*6076.12/5280), tuples))
print(statute_miles)

#Filter data
long= list(filter(lambda leg: d(leg) >= 5, tuples))
print(long)

#Using iter
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tail = iter(elements.pop, 5)
print(list(tail))

