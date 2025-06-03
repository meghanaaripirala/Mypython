y=int(input("enter the year ="))
if y%100==0:
    if y%400==0:
      print("it is a leap year")
    else :
       print("it is not leap year")
else :
   if y%4==0:
      print("it is leap year")
   else :
      print("it is not leap year")
      
