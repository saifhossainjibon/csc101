
# Problem Set:

# Write a program that will take the length and width of a rectangle from the user and prints the area and perimeter of the rectangle.
# Write a program that calculates the number of second, minutes and hours in 1 year. 
# Write a program that takes the number of hours as input and displays the equivalent number of weeks, days, and hours. For example, if the user inputs 4000 hours, the program displays 23 weeks, 5 days and 16 hours.
# Write a program that converts the number of days into month and years. For example, if the user inputs 813 days, the program prints: 2 years 2 months 23 days. (don’t worry about leap year and you can calculate using 1 month = 30 days)
# Write a program that prompts the user for the current year and user’s current age. It then calculates and prints the user’s birthday. 


#Problem 1
length=int(input("Give length of the rectangle: "))
width=int(input("Give width of the rectangle: "))

print("Area of the rectangle: ",length+width)
print("perimeter of the rectangle: ",2*(length+width))

#Problem 2
OneYear=365
Hour=24*OneYear
Minutes=60*Hour
Seconds=60*Minutes

print("Total days in one year: ",OneYear,"Days")
print("Total hour in one year: ",Hour,"hour")
print("Total mintues in one year: ",Minutes,"minutes")
print("Total seconds in one year: ",Seconds,"seconds")

# Problem 3
giveHours=int(input("Enter number of hours hours: "))

weeks=(giveHours//24)//7
days=(giveHours-weeks*24*7)//24
hours=(giveHours-weeks*24*7-days*24)
print(weeks,"Weeks",days,"Days",hours,"Hours")

# problem 4
number_of_days = int(input("Enter number of days: "))

years = number_of_days // 365
months = (number_of_days - years *365) // 30
days = (number_of_days - years * 365 - months*30)

print(years,"Years ", months,"Months ", days,"Days")

# problem 5
birthYear=int(input("Give your birth year: "))
birthMonth=int(input("Give your birth month: "))
birthDay=int(input("Give your birth day: "))
ageYear=(2021-birthYear)
ageMonth=(7-birthMonth)
ageDay=(10-birthDay)
print(ageYear,ageMonth,ageDay)