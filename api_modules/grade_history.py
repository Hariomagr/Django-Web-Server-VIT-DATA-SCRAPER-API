import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def grade_history(sem,s,error):
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
        url="https://vtopbeta.vit.ac.in/vtop/examinations/examGradeView/StudentGradeHistory"
        url=s.post(url,headers=headers,verify=False)
        soup=BeautifulSoup(url.content,'html.parser')
        table=soup.find_all('table')
        final={}
        grade1=[]
        final_grade={}
        final_grade['grades']=[]
        final_grade1={}
        final_grade1['total_grade']=[]
        if(len(table)>2):
            table=table[1]
            tr=table.find_all('tr')
            for i in range(2,len(tr),1):
                grade={}
                if(tr[i].has_attr('style')):
                    if(tr[i]['style']=='background: rgb(224, 234, 242);'):
                        td=tr[i].find_all('td')
                        grade['code']=td[1].text
                        grade['title']=td[2].text
                        grade['type']=td[3].text
                        grade['credit']=td[4].text
                        grade['grade']=td[5].text
                        grade['month']=td[6].text
                        grade['course']=td[9].text
                        grade1.append(grade)
            final['grades']=grade1
            table=soup.find_all('table')
            table=table[len(table)-1]
            tr=table.find_all('tr')
            if(len(tr)>1):
                tr=tr[1].find_all('td')
                total={}
                total['credit_registered']=tr[0].text
                total['credit_earned']=tr[1].text
                total['cgpa']=tr[2].text
                total1=[]
                total1.append(total)
                final['total_grade']=total1
        return (final)
        #final=json.dumps(final)
        #final=json.loads(final)
        #with open('grade_history.json','w') as outfile:
        #    json.dump(final,outfile)
    return (error)
