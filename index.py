# Interface for shapes
class Shape:
  def calculate_area(self):
    raise NotImplementedError("Subclasses must implement this method")

# Base class for geometric shapes
class GeometricShape(Shape):
  def __init__(self, name):
    self.name = name

# Rectangle class inheriting from GeometricShape
class Rectangle(GeometricShape):
  def __init__(self, name, length, width):
    super().__init__(name)
    self.length = length
    self.width = width

  # Override the inherited calculate_area method
  def calculate_area(self):
    return self.length * self.width

# Function to read data from a file and create Rectangle objects
def create_rectangles_from_file(filename):
  rectangles = []
  with open(filename, 'r') as file:
    for line in file:
      data = line.strip().split(',')  # Split line by comma
      name, length, width = data[0], float(data[1]), float(data[2])
      rectangles.append(Rectangle(name, length, width))
  return rectangles

# Main program
rectangles = create_rectangles_from_file("rectangles.txt")

# Loop through rectangles and print their details
for rect in rectangles:
  print(f"Rectangle: {rect.name}, Area: {rect.calculate_area()}")
