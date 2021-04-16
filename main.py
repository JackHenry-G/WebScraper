from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd

from time import sleep # to delay requests to not flood server
from random import randint # vary the time between requests

source = requests.get('https://www.findapprenticeship.service.gov.uk/apprenticeships?ApprenticeshipLevel=Degree&Hash=1515650079&Latitude=51.356874&Longitude=0.524629&Location=ME5%200JE&LocationType=NonNational&PageNumber=1&ResultsPerPage=5&SearchAction=Search&SearchField=All&SearchMode=Keyword&SortType=Relevancy&WithinDistance=0&DisabilityConfidentOnly=False').text
soup = BeautifulSoup(source, 'lxml')

jobs = {
    'Job Name': [],
    'Link' : [],
    'Start date' : []
}

jobNameList=[]
linkList=[]
startDateList=[]

list_dates = []
start_dates = soup.find_all('span', id="start-date-value")
for item in start_dates:
    item = item.text
    item = str(item)

    datetime_object = datetime.strptime(item, '%d %b %Y')
    list_dates.append(datetime_object)
    startDateList.append(datetime_object)

for job in soup.find_all('a', class_='vacancy-link'):
    job_name = job.text
    jobNameList.append(job_name)

for a in soup.find_all('a', class_='vacancy-link', href=True):
    job_reference = a['href']
    job_link = f'https://www.findapprenticeship.service.gov.uk/{job_reference}'
    linkList.append(job_link)


for x in range(2, 30):
    source2=requests.get(f'https://www.findapprenticeship.service.gov.uk/apprenticeships?ApprenticeshipLevel=Degree&Hash=1515650079&Latitude=51.356874&Longitude=0.524629&Location=ME5%200JE&LocationType=NonNational&PageNumber={x}&ResultsPerPage=5&SearchAction=Sort&SearchField=All&SearchMode=Keyword&SortType=Distance&WithinDistance=0&DisabilityConfidentOnly=False').text
    soup=BeautifulSoup(source2, 'lxml')

    list_dates = []
    start_dates = soup.find_all('span', id="start-date-value")
    for item in start_dates:
        item = item.text
        item = str(item)



        datetime_object = datetime.strptime(item, '%d %b %Y')
        list_dates.append(datetime_object)
        startDateList.append(datetime_object)


    for job in soup.find_all('a', class_='vacancy-link'):
        job_name = job.text
        jobNameList.append(job_name)

    #for identifier in soup.find_all('a', class_='vacancy-link')['href']:
    #for identifier in soup.find_all('a', class_='vacancy-link'):
        #print(identifier)
    for a in soup.find_all('a', class_='vacancy-link', href=True):
        job_reference = a['href']
        job_link = f'https://www.findapprenticeship.service.gov.uk/{job_reference}'
        linkList.append(job_link)


#print(jobNameList)
#print(linkList)
#print(startDateList)

jobs['Job Name']=jobNameList
jobs['Link']=linkList
jobs['Start date']=startDateList

#list_dates.sort()
#print(list_dates)
print(jobNameList)
print(linkList)
print(startDateList)

df = pd.DataFrame(jobs)
#print(df)

#df['Start date']=pd.to_datetime(df['Start date'])
#pd.set_option('display.max_columns', None)
#print(df.sort_values(by='Start date'))
#print(type(df.loc[0]))

job_details = []
for x in range(0, 5):
    job_array = df.loc[x].array
    job_role = job
    job_name = job_array[0]
    job_link = job_array[1]
    job_start_date = job_array[2]
    job_details.append([job_name, job_link, job_start_date])

#pd2 = df.loc[df['Start date'] < "2021-06-23"]
#print(type(pd2))



# 1. Do this for all pages - Y
# 2. Display in easier to read fashion - N
# 3. GUI it
# GITHUB
