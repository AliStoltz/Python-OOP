####### defining class and methods #########

class User: 
  total_users = 0

  def __init__(self, name, email, password, account_type='user'):
    self.name = name
    self.email = email
    self.password = password
    self.account_type = account_type
    User.total_users += 1

  
  def __str__(self):
    return f"<Class User> - name = {self.name}, email = {self.email}, Memory Location = {hex(id(self))}"
    

  def greet(self):
    return f'Hi! My name is {self.name}. Account Type = {self.account_type}'

  
  @classmethod
  def decrement_total(cls):
    cls.total_users -= 1
    return cls.total_users


class Admin(User):
  def __init__(self, name, email, password, account_type, superpower='Coding all day'):
    super().__init__(name, email, password, account_type)
    self.superpower = superpower

  def greet(self):
    return f'Hi! My name is {self.name}. Account Type = {self.account_type}. My superpower is {self.superpower}!'