import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def assignments(sem,s,error):
    if(error==""):
        url="https://vtopbeta.vit.ac.in/vtop/examinations/doDigitalAssignment"
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
        tr=table.find_all('tr')
        length=len(tr)
        assignment1=[]
        final_assignment={}
        if(length>1):
            for i in range(1,length):
                assignment={}
                tr1=tr[i]
                td=tr1.find_all('td')
                assignment['class_no']=td[1].text
                assignment['code']=td[2].find_all('p')[0].text
                assignment['title']=td[3].find_all('p')[0].text
                assignment['type']=td[4].text
                assignment['slot']=td[11].text
                assignment['faculty']=td[12].find_all('p')[0].text
                assignment['option']=td[10].text
                data={'classId':td[1].text,'courseCode':td[2].find_all('p')[0].text,'title':td[3].find_all('p')[0].text,'type':td[4].text,'option':td[10].text,'slot':td[11].text,'fName':td[12].find_all('p')[0].text}
                url="https://vtopbeta.vit.ac.in/vtop/examinations/processDigitalAssignment"
                url=s.post(url,data=data,headers=headers,verify=False)
                soup1=BeautifulSoup(url.content,'html.parser')
                table1=soup1.find_all('table')[1]
                tr2=table1.find_all('tr')
                length1=len(tr2)
                details=[]
                if(length1>1):
                    for j in range(1,length1):
                        assignment_detail={}
                        tr3=tr2[j]
                        td1=tr3.find_all('td')
                        assignment_detail['title']=td1[1].text
                        assignment_detail['max']=td1[2].text
                        assignment_detail['weightage']=td1[3].text
                        assignment_detail['due_date']=td1[4].find_all('span')[0].text
                        chk_not_upload=td1[5].find_all('h5')
                        if(len(chk_not_upload)!=0):
                            assignment_detail['status']=chk_not_upload[0].text
                        chk_blank=td1[5].find_all('span')
                        if(len(chk_not_upload)==0 and len(chk_blank)==0):
                            assignment_detail['status']=""
                        if(len(chk_blank)>1):
                            span=chk_blank[1].find_all('span')
                            if(len(span)>1):
                                assignment_detail['status']=span[0].text+" "+span[1].text
                            else:
                                assignment_detail['status']=""
                        details.append(assignment_detail)
                assignment['details']=details
                assignment1.append(assignment)
            final_assignment['assignment']=assignment1
            #final_assignment=json.dumps(final_assignment)
            #final_assignment=json.loads(final_assignment)
        #with open('assignments.json','w') as outfile:
            #json.dump(final_assignment,outfile)
        return (final_assignment)
    return (error)
