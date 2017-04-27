#!/usr/bin/env python
import urllib2

BASE_URL = 'http://virginia.edu/uvapolice/police_reports/'
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
years = ['99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']

for year in years:
    for month in months:
        filename = month + year + ".txt"
        url = BASE_URL + filename
        resp = urllib2.urlopen(url, filename)
        prefix = '20'
        if year == '99':
            prefix = '19'

        monthnum = months.index(month) + 1
        if monthnum < 10:
            monthnum = '0' + str(monthnum)

        monthnum = str(monthnum)

        newfilename = prefix+year+'-'+monthnum+'.txt' # 2000-01.txt.
        with open(newfilename, 'wb') as f:
            f.write(resp.read())
