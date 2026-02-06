#when user inputs no of minutes,we should output the
#no of hours and remaining minutes

minutes=int(input("please input no of minutes:"))
hours=minutes//60
extra_minutes=minutes%60


print('Hours :',hours)
print('Extra minutes :',extra_minutes)
