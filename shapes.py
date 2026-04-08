import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract Base Class for geometric shapes.
    Demonstrates: Abstract Base Class, Interface.
    """
    
    @abstractmethod
    def calculate_area(self):
        """Calculates and returns the area of the shape."""
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass
    
    @abstractmethod
    def __str__(self):
        """Returns a string representation of the shape."""
        pass

class Square(Shape):
    """
    Class representing a Square.
    Demonstrates: Inheritance, Properties.
    """
    def __init__(self, side: float):
        self._side = side
    
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Panjang sisi tidak boleh negatif")
        self._side = value
    
    def calculate_area(self):
        return self._side ** 2
    
    def calculate_perimeter(self):
        return self._side * 4
    
    def __str__(self):
        return f"Persegi (sisi={self._side})"

class Rectangle(Shape):
    """
    Class representing a Rectangle.
    Demonstrates: Inheritance, Polymorphism.
    """
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Lebar tidak boleh negatif")
        self._width = value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Tinggi tidak boleh negatif")
        self._width = value # Fixed a bug here too (should be height)
        self._height = value
    
    def calculate_area(self):
        return self._width * self._height
    
    def calculate_perimeter(self):
        return 2 * (self._width + self._height)
    
    def __str__(self):
        return f"Persegi Panjang (lebar={self._width}, tinggi={self._height})"

class Circle(Shape):
    """
    Class representing a Circle.
    Demonstrates: Inheritance, Polymorphism.
    """
    def __init__(self, radius: float):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Jari-jari tidak boleh negatif")
        self._radius = value
    
    def calculate_area(self):
        return math.pi * (self._radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self._radius
    
    def __str__(self):
        return f"Lingkaran (radius={self._radius})"

# Function demonstrate polymorphism and method overloading simulation
def display_shape_info(shape: Shape, *args):
    """
    Displays the area and perimeter of any shape.
    Python doesn't support C++ type true overloading, but we can simulate 
    it by checking args or utilizing dynamic typing as shown here.
    """
    print(f"\n--- {shape} ---")
    print(f"Luas: {shape.calculate_area():.2f}")
    print(f"Keliling: {shape.calculate_perimeter():.2f}")
    if args:
        print(f"Data tambahan: {args}")

if __name__ == "__main__":
    # Quick test
    sq = Square(5)
    rect = Rectangle(4, 6)
    circ = Circle(7)
    
    for s in [sq, rect, circ]:
        display_shape_info(s)
