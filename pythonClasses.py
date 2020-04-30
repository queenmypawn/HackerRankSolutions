#!/bin/python

import math
import os
import random
import re
import sys

# Create two classes in Python.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        areaOfRect = self.length*self.width
        return areaOfRect

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        areaOfCircle = (math.pi)*(self.radius**2)
        return areaOfCircle

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input())
    queries = []
    for _ in xrange(q):
        args = raw_input().split()
        shape_name, params = args[0], map(int, args[1:])
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
