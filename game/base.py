import collections
import math
import os

# for file name
def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath

# for axis
def line(a,b,x,y):
    import turtle
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)

# a vector class to calculate
class vector(collections.Sequence):
    PRECISION = 6
    __slots__ = ('_x','_y','_hash')

    def __init__(self,x,y): #initializing the variables
        self._hash = None
        self._x = round(x,self.PRECISION)
        self._y = round(y,self.PRECISION)
    
    @property #getter for x
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        if self._hash is not None:
            raise ValueError('Cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @property #getter for y
    def y(self):
        return self._y

    @x.setter
    def y(self,value):
        if self._hash is not None:
            raise ValueError('Cannot set y after hashing')
        self._y = round(value, self.PRECISION)
    
    def __hash__(self):
        #V.__hash__() -> hash(v)
        # v = vector(1,2)
        # '''h = hash(v) v.x = 2 give value error'''
        if self._hash is none:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        
        return self._hash
    
    def __len__(self):
        return 2 #vector dimention will always be 2

    def __getitem__(self,index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            return IndexError

        
    def copy(self):
        """
        v = vector(1,2)
        w = v.copy()
        v is w (False)
        """
        type_self = type(self)
        return type_self(self.x,self.y)

    def __eq__(self,other): #here other is vector components
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y #this will return a bool type
        return NotImplemented #if it is not a vector component

    def __ne__(self, other):
        if isinstance(other, vector):
            return self.x != other.x and self.y != other.y
        return NotImplemented
    
    def __iadd__(self, other):
        # v.__iadd__(w) -> v += w
        if self._hash is not None:
            return ValueError("can't add vector after hashing")
        elif isinstance(other,vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self


    def __add__(self,other):
        # v.__add__(w) > v + w
        copy = self.copy()
        return copy.__iadd__(other)
    
    __radd__ = __add__
    def move(self.other):
        # move vector by other(n place)
        # v = vector(1,2) w = vector(3,4) v.movee(w) v ==> vector(4,6)
        self.__iadd__(other)
    
    def __isub__(self, other):
        # v.__isub__(w) -> v -= w
        if self._hash  is not None:
            raise ValueError('can\'t subtract vector after hashing')
        elif isinstance(other, vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __sub__(self, other):
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self,other):
        if self._hash is not None:
            raise ValueError("can't mulply vector after hashing")
        elif isinstance(other, vector):
            self.x *= other.x
            self.y *= other.x
        else:
            self.x *= other
            self.y *= other
        reurn self

    def __mul__(self,other):
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __imul__

    def scale(self,other):
        self.__imul__(other):

    def __itruediv__(self, other):
        if self._has is not None:
            raise ValueError("can't devide vector after hashing")
        elif isinstance(other, vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return self
    
    def __truediv__(self,other):
        copy = self.copy()
        return copy.__itruediv__(other)
    
    def __neg__(self):
        # this will give us a negative vector
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy
    
    def __abs__(self):
        # vector(3,4) => 5
        return (self.x**2+self.y**2)**0.5

    def rotate(self, angle):
        
