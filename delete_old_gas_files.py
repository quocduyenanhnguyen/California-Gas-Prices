from datetime import datetime, timedelta, date
# calculate and format a date that is 90 days prior to the current date
prev = date.strftime(datetime.today() - timedelta(days=90), '%Y-%m-%d')

with open('/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Regular_Gas.csv', 'r+') as dates:
    # build a list of dates that are greater than *prev*
    d = [s for s in dates if s.strip() > prev]
    dates.seek(0) # seek to start of file
    dates.write(''.join(d)) # write the list
    dates.truncate() # truncate

with open('/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Midgrade_Gas.csv', 'r+') as dates:
    # build a list of dates that are greater than *prev*
    d = [s for s in dates if s.strip() > prev]
    dates.seek(0) # seek to start of file
    dates.write(''.join(d)) # write the list
    dates.truncate() # truncate

with open('/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Premium_Gas.csv', 'r+') as dates:
    # build a list of dates that are greater than *prev*
    d = [s for s in dates if s.strip() > prev]
    dates.seek(0) # seek to start of file
    dates.write(''.join(d)) # write the list
    dates.truncate() # truncate

with open('/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Diesel_Fuel_Gas.csv', 'r+') as dates:
    # build a list of dates that are greater than *prev*
    d = [s for s in dates if s.strip() > prev]
    dates.seek(0) # seek to start of file
    dates.write(''.join(d)) # write the list
    dates.truncate() # truncate
