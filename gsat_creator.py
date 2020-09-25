import csv
import datetime

dates = []
oil = []
group_name = input("Please enter group name - limit to three characters.")

#  open csv file and read in rates and dates into list
with open("/Users/davidtaylor/Documents/python/gsat/rate_data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    # skip the headers
    next(reader)
    #  create lists for dates and rates
    for line in reader:
        dates.append(line[0])
        oil.append(line[1])

#  add in some check to make sure length of dates is the same as rates otherwise print out error

with open("/Users/davidtaylor/Documents/python/gsat/gsatprod.inc","w") as file:
    for num in range(0,len(dates)):
        date = datetime.datetime.strptime(dates[num],"%d/%m/%Y")
        file.write(f"""
        ACTIONX
        {group_name}{num+1} 30 1 /
        YEAR = {date.year} MNTH = {date.month} DAY = {date.day} /
        GSATPROD
        {group_name} {oil[num]} /
        /
        ENDACTIO\n""")