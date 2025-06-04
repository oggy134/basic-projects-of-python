
user=int(input("Enter 1 to if you temprature is in Celcius \n Enter 2 to if you temprature is in Fahrehnit \n : "))
temp=float(input("Enter the Temperature: "))
if user== 1 :
    temp=round(temp*9/5+32)
    print(f"The temp in Fahrehnit is {temp} degree")
    
elif user==2 :
    temp=round(temp-32*5/9)
    print(f"The temp in Celcius is {temp} degree")

else:
    print(f"{user} is an invalid unit try again")
    
