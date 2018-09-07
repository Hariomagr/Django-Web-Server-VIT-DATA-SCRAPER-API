import re
import json
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def timetable(sem,s,error):
    if(error==""):
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        }
        if(sem=="FS19"):
            sem="VL2018191"
        elif(sem=="TS19"):
            sem="VL2018192"
        elif(sem=="WS18"):
            sem="VL2017185"
        elif(sem=="FS18"):
            sem="VL2017181"
        url="https://vtopbeta.vit.ac.in/vtop/processViewTimeTable"
        data={'semesterSubId':sem}
        url=s.post(url,data=data,headers=headers,verify=False)
        soup=BeautifulSoup(url.content,'html.parser')
        table=soup.find_all('table')[0]
        length=len(table.find_all('tr'))
        timetable1={}
        timetable=[]
        for i in range(2,length-2):
            course={}
            tr=table.find_all('tr')[i]
            td=tr.find_all('td')
            course['code']=td[2].find_all('p')[0].text
            course['title']=td[3].find_all('p')[0].text
            course['type']=td[4].find_all('p')[0].text
            course['credit']=td[5].find_all('p')[0].text
            course['class_no']=td[7].find_all('p')[0].text
            course['slot']=td[8].find_all('p')[0].text
            course['venue']=td[9].find_all('p')[0].text
            course['faculty']=td[10].find_all('p')[0].text
            timetable.append(course)
        timetable1['Timetable']=timetable
        #timetable1=json.dumps(timetable1)
        #timetable1=json.loads(timetable1)
        return(timetable1)
    return (error)
        #with open('timetable.json','w') as outfile:
        #    json.dump(timetable1,outfile)
