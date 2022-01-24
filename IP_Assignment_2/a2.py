# Assignment - 2
# Name - Harjeet Singh Yadav
# Roll No - 2020561

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):

    idf=[]
    f=first_name.lower()
    for i in records:
        if i['first_name'].lower()==f:
            idf.append(i['id'])
            
    return list(set(idf))


def filter_by_last_name(records, last_name):
    
    idl=[]
    l=last_name.lower()
    for i in records:
        if i['last_name'].lower()==l:
            idl.append(i['id'])
            
    return list(set(idl))


def filter_by_full_name(records, full_name):
    
    idfn=[]
    fn=full_name.lower()
    for i in records:
        if (i['first_name'].lower()+' '+i['last_name'].lower())==fn:
            idfn.append(i['id'])
            
    return list(set(idfn))


def filter_by_age_range(records, min_age, max_age):

    ida=[]
    for i in records:
        if min_age<= i['age']<=max_age:
            ida.append(i['id'])
            
    return list(set(ida))

def count_by_gender(records):


    idg={'male':0 , 'female':0}
    for i in records:
        if i['gender']=='male':
            idg['male']+=1
        if i['gender']=='female':
            idg['female']+=1
    return idg
            
    


def filter_by_address(records, address):

    ida=[]
    new={}
    
    a=address.items()
    for k,v in a:
        if isinstance(v,str):
            v=v.lower()
        new[k.lower()]=v;
            
        
    for i in records:
        dic={}
        p=i["address"].items()
        for k,v in p:
            if isinstance(v,str):
                v=v.lower()
            dic[k.lower()]=v;
            
        if new.items()<=dic.items():
            ida.append({"first_name":i["first_name"],"last_name":i["last_name"]})
    
    temp=[]
    for i in ida:
        if i not in temp:
            temp.append(i)
            
    return temp


def find_alumni(records, institute_name):

    ida=[]
    sch=institute_name.lower()
    for i in records:
        e=i["education"]
        for j in e:
            if j["ongoing"]==False and j["institute"].lower()==sch:
                if len(ida)>0 and ida[-1]["first_name"]==i["first_name"] and ida[-1]["last_name"]==i["last_name"]:
                    ida.pop()
                ida.append({"first_name":i["first_name"], "last_name":i["last_name"],"percentage":float(j["percentage"]) })
                
    temp=[]
    for i in ida:
        if i not in temp:
            temp.append(i)
            
    return temp


def find_topper_of_each_institute(records):

    ins=[]
    top={}
    
    for i in records:
        for j in i["education"]:
            if j["institute"] not in ins:
                ins.append(j["institute"])
    
    for i in ins:
        dic={}
        for r in records:
            for e in r["education"]:
                if e["institute"]==i:
                    
                    dic[r["id"]]=e.get("percentage",0)
            
        
        top[i]=max(dic,key=dic.get)
        
    return top
                    
    
        


def find_blood_donors(records, receiver_person_id):
    
    bd={}
    bg=''
    rid=receiver_person_id
    for i in records:
        if rid==i["id"]:
            bg=i["blood_group"]
            break
            
    acd=["A","AB","a","ab","aB","Ab"]
    bcd=["B","AB","b","ab","Ab","aB"]
    abcd=["AB","ab","aB","Ab"]
    ocd=["A","B","AB","O","o","a","b","ab","aB","Ab"]
    
    for i in records:
        if i["id"]==rid:
            continue
        d=i["blood_group"]
        if( d=="A" or d=="a" ) and ( bg in acd ):
            bd[i["id"]]=i["contacts"]
        elif (d=="B" or d=="b") and (bg in bcd):
            bd[i["id"]]=i["contacts"]
        elif (d in abcd) and (bg in abcd):
            bd[i["id"]]=i["contacts"]
        elif (d=="o" or d=="O") and (bg in ocd):
            bd[i["id"]]=i["contacts"]
            
    return bd


def get_common_friends(records, list_of_ids):

    l=list_of_ids
    temp=[]
    cf=[]
    for i in records:
        if i["id"] in l:
            temp.append(i["friend_ids"])
    
    if len(temp)==0:
        return temp
    if len(temp)==1:
        return temp[0]
    
   
    for i in temp[0]:
        flag=True
        for j in temp[1:]:
            if i not in j:
                flag =False
                break
                
        if flag:
            cf.append(i)
         
        
    return cf    
            


def is_related(records, person_id_1, person_id_2):

    fl={}
    for i in records:
        fl[i["id"]]=i["friend_ids"]
    
    p=person_id_1
    f=person_id_2
    
    if p not in fl.keys() or f not in fl.keys():
        return False
 
    
    l=fl[p][:]
    c=0
    for i in l:
        
        if f in l:
            return True
        a=len(l)
        l1=[]
        for j in l[c:]:
            l1.extend(fl[j])
            
        l.extend(l1)   
        l = list(dict.fromkeys(l))       
        b=len(l)
        c=a
        if a==b:
            return False
        
        
        
    
    


def delete_by_id(records, person_id):

    
    pid=person_id
    r=[i for i in records if i["id"]!=pid]
    
    for i in r:
        if pid in i["friend_ids"]:
            i["friend_ids"]=[j for j in i["friend_ids"] if j!=pid]
            
    
    return r
            
            


def add_friend(records, person_id, friend_id):

    pid=person_id
    fid=friend_id
    l=[]
    for i in records:
        l.append(i["id"])
    
    if (pid not in l) or (fid not in l):
        return records
    
    for i in records:
        if i["id"]==pid:
            if fid not in i["friend_ids"]:
                i["friend_ids"].append(fid)
        elif i["id"]==fid:
            if pid not in i["friend_ids"]:
                i["friend_ids"].append(pid)
            
    return records
            


def remove_friend(records, person_id, friend_id):

    pid=person_id
    fid=friend_id
    l=[]
    for i in records:
        l.append(i["id"])
    
    if (pid not in l) or (fid not in l):
        return records
    
    for i in records:
        if i["id"]==pid:
            if fid in i["friend_ids"]:
                i["friend_ids"]=[j for j in i["friend_ids"] if j!=fid]
        elif i["id"]==fid:
            if pid in i["friend_ids"]:
                i["friend_ids"]=[j for j in i["friend_ids"] if j!=pid]
            
    return records


def add_education(records, person_id, institute_name, ongoing, percentage):

    ins=''
    l=institute_name.split()
    if len(l)==1:
        ins=l[0].upper()
    if len(l)>=2:
        for i in range(len(l)):
            if i==0:
                ins=l[0].upper()
            else:
                ins=ins +' '+ l[i].capitalize()
            
       
    
    for i in records:
        if i["id"]==person_id:
            if ongoing:
                i["education"].append({"institute":ins, "ongoing":True})
            if ongoing==False:
                i["education"].append({"institute":ins, "ongoing":False, "percentage":float(percentage) })
                
    return records
                
