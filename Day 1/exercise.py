#declare three string variables
#print the variables in a single line

distance=5
speed=2.5
time=2

print(f"Distance is:{distance} km | speed is:{speed} km/h | time is:{time}h")


#second exercise
#Declare three strings,value of the string should be city names
#print the cities in a single line separated by commas

city_1="Ragama"
city_2="Gampaha"
city_3="Colombo"

print(city_1,city_2,city_3,sep=',') # using separator

print(city_1+','+city_2+','+city_3) # string concatination

print(f"{city_1},{city_2},{city_3}") # formating

#Declare string variable and an integer variable then concatinate

city_distance=20

message=("I am from"' ' + city_1 +' '"and distance to home around"' '+ str(city_distance)+"km")
#correct method
print(message)
print(city_1+','+str(city_distance))



