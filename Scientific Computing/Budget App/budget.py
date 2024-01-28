class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  #Accepts an amount and description
  #If no description is given, it should default to an empty string.
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  #Store amount as a negative number
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  #Returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  def get_balance(self):
    return sum(item['amount'] for item in self.ledger)

  #Transfer method that accepts an amount and another budget category as arguments.
  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  #Check funds method that accepts an amount as an argument.
  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    output = f"{'*' * ((30 - len(self.category)) // 2)}{self.category}{'*' * ((30 - len(self.category)) // 2)}\n"
    for item in self.ledger:
      output += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
    output += f"Total: {self.get_balance():.2f}"
    return output


#Show percentage spent in each category passed
def create_spend_chart(categories):

  #Calculate total withdrawals for each category
  category_withdrawals = []

  for category in categories:
    total_withdrawals = sum(
        abs(transaction["amount"]) for transaction in category.ledger
        if transaction["amount"] < 0)
    category_withdrawals.append(total_withdrawals)

  #Calculate totals and derive percentages for the bar graph
  total = sum(category_withdrawals)
  percentage = [
      withdrawal / total * 100 for withdrawal in category_withdrawals
  ]
  print(percentage)

  #Title
  chart = "Percentage spent by category" + "\n"

  #Create labels list and append to the chart string
  labels = []

  for decile in range(100, -1, -10):
    number_label = str(decile).rjust(3) + "|"
    labels.append(number_label)
    chart += number_label

    for p in percentage:
      chart += " o " if p > decile else "   "

    chart += " " + "\n"

  #Add bottom line
  bottom_line = (4 * " ") + (len(categories) * "---") + "-"
  chart += bottom_line

  #Get information for titles
  category_lengths = [len(category.category) for category in categories]
  max_category_lengths = max(category_lengths)

  #Assign number of lines based on max category length
  title_line = ""

  for i in range(max_category_lengths):
    title_line += "\n" + (4 * " ")

    for j in range(len(categories)):
      if i < category_lengths[j]:
        title_line += f" {categories[j].category[i]} "
      else:
        title_line += "   "

    title_line += " "

  chart += title_line

  return chart
