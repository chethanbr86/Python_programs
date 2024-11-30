class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Width must be positive')
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print('Height must be positive')

    @width.deleter
    def width(self):
        del self._width
        print('Width deleted')

    @height.deleter
    def height(self):
        del self._height
        print('Height deleted')

rectangle = Rectangle(10, -20)

rectangle.width = -30
rectangle.height = 40

print(rectangle.width, rectangle.height)

del rectangle.width
del rectangle.height

