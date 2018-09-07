import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def exam(sem,s,error):
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
        url="https://vtopbeta.vit.ac.in/vtop/examinations/doSearchExamScheduleForStudent"
        data={'semesterSubId':sem}
        url=s.post(url,data=data,headers=headers,verify=False)
        soup=BeautifulSoup(url.content,'html.parser')
        table=soup.find_all('table')
        exam1={}
        final_exam={}
        final_exam['FAT']=[]
        final_exam['CAT1']=[]
        final_exam['CAT2']=[]
        if(len(table)!=0):
            table=table[0]
            tr=table.find_all('tr')
            exam_arr=[]
            exam_name=""
            chk=0
            for i in range(1,len(tr)):
                tr1=tr[i]
                exam={}
                if(tr1['class'][0]=='warning'):
                    if(chk==1):
                        final_exam[exam_name]=exam_arr
                    chk=1
                    exam_name=tr1.find_all('td')[0].text
                    exam_arr=[]
                else:
                    td=tr1.find_all('td')
                    exam['code']=td[1].text
                    exam['tite']=td[2].text
                    exam['type']=td[3].text
                    exam['class_no']=td[4].text
                    exam['slot']=td[5].text
                    exam['date']=td[6].text
                    exam['time']=td[8].text
                    exam['venue']=td[9].find_all('span')[0].text
                    exam['seat']=td[11].text
                    exam_arr.append(exam)
            final_exam[exam_name]=exam_arr
        exam1['schedule']=final_exam
        return (exam1)
        #exam1=json.dumps(exam1)
        #exam1=json.loads(exam1)
        #with open('exam_schedule.json','w') as outfile:
        #    json.dump(exam1,outfile)
    return (error)
