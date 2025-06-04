p=0
r=0
t=0

while p<=0:
    p=float(input("Enter your Principle amount: "))
    if p<=0:
        print("Principle amount must be more than 0")
        
while r<=0:
    r=float(input("Enter your rate of intrest: "))
    if r<=0:
        print("Intrest  must be more than 0")
        
while t<=0:
    t=int(input("Enter your time : "))
    if t<=0:
        print(" time must be more than a year ")
        
        
total_amount=p*pow((1+r/100),t,)
print(f"The total amount after {t} year is {total_amount:.2f} ")