#on-6-12-2020
import datetime

M_day = input(" Add the Day ")
M_month = input(" Add the month ")
M_year = input(" Add the Year ")


print(" Your birthday on " + str(M_day) + " - " +str(M_month) + " - " +str(M_year))


my_birthday = datetime.date(int(M_year) , int(M_day), int(M_month))
today = datetime.date.today()
daydif = (today-my_birthday)

print(" your age is "+str(int(daydif.days/365.25))+ " Year ")
