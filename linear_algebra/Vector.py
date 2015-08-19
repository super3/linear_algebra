class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def eq_dimension(self, v):
        if not self.dimension == v.dimension:
            raise ValueError('Vectors must be of equal dimension')

    def __add__(self, v):
        """Vector addition."""
        coordinates = []
        self.eq_dimension(v)
        for i in range(self.dimension):
            coordinates.append(round(self.coordinates[i] + v.coordinates[i], 3))
        return Vector(coordinates)

    def __sub__(self, v):
        """Vector subtraction."""
        coordinates = []
        self.eq_dimension(v)
        for i in range(self.dimension):
            coordinates.append(round(self.coordinates[i] - v.coordinates[i], 3))
        return Vector(coordinates)

    def __mul__(self, c):
        """Vector scaling/multiplication."""
        coordinates = []
        for i in range(self.dimension):
            coordinates.append(round(self.coordinates[i] * c, 3))
        return Vector(coordinates)