class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        new_int_set = intSet()
        for number in self.vals:
            if other.member(number):
                new_int_set.insert(number)
        return new_int_set

    def __len__(self):
        return len(self.vals)

"""
Used for running, do not include when submitting to grader
"""
if __name__ == "__main__":
    int_set1 = intSet()
    int_set1.insert(2)
    int_set1.insert(3)
    int_set1.insert(4)
    int_set1.insert(5)

    int_set2 = intSet()
    int_set2.insert(4)
    int_set2.insert(5)
    int_set2.insert(6)
    int_set2.insert(7)

    int_set3 = int_set1.intersect(int_set2)
    print(int_set3)
    print("Length of int_set3: {}".format(len(int_set3)))

"""
End Runner Code
"""
