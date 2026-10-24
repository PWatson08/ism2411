# In Exercise 5, the first bug that I spotted was the missing colon on the for loop. I found it from explaining the code out loud to a duck, which is when I caught small, but devious mistake.
# Apply_discount(price, tier) function takes a tier and gives its price after applying that tier's discount.
# Disclosure, AI used on assignment. I used AI to help me troubleshoot issues with my own file. when I use AI to fix things, rather than just copying it down, I ask it why that is, and go back and forth until it makes sense to me.

#Exercise 1 

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    if tier == "silver":
        return price * 0.90
    if tier == "bronze":
        return price * 0.95
    else:
        return price


original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


#Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold')= ${final_price(200, 0.07, 'gold'):.2f}")

#Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

rate =0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 5


# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales: #Added a colon that was missing on the loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # to fix the issue listed below, removed the equals sign. Because the index cannot reach 5(the length of sales)
    print(sales[i])
    i += 1
#Error Message is "IndexError: list index out of range"; AI says that it can be from a loop that is running to far, trying to reach a value that does not exist.
#Ais explanation did match the actual bug


#Exercise 6

x = 100 #global x 

def double_it():
    x = 999 # local x 
    return x * 2

print(x)
print(double_it())
print(x)
#The reason why when you print x before and after printing double it and it stays the same is because
#the local variable x in the function double_it() does not affect the global variable x. or in other words
#What happens inside of the function double it, stays inside of it. 