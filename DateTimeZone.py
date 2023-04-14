from datetime  import datetime
import pytz
import tzlocal

user_tzlocal_name= tzlocal.get_localzone_name()
my_time_zone= pytz.timezone(user_tzlocal_name)
timeInzone=datetime.now(my_time_zone)
dateInzone=datetime.now().date()
current_time=timeInzone.strftime("%H:%M:%S")
current_date=dateInzone.strftime("%d:%m:%y")
time={
    "local time zone" : user_tzlocal_name,
    "current time" :current_time,
    "current date" : current_date
}
print(time)
