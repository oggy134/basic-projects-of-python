foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food or grocery you want(q for quit): ")
    if food.lower()=="q":
        break
    price=float(input(f"Enter the cost of {food} $"))
    foods.append(food)
    prices.append(price)
print("--- YOUR CART ---")
for food in foods:
    print(food,end=" ")
    
for price in prices:
    total=total+price
print() 
print(f"Your total is: ${total}")
    