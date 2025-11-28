age = int (input("Enter your age : "))
ticket = bool(input("Enter 0 for True and 1 for False"))
permission = bool(ticket)
if age > 20 :
    print ("You can watch the movie")
    if age > 20 : 
        print("show me ur id ")
    if ticket == True:
        print(" you can go inside")
        
elif age <= 16 :
    print("you can watch the movie with parents")
    print(" and come outside")
else :
    print("not allowed")
