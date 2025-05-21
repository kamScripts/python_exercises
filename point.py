import math
import copy
import print_attributes 
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __add__(self, other):
        """Type-based dispatch, dispatches the computation to different methods
        based on the type of the arguments.
        """
        if isinstance(other, Point):
            return self.add_points(other)
        
        return self.add_tuple(other)
    def __radd__(self, other):
        """Do a computation if other is placed as a first arg"""
        return self.__add__(other)
    def print_point(self):
        print(str(self))
    def add_tuple(self, t):
        """Add point if coordinates are in a form of a tuple
        t: tuple (x,y).
        Returns Point"""
        dx=self.x+ t[0]
        dy=self.y+ t[1]
        return Point(dx,dy)
    def add_points(self, other):
        """Add points
        other: Point
        Returns Point"""
        dx=self.x + other.x
        dy=self.y + other.y
        return Point(dx, dy)

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner x, corner y coordinates.
    """
    def __init__(self,width, height, corner_x, corner_y):
        self.width=width
        self.height=height
        self.corner=Point(corner_x, corner_y)
    def find_center(self):
        """Find center of the rectangle"""
        x=self.corner.x + self.width/2
        y=self.corner.y + self.height/2
        p=Point(x,y)
        return p
    def move_rect(self, dx, dy):
        """Move the Rectangle by modifying its corner object.

        rect: Rectangle object.
        dx: change in x coordinate (can be negative).
        dy: change in y coordinate (can be negative).
        """
        self.corner.x+=dx
        self.corner.y+=dy
class Circle:
    """Represents a circle
    attributes: center, radius"""
    def __init__(self, radius, center_x, center_y):
        self.radius = radius
        self.center = Point(center_x, center_y)
    def point_in_circle(self, point:Point):
        """Check if point lies in or on the boundary of the circle"""
        is_in_circle=(point.x- self.center.x)**2+(point.y-self.center.y)**2<=self.radius**2
        return is_in_circle



              
def distance_between_two_points(p1:Point, p2:Point):
    """Calculate distance between 2 points in 2-D space.
    p1: Point (x,y)
    p2: Point (x,y)
    Returns: float
    """
    return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
def move_and_copy_rect(rect:Rectangle, dx, dy):
    """Move and the Rectangle by making a deep copy of its corner object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    Returns: Rectangle obj.
    """
    r=copy.deepcopy(rect)
    r.move_rect(dx, dy)
    return r

if __name__=='__main__':
    point_1=Point(3,2)
    point_2=Point(5,5)
    d_p1_p2=distance_between_two_points(point_1, point_2)
    print(d_p1_p2)
    box=Rectangle(100,200,0,0)
    center=box.find_center()
    center.print_point()
    # copy.copy creates a shallow copy so to copy object and all referring objects use deepcopy
    box2=copy.deepcopy(box)
    p1=Point(10,50)
    p2=Point(7,3)
    p3=p1+p2
    p4=(3,7)+p3
    print(p1,p2,p3,p4, sep='\t')
    
print_attributes.print_attributes(p4)
