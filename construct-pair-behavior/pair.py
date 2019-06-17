def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a;
    return f(left)

def cdr(f):
    def right(a, b):
        return b;
    return f(right)

def add(f):
    def add1(a, b):
        return a + b;
    return f(add1)

p = cons(3, 4);
print(car(p))
print(cdr(p))
print(add(p))
