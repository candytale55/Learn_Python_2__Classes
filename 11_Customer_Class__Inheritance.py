""" ReturningCustomer class inherits from parent class Customer. 
Note that we don’t define the display_cart method in the body of ReturningCustomer, 
but it will still have access to that method via inheritance."""



class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"



class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()






""" Inheritance is the process by which one class takes on the attributes and methods of another, 
and it’s used to express an is-a relationship. 
For example, a Panda is a bear, so a Panda class could inherit from a Bear class. 
However, a Toyota is not a Tractor, so it shouldn’t inherit from the Tractor class 
(even if they have a lot of attributes and methods in common). 
Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class."""
