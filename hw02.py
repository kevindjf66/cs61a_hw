HW_SOURCE_FILE = 'hw02.py'

#############
# Questions #
#############

from operator import add, mul

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def summation(n, term):
    """Return the summation of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> summation(3, identity) # 1 + 2 + 3
    6
    >>> summation(5, identity) # 1 + 2 + 3 + 4 + 5
    15
    >>> summation(3, square)   # 1^2 + 2^2 + 3^2
    14
    >>> summation(5, square)   # 1^2 + 2^2 + 3^2 + 4^2 + 5^2
    55
    """
    "*** YOUR CODE HERE ***"
    i, total = 1, 0
    while i <= n:
        total = total + term(i)
        i += 1
    return total

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)   # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)   # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    """
    "*** YOUR CODE HERE ***"
    i, total = 1, 0
    while i <= n:
        total = total * term(i)
        i += 1
    return total

# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return product(n, identity)

def make_adder(n):
    return lambda n: n + k

def accumulate(combiner, base, n, term):
    i = 0
    while i <= n:
        base = combiner(base, term(i))
        i += 1
    return base

def summation_using_accumulate(n, term):
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    return accumulate(mul, 1, n, term)

def filtered_accumulate(combiner, base, pred, n, term):
    def combine_if(x, y):
        if pred(y):
            return combiner(x, y)
        else:
            return x
    return accumulate(combine_if, base, n, term)

def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    """
    i = 1
    while i <= n:
        n = f(n)
        i += 1
    return n

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h
