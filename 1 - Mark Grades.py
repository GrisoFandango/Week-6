#Ask the user to put the mark value
mark=int(input("Please put your mark:"))

#We verify if the input from the user is enough
#to pass the course
if mark >= 40:
    print("Congratulations!!! YOU PASS!")
else:
    print("Sorry! You do not pass")
