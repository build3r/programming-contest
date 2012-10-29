from math import factorial
import functools
 
def memoize(func):
    cache = {}
    def memoized(key):
        # Returned, new, memoized version of decorated function
        if key not in cache:
            cache[key] = func(key)
        return cache[key]
    return functools.update_wrapper(memoized, func)
 
 
@memoize
def fact(n):
    return factorial(n)
 
def cat_direct(n):
    return fact(2*n) // fact(n + 1) // fact(n)
 
@memoize    
def catR1(n):
    return ( 1 if n == 0
             else sum( catR1(i) * catR1(n - 1 - i)
                       for i in range(n) ) )
 
@memoize    
def catR2(n):
    return ( 1 if n == 0
             else ( ( 4 * n - 2 ) * catR2( n - 1) ) // ( n + 1 ) )
 
 
if __name__ == '__main__':
    import sys
    n = int(sys.stdin.readline())
    print cat_direct(n) % 1000000007
