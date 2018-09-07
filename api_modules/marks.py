import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def marks(sem,s,error):
    if(error==""):
        url="https://vtopbeta.vit.ac.in/vtop/examinations/doStudentMarkView"
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
        final_mark=[]
        final_mark1={}
        if(len(table)>0):
            tr=table[0].find_all('tr')
            for i in range(1,len(tr)):
                if(tr[i-1].has_attr('style')):
                    if(tr[i-1]['style']=='background-color: #d2edf7;'):
                        course_info=tr[i-1].find_all('td')
                        marks={}
                        marks['class_no']=course_info[1].text
                        marks['code']=course_info[2].text
                        marks['title']=course_info[3].text
                        marks['type']=course_info[4].text
                        marks['credit']=course_info[5].text
                        marks['faculty']=course_info[7].text
                        marks['slot']=course_info[8].text
                        mark_info=tr[i].find_all('td')[0].find_all('table')[0]
                        mark_tr=mark_info.find_all('tr')
                        store_mark=[]
                        for j in range(1,len(mark_tr)):
                            td1=mark_tr[j].find_all('td')
                            mark_sub={}
                            mark_sub['title']=td1[1].find_all('output')[0].text
                            mark_sub['max']=td1[2].find_all('output')[0].text
                            mark_sub['weightage']=td1[3].find_all('output')[0].text
                            mark_sub['status']=td1[4].find_all('output')[0].text
                            mark_sub['scored']=td1[5].find_all('output')[0].text
                            mark_sub['percentage']=td1[6].find_all('output')[0].text
                            store_mark.append(mark_sub)
                        marks['details']=store_mark
                        final_mark.append(marks)
            final_mark1['marks']=final_mark
            #final_mark1=json.dumps(final_mark1)
            #final_mark1=json.loads(final_mark1)
        return (final_mark1)
    return  (error)
        #with open('marks.json','w') as outfile:
        #    json.dump(final_mark1,outfile)
