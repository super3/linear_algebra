import unittest
from linear_algebra.Vector import Vector


class VectorTest(unittest.TestCase):

    def test_vector_add(self):
        v1 = Vector([1, 2])
        v2 = Vector([3, 1])

        result = Vector([4, 3])
        self.assertEqual(v1 + v2, result)

    def test_vector_subtract(self):
        v1 = Vector([1, 3])
        v2 = Vector([5, 1])

        result = Vector([-4, 2])
        self.assertEqual(v1 - v2, result)

    def test_vector_scale(self):
        v1 = Vector([1, 2])
        v2 = Vector([3, 2, 1])

        result1 = Vector([2, 4])
        result2 = Vector([-1.5, -1, -0.5])

        self.assertEqual(v1 * 2, result1)
        self.assertEqual(v2 * (-0.5), result2)

    def test_prob_set_1(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])

        v3 = Vector([7.119, 8.215])
        v4 = Vector([-8.223, 0.878])

        v5 = Vector([1.671, -1.012, -0.318])

        result1 = Vector([7.089, -7.23])
        result2 = Vector([15.342, 7.337])
        result3 = Vector([12.382, -7.499, -2.356])

        self.assertEqual(v1 + v2, result1)
        self.assertEqual(v3 - v4, result2)
        self.assertEqual(v5*7.41, result3)

    def prob_set_2(self):
        v1 = Vector([-0.221, 7.437])
        v2 = Vector([8.813, -1.331, -6.247])
        v3 = Vector([5.581, -2.136])
        v4 = Vector([1.996, 3.108, -4.554])
