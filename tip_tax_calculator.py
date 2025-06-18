# define function tip_tax_calculator()
def tip_tax_calculator():
  # ask for subtotal, tip %, tax %
  subtotal = float(input("Enter Subtotal: "))
  tip_prcnt = float(input("Enter tip percentage: "))
  tax_prcnt = float(input("Enter tax percentage: "))
  # get Tip amount = subtotal × (tip / 100)
  tip_amount = subtotal * (tip_prcnt/100)
  # get Tax amount = subtotal × (tax / 100)
  tax_amount = subtotal * (tax_prcnt/100)
  # Total = subtotal + tip amount + tax amount
  total = subtotal + tip_amount + tax_amount
  # Print tip, tax and total amount
  print(f"Tip amount: ${tip_amount:.2f}")
  print(f"Tax amount: ${tax_amount:.2f}")
  print(f"Total amount: ${total:.2f}")
# call function
tip_tax_calculator()