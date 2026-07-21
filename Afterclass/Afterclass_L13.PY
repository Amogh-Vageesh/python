def calculate_item_cost(price, quantity):
  return price * quantity


def calculate_tax(subtotal, tax_rate):
  return subtotal * tax_rate


def print_bill(item_name, item_cost, tax_amount, final_total):
  print("--- Art Supplies Bill ---")
  print(f"Item: {item_name}")
  print(f"Cost: ${item_cost:.2f}")
  print(f"Tax: ${tax_amount:.2f}")
  print(f"Total: ${final_total:.2f}")


# Main program execution
name = "Paintbrush"
price_per_unit = 4.50
qty = 3
tax_percentage = 0.08

subtotal = calculate_item_cost(price_per_unit, qty)
tax = calculate_tax(subtotal, tax_percentage)
total = subtotal + tax

print_bill(name, subtotal, tax, total)
