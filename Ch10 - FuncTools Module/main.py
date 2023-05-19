from functools import lru_cache
from functools import total_ordering

@lru_cache(128)
def fibc(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibc(n-1) + fibc(n-2)

print(fibc(20))

"""the @total_ordering decorator handles the construction of all other comparisons. 
In both cases, we've allowed comparisons between cards and also between a card and a number"""
@total_ordering
class Card(tuple):
    __slots__ = ()
    
    def __new__( class_, rank, suit ):
        obj= tuple.__new__(Card, (rank, suit))
        return obj
    
    def __repr__(self):
        return "{0.rank}{0.suit}".format(self)
    
    @property
    def rank(self):
        return self[0]
    
    @property
    def suit(self):
        return self[1]
    
    def __eq__(self, other):
        if isinstance(other,Card):
            return self.rank == other.rank
        elif isinstance(other,int):
            return self.rank == other
    
    def __lt__(self, other):
        if isinstance(other,Card):
            return self.rank < other.rank
        elif isinstance(other,int):
            return self.rank < other
    
    