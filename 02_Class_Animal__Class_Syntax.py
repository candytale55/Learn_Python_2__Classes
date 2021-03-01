# A basic class consists only of the class keyword, the name of the class, and the class from which the new class inherits in parentheses.  
# For now, our classes will inherit from the _object_ class. 

# This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.


class NewClass(object):
  # Class magic here
  pass

# pass doesn’t do anything, but it’s useful as a placeholder in areas of your code where Python expects an expression.



class NewClass(object):
  # Class magic here
  pass


# __init__()
#  we start our class definition off with an odd-looking function: __init__(), required for classes, and it’s used to initialize the objects it creates. 

# __init__() always takes at least one argument, self, that refers to the object being created. You can think of __init__() as the function that “boots up” each object the class creates.


class Animal(object):
  def __init__(self):
    pass


# https://discuss.codecademy.com/t/what-does-it-mean-to-inherit-from-the-object-class/340587
# https://discuss.codecademy.com/t/what-is-the-difference-between-a-class-and-an-object/340593
