import datetime
now=datetime.datetime.now()
print(now.strftime(("%d/%m/%Y")))
print(now.strftime(("%d/%m/%y")))
print(now.strftime(("%d:%m:%Y")))

print(datetime.date.today().month)

# search more in google

x=datetime.datetime(2019,12,3)
y=datetime.datetime(2022,11,17)

dif=y-x
print(dif)
s=0
end=datetime.datetime.now()

difference=end-now

print(difference)