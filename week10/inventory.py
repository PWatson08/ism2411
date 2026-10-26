# Reflection Q1: What is the most surprising thing about how lists work in Python compared to what you expected coming in?
#The Most surprising thing about how lists work in Python compared to what I expected coming in was how simple they are. I expected some complicated syntax to calculate things like sums and middles, but there is simple functions for that. 
# Reflection Q2: Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
# A real business situation where a Python list would have saved time is when analyzing sales data. Instead of manually sorting and filtering data in Excel, a Python list could be used to quickly identify high-performing products or regions, saving significant time and reducing errors.



# Exercise 1: build a list 

print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2: Index Practice
print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #Always grabs the first item
print(inventory[-1]) #Always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) #Always grabs the middle item

#Exercise 3: List Slicing
print("--- Exercise 3: List Slicing ---")
print(inventory[:3]) #Grabs the first three items
print(inventory[-2:]) #Grabs the last two items
print(inventory[::2]) #Grabs every other item

#Exercise 4: List Methods
print("--- Exercise 4: List Methods ---")
inventory.append("envelope") #Adds an item "envelope" to the end of the list
inventory.append("tape") #Adds an item "tape" to the end of the list
print(inventory)


inventory.remove("tape") #Removes the item "tape" from the list
print(inventory) #We notice that .remove() only removes the first instance of the item in the list, not both. Be careful of this.

inventory.sort() #Sorts the list in alphabetical order

#Exercise 5: Tuple Comparison
print("--- Exercise 5: Tuple Comparison ---")
coordinates = (40.7128, -74.0060) #Tuple of coordinates for New York City

try:
    coordinates[0] = 99 
except TypeError as e:
    print(f"TypeError caught: {e}")
    print("Tuples protect coordinates from being changed accidentally.")

#Exercise 6: Average List of Sales
print("--- Exercise 6: Average List of Sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

#Exercise 7: Accumulator Pattern
print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted_price = price * 0.9 # Apply a 10% discount
    discounted.append(round(discounted_price, 2))

print(prices)
print(discounted)

#Exercise 8: Filter above threshold
print("--- Exercise 8: Filter Above Threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
