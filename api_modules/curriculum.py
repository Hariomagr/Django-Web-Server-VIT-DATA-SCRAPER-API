import re
import json
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
def curriculum(sem,s,error):
    if(error==""):
        credit={}
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
        url="https://vtopbeta.vit.ac.in/vtop/academics/common/Curriculum"
        data={'semesterSubId':sem}
        url=s.post(url,data=data,headers=headers,verify=False)
        soup=BeautifulSoup(url.content,'html.parser')
        table0=soup.find_all('table')[0]
        credit1=[]
        for i in range(2,6):
            tr=table0.find_all('tr')[i]
            td1=tr.find_all('td')[1].text.replace("\n","")
            td1=td1.replace("\t"," ")
            td1=re.sub(' +',' ',td1)
            td2=tr.find_all('td')[2].text
            credit[td1]=td2
            credit1.append(credit)
        curriculum={}
        curriculum['Credits']=credit1
        for i in range(1,5):
            table=soup.find_all('table')[i]
            tr=table.find_all('tr')
            seq=[]
            for j in range(1,len(tr)):
                course={}
                td1=tr[j].find_all('td')[1].text
                td2=tr[j].find_all('td')[2].text
                td8=tr[j].find_all('td')[8].text
                course['code']=td1
                course['title']=td2
                course['credit']=td8
                seq.append(course)
            if(i==1):
                curriculum['PC']=seq
            elif(i==2):
                curriculum['PE']=seq
            elif(i==3):
                curriculum['UC']=seq
            elif(i==4):
                curriculum['UE']=seq
        return (curriculum)
        #curriculum=json.dumps(curriculum)
        #curriculum=json.loads(curriculum)
        #with open('curriculum.json','w') as outfile:
        #    json.dump(curriculum,outfile)
    return (error)
