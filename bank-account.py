class BankAccount:
  def __init__(self):
    self.balance = 0
    self.interest_rate = .02

  def deposit(self, amount):
    if amount <= 0:
      print('Cannot deposit a negative amount')
    else:
      self.balance += amount
      return self.balance 
    
  def withdraw(self, amount):
    if self.balance <= amount:
      self.balance -= self.overdraft_penalty
      print("Insufficiant Funds")
    else:
      self.balance -= amount
      return amount
    
  