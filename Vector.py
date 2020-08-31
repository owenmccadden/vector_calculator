import numpy as np


class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            self.values.append(i)
        self.dimensions = len(self.values)

    def __add__(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        new_vals = []
        for i in range(0, self.dimensions):
            new_vals.append(self.values[i] + other.values[i])
        v = Vector(*new_vals)
        v.print_summary()
        return v

    def __sub__(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        new_vals = []
        for i in range(0, self.dimensions):
            new_vals.append(self.values[i] - other.values[i])
        v = Vector(*new_vals)
        v.print_summary()
        return v

    def __mul__(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        sum = 0
        for i in range(0, self.dimensions):
            sum += self.values[i] * other.values[i]
        print(sum)
        return sum

    def __pow__(self, other, modulo=None):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        if self.dimensions == 2:
            v = Vector((self.values[0] * other.values[1]) - (self.values[1] * other.values[0]))
            v.print_summary()
            return v
        elif self.dimensions == 3:
            v = Vector(((self.values[1]*other.values[2]) - (self.values[2]*other.values[1])),
                           (-(self.values[0]*other.values[2]) + (self.values[2]*other.values[0])),
                           ((self.values[0]*other.values[1]) - (self.values[1]*other.values[0])))
            v.print_summary()
            return v
        else:
            raise ValueError("Too many dimensions.")

    def scale(self, scalar):
        new_vals = []
        for i in range(0, self.dimensions):
            new_vals.append(self.values[i] * scalar)
        v = Vector(*new_vals)
        v.print_summary()
        return v

    def get_length(self):
        total = 0
        for i in self.values:
            total += i ** 2
        print(np.sqrt(total))
        return np.sqrt(total)

    def get_unit_vector(self):
        new_values = []
        for i in range(0, self.dimensions):
            new_values.append(self.values[i] / self.get_length())
        n = Vector(*new_values)
        n.print_summary()
        return n

    def get_dot_product(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        dp = 0
        for i in range(0, self.dimensions):
            dp += (self.values[i] * other.values[i])
        return dp

    def get_interior_angle(self, other, radians=True):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        theta = np.arccos(self.get_dot_product(other) / (self.get_length() * other.get_length()))
        if radians:
            print(theta)
            return theta
        else:
            print(np.rad2deg(theta))
            return np.rad2deg(theta)

    def get_scalar_projection(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        sp = self.get_dot_product(other) / other.get_length()
        print(sp)
        return sp

    def get_vector_projection(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        uv = other.get_unit_vector()
        scalar = self.get_scalar_projection(other)
        print(uv.scale(scalar))
        return uv.scale(scalar)

    # def get_cross_product(self, other):
    #     if self.dimensions != other.dimensions:
    #         raise ValueError("Vectors must have same Dimensions")
    #     if self.dimensions == 2:
    #         return Vector((self.values[0] * other.values[1]) - (self.values[1] * other.values[0]))
    #     elif self.dimensions == 3:
    #         return Vector(((self.values[1]*other.values[2]) - (self.values[2]*other.values[1])),
    #                        ((self.values[0]*other.values[2]) - (self.values[2]*other.values[0])),
    #                        ((self.values[0]*other.values[1]) - (self.values[1]*other.values[0])))
    #     else:
    #         print('error too many dimensions')
    #         return None

    def is_perpendicular_to(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        if self.get_dot_product(other) == 0:
            print(True)
            return True
        else:
            print(False)
            return False

    def is_parallel_to(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have same Dimensions")
        parallel = True
        scalar = self.values[0] / other.values[0]
        for i in range(1, self.dimensions):
            if self.values[i] / other.values[i] != scalar:
                parallel = False
        print(parallel)
        return parallel

    def print_summary(self):
        output = '<'
        for i in range(0, self.dimensions):
            if i < self.dimensions - 1:
                output += str(self.values[i]) + ',' + ' '
            else:
                output += str(self.values[i]) + '>'
        print(output)


