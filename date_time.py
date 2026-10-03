import datetime as dt

now = dt.datetime.now()
# print(type(now))

# print(now.date())
# print(now.time())
# print(now.hour)
# print(now.month)

mytime = dt.datetime(2030,9,19,10,30)
# print(mytime)                
                     



""" 
Token	    Meaning	                            Example
%Y	        Year (4 digits)	                    2026
%y	        Year (2 digits)	                    26
%m	        Month (01–12)	                    09
%B	        Full month name	                    September
%b / %h        	Abbreviated month name	        Sep
%d	        Day of month (01–31)	            19
%A	        Full weekday name	                Saturday
%a	        Abbreviated weekday name	        Sat
%H	        Hour (00–23)	                    14
%I	        Hour (01–12)	                    02
%p	        AM/PM	                            PM
%M	        Minute (00–59)	                    45
%S	        Second (00–59)	                    07
%f	        Microsecond (000000–999999)	        123456
%z	        UTC offset	                        +0100
%Z	        Time zone name	                    UTC
%j	        Day of year (001–366)	            263
%U	        Week number (Sunday first day)	    37
%W	        Week number (Monday first day)	    37
%c	        Locale’s date and time	            Sat Sep 19 14:45:07 2026
%x	        Locale’s date	                    09/19/26
%X	        Locale’s time	                    14:45:07

"""

# 19 Sept, 2026
# 19/09/26
# 19-09-2026

# str_time = now.strftime("%d %b, %Y.")
# str_time = now.strftime("%d/%m/%y")
# str_time = now.strftime("%x")
# print(str_time)

# dob = input("DOB (YYYY/MM/DD): ")

# dt_dob = dt.datetime.strptime(dob, "%Y/%m/%d")

# print(now.year - dt_dob.year)


# print(now + dt.timedelta(weeks=52))

# ASS 
# Build a schedule/ alarm system