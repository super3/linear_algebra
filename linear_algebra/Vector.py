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
            coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(coordinates)

    def subtract(self, v):
        """Vector subtraction."""
        self.eq_dimension(v)

    def scale(self, v):
        """Vector scaling/multiplication."""
        self.eq_dimension(v)