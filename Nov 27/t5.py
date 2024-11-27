import datetime as dt

# now date and time 

x  = dt.datetime.now()

print("today's date and time : ",x)

# if we use specifiers for date and time module then user 
# have a function whihch is called 
# strftime strf time is a function whihch is 
# use for print date time according to users format 

a  = x.strftime("date : %d / %m / %Y \n day : %A \n time: %H: %M: %S")

print(a)
