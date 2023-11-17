import math

def dotproduct(x: tuple, y: tuple) -> float:
    return (x[0] * y[0] + x[1] * y[1])

def abs(x: tuple) -> float:
    return math.sqrt(dotproduct(x, x))