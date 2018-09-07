import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def grade_semwise(sem,s,error):
    if(error==""):
        url="https://vtopbeta.vit.ac.in/vtop/examinations/examGradeView/doStudentGradeView"
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
        table=soup.find_all('table')
        grade1={}
        final_grade=[]
        grade1['grades']=[]
        if(len(table)>0):
            table=table[0]
            tr=table.find_all('tr')
            for i in range(2,len(tr)-1):
                td=tr[i].find_all('td')
                grade={}
                grade['title']=td[2].text
                grade['code']=td[1].text
                grade['type']=td[3].text
                grade['credit']=td[4].text+" "+td[5].text+" "+td[6].text+" "+td[7].text
                grade['grade']=td[12].text
                final_grade.append(grade)
            grade1['grades']=final_grade
        return (grade1)
    return (error)
        #    grade1=json.dumps(grade1)
        #    grade1=json.loads(grade1)
        #with open('grade_semwise.json','w') as outfile:
        #    json.dump(grade1,outfile)
