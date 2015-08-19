import unittest
from linear_algebra.Vector import Vector


class VectorTest(unittest.TestCase):

    def test_vector_add(self):
        v1 = Vector([1, 2])
        v2 = Vector([3, 1])

        result = Vector([4, 3])
        self.assertEqual(result, v1 + v2)
