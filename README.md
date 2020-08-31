# vector_calculator
This repository provides a basic python class for representing vectors and performing vector operations.

## Constructor

The Vector.py file contains the code for the Vector class. The constructor of the Vector class accepts any number of comma-separated floating-point numbers 
as input. Because of this, the class supports all n-dimensional vectors.

## Methods

The Vector class uses operator overloading to allow for more user-friendly inputs for the vector operations of addition, 
subtraction, dot-product, and cross-product. All other operators are written as methods of the vector class.

Operators that take in another vector as a parameter assume the vectors are of the same length. These operaors will raise a ValueError if 
the two vectors do not have the same number of dimensions.

All operators both return the output of the operation and print the output to the console.

### +

The + operator returns the sum of two vectors

### -

The - operator returns the difference of two vectors.

### *

The * operator returns the dot product of two vectors.

### **

The ** operator returns the cross product of two vectors. 
**Note this operation only works for two and three dimensional vectors**

### scale(scalar)

The scale method accepts a floating-point number as a parameter and returns the scalar multiple of the original vector.

### get_length()

The get_length method returns the length of the vector

### get_unit_vector()

The get_unit_vector method returns a unit vector in the direction of the original vector.

### get_interior_angle(other, radians=True)

The get_interior_angle method accepts another vector and a boolean as parameters. The method calculates the interior angle 
between the original vector and the other vector in radians if the boolean is True and degrees if it is false.

### get_scalar_projection(other)

The get_scalar_projection method accepts another vector as a parameter and returns the scalar projection of the 
original vector onto the provided vector.

### get_vector_projection(other)

The get_vector_projection method accepts another vector as a parameters and returns the vector projection of the original vector onto the provided vector.

### is_perpendicular_to(other)

The is_perpendicular_to method accepts another vector as a parameter and returns a boolean to indicate whether or not the 
two vectors are perpendicular to one another.

### is_parallel_to(other)

The is_parallel_to method accepts another vector as a parameter and returns a boolean to indicate whether or not the 
two vectors are parallel to one another.

### print_summary()

The print_summary method prints the vector to the console. This method is utilized by all others to print the results of each operation.


