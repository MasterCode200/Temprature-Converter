Celcius= float(input("Enter the temprature in celcius- ")) #The input is in a float
Far= Celcius*9/5+32 #this is the conversion of celcius into farheniet
print("The temprature in fahrenheit is - " + str(Far))
if (Far>=104):
    print("It is a hot day")
elif(Far<=50):
    print("It is a cold day")
else:
    print("The weather is nice")
