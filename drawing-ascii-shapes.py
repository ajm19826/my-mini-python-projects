class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)

class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)

class Triangle(Shape):
    # This method prints 'i + 1' characters for each row 'i'
    def printRow(self, i):
        print(self.printChar * (i + 6))

# Example usage:
triangle_shape = Triangle()
triangle_shape.print()
