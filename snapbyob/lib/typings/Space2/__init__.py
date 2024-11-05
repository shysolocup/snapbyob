import asyncio;
import math;


class Space2:
    def __init__(self, x: int | float = None, y:int | float = None):
        self.x = float(x);
        self.y = float(y);

    def __str__(self):
        return "{ " + str(self.x) + ", " + str(self.y) + " }";

    def __int__(self):
        return self.x, self.y;

    def __float__(self):
        return float(self.x), float(self.y);

    def __complex__(self):
        return complex(self.x), complex(self.y);

    def __oct__(self):
        return oct(self.x), oct(self.y);

    def __hex__(self):
        return hex(self.x), hex(self.y);

    def __invert__(self):
        return Space2(((-self.x) - 1), ((-self.y) - 1))
    
    def __neg__(self):
        return Space2(-self.x, -self.y);

    def __round__(self, n=0):
        return Space2(round(self.x, n), round(self.y, n))

    def __abs__(self):
        return Space2(abs(self.x), abs(self.x));

    def __floor__(self):
        return Space2(math.floor(self.x), math.floor(self.y));

    def __ceil__(self):
        return Space2(math.ceil(self.x), math.ceil(self.x));

    def __trunc__(self):
        return Space2(math.trunc(self.x), math.trunc(self.y));

    def __add__(self, a):
        if type(a) == Space2:
            return Space2(self.x + a.x, self.y + a.y);
        else:
            return Space2(self.x + a, self.y + a);

    def __sub__(self, a):
        if type(a) == Space2:
            return Space2(self.x - a.x, self.y - a.y);
        else:
            return Space2(self.x - a, self.y - a);

    def __mul__(self, a):
        if type(a) == Space2:
            return Space2(self.x * a.x, self.y * a.y);
        else:
            return Space2(self.x * a, self.y * a);

    def __div__(self, a):
        if type(a) == Space2:
            return Space2(self.x / a.x, self.y / a.y);
        else:
            return Space2(self.x / a, self.y / a);

    def __mod__(self, a):
        if type(a) == Space2:
            return Space2(self.x % a.x, self.y % a.y);
        else:
            return Space2(self.x % a, self.y % a);

    def __pow__(self, a):
        if type(a) == Space2:
            return Space2(self.x ** a.x, self.y * a.y);
        else:
            return Space2(self.x ** a, self.y ** a);

    def __floordiv__(self, a):
        if type(a) == Space2:
            return Space2(self.x // a.x, self.y // a.y);
        else:
            return Space2(self.x // a, self.y // a);

    def __lshift__(self, a):
        if type(a) == Space2:
            return Space2(self.x << a.x, self.y << a.y);
        else:
            return Space2(self.x << a, self.y << a);

    def __rshift__(self, a):
        if type(a) == Space2:
            return Space2(self.x >> a.x, self.y >> a.y);
        else:
            return Space2(self.x >> a, self.y >> a);

    def __iadd__(self, a):
        if type(a) == Space2:
            self.x += a.x;
            self.y += a.y;
        else:
            self.x += a;
            self.y += a;
    
        return self;

    def __isub__(self, a):
        if type(a) == Space2:
            self.x -= a.x;
            self.y -= a.y;
        else:
            self.x -= a;
            self.y -= a;
    
        return self;

    def __imul__(self, a):
        if type(a) == Space2:
            self.x *= a.x;
            self.y *= a.y;
        else:
            self.x *= a;
            self.y *= a;
    
        return self;

    def __idiv__(self, a):
        if type(a) == Space2:
            self.x /= a.x;
            self.y /= a.y;
        else:
            self.x /= a;
            self.y /= a;
    
        return self;

    def __imod__(self, a):
        if type(a) == Space2:
            self.x %= a.x;
            self.y %= a.y;
        else:
            self.x %= a;
            self.y %= a;
    
        return self;

    def __ipow__(self, a):
        if type(a) == Space2:
            self.x **= a.x;
            self.y **= a.y;
        else:
            self.x **= a;
            self.y **= a;
    
        return self;

    def __ilshift__(self, a):
        if type(a) == Space2:
            self.x <<= a.x;
            self.y <<= a.y;
        else:
            self.x <<= a;
            self.y <<= a;
    
        return self;

    def __irshift__(self, a):
        if type(a) == Space2:
            self.x >>= a.x;
            self.y >>= a.y;
        else:
            self.x >>= a;
            self.y >>= a;
    
        return self;

    def __ifloordiv__(self, a):
        if type(a) == Space2:
            self.x //= a.x;
            self.y //= a.y;
        else:
            self.x //= a;
            self.y //= a;
    
        return self;

    def __eq__(self, a):
        if type(a) == Space2:
            return self.x == a.x and self.y == a.y
        else:
            return self.x == a and self.y == a

    def __ge__(self, a):
        if type(a) == Space2:
            return self.x >= a.x and self.y >= a.y
        else:
            return self.x >= a and self.y >= a
    
    def __le__(self, a):
        if type(a) == Space2:
            return self.x <= a.x and self.y <= a.y
        else:
            return self.x <= a and self.y <= a
    
    def __gt__(self, a):
        if type(a) == Space2:
            return self.x > a.x and self.y > a.y
        else:
            return self.x > a and self.y > a
    
    def __lt__(self, a):
        if type(a) == Space2:
            return self.x < a.x and self.y < a.y
        else:
            return self.x < a and self.y < a