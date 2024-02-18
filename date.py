#ex1

# def days5(somedate):
#     number = int(somedate[0:2]) - 5
#     if (number > 0):
#         newdate = somedate.replace(somedate[0:2], str(number))
#         if (len(newdate) == 9):
#             newdate = "0" + newdate
#             print(newdate)
#         else:
#             print(newdate)

#     elif (number <= 0):
#         day = 30 + number
#         month = int(somedate[3:5]) - 1
#         newdate1 = str(day) + "." + str(month) + "." + somedate[6:]
        
#         if(month <= 0):
#             year = int(somedate[6:]) - 1
#             month = 12
#             otherdate = newdate1[0:2] + "." + str(month) + "." + str(year)
#             print(otherdate)

#         elif(month > 0):
#             if (len(newdate1) == 9):
#                 fixedmonth = "0" + str(month) 
#                 newdate = str(day) + "." + str(fixedmonth) + "." + somedate[6:]
#                 print(newdate)
#             elif (len(newdate1 == 10)):
#                 print(newdate)
            
# yourdate = input("Enter current date: ")
# days5(yourdate)





# from datetime import datetime, timedelta

# today = datetime.now()

# days5 = today -  timedelta(days = 5)

# print("Current date is: " + str(today.strftime("%d.%m.%Y")))
# print("The date 5 days ago: " + str(days5.strftime("%d.%m.%Y")))


#ex2
# from datetime import datetime, timedelta
# today = datetime.now()
# yesterday = today - timedelta(days = 1)
# tomorrow = today + timedelta(days = 1)

# print("Today is: " + str(today.strftime("%d.%m.%Y")))
# print("Yesterday was: " + str(yesterday.strftime("%d.%m.%Y")))
# print("Tomorrow will be: " + str(str(tomorrow.strftime("%d.%m.%Y"))))


#ex3
# from datetime import datetime, timedelta

# a = datetime.now()

# print(a.strftime("%f"))



#ex4
# from datetime import datetime, timedelta

# today = datetime.now()

# days2 = today - timedelta(days = 2)

# diff = today - days2

# print(diff.total_seconds())

