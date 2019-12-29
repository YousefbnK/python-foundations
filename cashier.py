list_of_items = []

stop = "go"

while stop != "done":
	items = {}
	name = input("Item (enter \"done\" when finished):   ")
	price = float(input("Price:   "))
	quantity = int(input("Quantity:   "))

	items["name"] = name
	items["price"] = price
	items["quantity"] = quantity

	list_of_items.append(items)

	stop = input("Press anything to continue or enter \"done\" when finished:   ")

	
print('-'*20)
print("receipt")
print('-'*20)

grand_total = []

for items in list_of_items:
	item_total = items["price"] * items["quantity"]
	grand_total.append(item_total)
	print(items["quantity"], items["name"], items["price"])

print("-"*20)

sum = sum(grand_total)
print("Total Price:", (sum))
