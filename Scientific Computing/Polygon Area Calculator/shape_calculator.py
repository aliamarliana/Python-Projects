class Rectangle:

  #Initialize the class with width and height
  def __init__(self, width, height):
    self.width = width
    self.height = height

  #set_width method
  def set_width(self, width):
    self.width = width

  #set_height method
  def set_height(self, height):
    self.height = height

  #get_area method (returns area) => width * height
  def get_area(self):
    return self.width * self.height

  #get_perimeter method (returns perimeter) => 2 * width + 2 * height
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  #get_diagonal method (returns diagonal) => (width ** 2 + height ** 2) ** .5
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  #get_picture method (returns a string that represents the shape using lines of "*"
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*" * self.width + "\n"
      return picture

  #get_amount_inside method (takes another shape (square or rectangle) as an argument)
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  #instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  #Initialize the class with side
  def __init__(self, side):
    super().__init__(side, side)

  #set_side method
  def set_side(self, side):
    self.width = side
    self.height = side

  #set_width method
  def set_width(self, width):
    self.width = width

  #set_height method
  def set_height(self, height):
    self.height = height

  #instance of a Square is represented as a string, it should look like: Square(side=9)
  def __str__(self):
    return f"Square(side={self.width})"
