import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def attandence(sem,s,error):
    if(error==""):
        url="https://vtopbeta.vit.ac.in/vtop/processViewStudentAttendance"
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
        data={'semesterSubId':sem}
        url=s.post(url,data=data,headers=headers,verify=False)
        soup=BeautifulSoup(url.content,'html.parser')
        table=soup.find_all('table')[0]
        length=len(table.find_all('tr'))
        attendance1={}
        attendance=[]
        for i in range(1,length-1):
            course={}
            tr=table.find_all('tr')[i]
            td=tr.find_all('td')
            course['code']=td[1].find_all('p')[0].text
            course['title']=td[2].find_all('p')[0].text
            course['type']=td[3].text
            course['slot']=td[4].text
            course['faculty']=td[5].find_all('p')[1].text
            course['attended']=td[7].find_all('p')[0].text
            course['total']=td[8].find_all('p')[0].text
            course['percentage']=td[9].find_all('p')[0].text
            classs=td[11].find_all('a')[0]['onclick'].split("'")[1]
            slot=td[11].find_all('a')[0]['onclick'].split("'")[3]
            url="https://vtopbeta.vit.ac.in/vtop/processViewAttendanceDetail"
            data={'classId':classs,'slotName':slot}
            url=s.post(url,data=data,headers=headers,verify=False)
            soup1=BeautifulSoup(url.content,'html.parser')
            table1=soup1.find_all('table')[0]
            length1=len(table1.find_all('tr'))
            detail1=[]
            detail={}
            for j in range(1,length1):
                tr1=table1.find_all('tr')[j]
                td1=tr1.find_all('td')
                detail['date']=td1[1].text
                detail['slot']=td1[2].find_all('p')[0].text
                detail['status']=td1[4].find_all('span')[0].text
                detail1.append(detail)
            course['details']=detail1
            attendance.append(course)
        attendance1['Attendance']=attendance
        #attendance1=json.dumps(attendance1)
        #attendance1=json.loads(attendance1)
        return (attendance1)
        #with open('attendance.json','w') as outfile:
        #    json.dump(attendance1,outfile)
    return (error)
