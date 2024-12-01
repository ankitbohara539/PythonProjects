# this is the program to build a shopping cart program

foods = []
prices = []
total = 0
while True:
    food = input("Enter the food item Q to quit: ")
    if food.lower()=="q":
        break
    else :
        price = int(input(f"Enter the price of a {food}:Rs. "))
        foods.append(food)
        prices.append(price) 
        
print(" -----Your Bill is Here--------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total +=price

print()
print(f"The totsl amount is: Rs. {total} only")




    