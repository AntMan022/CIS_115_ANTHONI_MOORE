#this program will calculate sales tax

itemprice = 75.34
sales_tax = .0725

itemTax = itemprice * sales_tax
totalprice = itemTax + itemprice

print(f"The price for the item is {itemprice} The total price for the item with tax is {totalprice:.2f}")
