

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Coordinate({},{})".format(self.x, self.y)

"""
Used for running, do not include when submitting to grader
"""
if __name__ == "__main__":
    coordinate1 = Coordinate(2, 3)
    coordinate2 = Coordinate(2, 3)
    coordinate3 = Coordinate(3, 4)

    print("coordinate1 and coordinate2: {}".format(coordinate1 == coordinate2))
    print("coordinate2 and coordinate3: {}".format(coordinate2 == coordinate3))

    print("Representation of coordiante1: {}".format(repr(coordinate1)))

"""
End Runner Code
"""
