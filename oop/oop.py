# ============================================
# STEP 1: DEFINE A SIMPLE CLASS (Shape)
# ============================================
import turtle

class Shape:
    def __init__(self, t, size):
        self.t = t
        self.size = size   # basic attribute


# ============================================
# STEP 2: CREATE OBJECTS FROM THE CLASS
# Two objects using the same class
# ============================================
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(3)

square = Shape(pen, 80)     # object 1
triangle = Shape(pen, 100)  # object 2


# ============================================
# STEP 3: ENCAPSULATION
# Define methods *inside* the class to hide drawing details
# ============================================
def draw_square(self):
    for _ in range(4):
        self.t.forward(self.size)
        self.t.right(90)

def draw_triangle(self):
    for _ in range(3):
        self.t.forward(self.size)
        self.t.left(120)

# Attach methods to class (simple for teaching)
Shape.draw_square = draw_square
Shape.draw_triangle = draw_triangle

square.t.penup(); square.t.goto(-120, 0); square.t.pendown()
square.draw_square()

triangle.t.penup(); triangle.t.goto(120, 0); triangle.t.pendown()
triangle.draw_triangle()


# ============================================
# STEP 4: INHERITANCE
# A subclass that inherits Shape
# (realisation ≠ inheritance — realisation means creating objects)
# ============================================
class FancyShape(Shape):
    def __init__(self, t, size, color):
        super().__init__(t, size)
        self.color = color


# ============================================
# STEP 5: POLYMORPHISM
# Override a method in the subclass
# ============================================
class FancyShape(Shape):
    def __init__(self, t, size, color):
        super().__init__(t, size)
        self.color = color

    # polymorphism: same method name, different behavior
    def draw_square(self):
        self.t.color(self.color)
        for _ in range(4):
            self.t.forward(self.size)
            self.t.right(90)

fancy = FancyShape(pen, 60, "blue")
fancy.t.penup(); fancy.t.goto(0, -150); fancy.t.pendown()
fancy.draw_square()


# ============================================
# STEP 6: ABSTRACTION
# User calls simple methods without knowing drawing logic
# ============================================
# A method that hides everything behind one simple call
def draw_shape(self, shape_type):
    if shape_type == "square":
        self.draw_square()
    elif shape_type == "triangle":
        self.draw_triangle()

Shape.draw_shape = draw_shape

triangle.t.penup(); triangle.t.goto(0, 150); triangle.t.pendown()
triangle.draw_shape("triangle")

turtle.done()
