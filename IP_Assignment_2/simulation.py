# Name -Harjeet Singh Yadav 
# Roll No - 2020561

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program. 

import a2

def show_menu():
    print('-'*40,' '*17 + "MENU",'-'*40,sep='\n')
    print("1  | READ DATA FROM FILE  |","-"*40,sep='\n')
    print("2  | FILTER BY FIRST NAME |","-"*40,sep='\n')
    print("3  | FILTER BY LAST NAME  |","-"*40,sep='\n')
    print("4  | FILTER BY FULL NAME  |","-"*40,sep='\n')
    print("5  | FILTER BY AGE RANGE  |","-"*40,sep='\n')
    print("6  | COUNT BY GENDER      |","-"*40,sep='\n')
    print("7  | FILTER BY ADDRESS    |","-"*40,sep='\n')
    print("8  | FIND ALUMINI         |","-"*40,sep='\n')
    print("9  | FIND TOPPER OF EACH INSTITUTE |","-"*40,sep='\n')
    print("10 | FIND BLOOD DONORS    |","-"*40,sep='\n')
    print("11 | GET COMMON FRINENDS  |","-"*40,sep='\n')
    print("12 | IS RELETED           |","-"*40,sep='\n')
    print("13 | DELETE BY ID         |","-"*40,sep='\n')
    print("14 | ADD FRIEND           |","-"*40,sep='\n')
    print("15 | REMOVE FRIENDS       |","-"*40,sep='\n')
    print("16 | ADD EDUCATION        |","-"*40,sep='\n')
    

    
def main():
    
    show_menu()
    upd_rec = a2.read_data_from_file()
    
    while True:
        
        q=int(input("enter a number bwtween 1 and 16 or -1 to quit :"))
        if q==-1:
            print("Thank you !")
            break
            
        if q==2:
            f_name=input("Enter first name :")
            print(a2.filter_by_first_name(upd_rec, f_name))
            
        elif q==1:
            print(upd_rec)
            
        elif q==3:
            l_name=input("Enter last name :")
            print(a2.filter_by_last_name(upd_rec, l_name))
            
        elif q==4:
            full=input("Enter full name :")
            print(a2.filter_by_full_name(upd_rec, full))
            
        elif q==5:
            mini=int(input("Enter minimum age :")); maxi=int(input("Enter maximum age :"))
            print(a2.filter_by_age_range(upd_rec, mini, maxi))
            
        elif q==6:
            print(a2.count_by_gender(upd_rec)) 
            
        elif q==12:
            id_1=int(input("Enter id of person 1 :")); id_2=int(input("Enter id of person 2 :"))
            print(a2.is_related(upd_rec, id_1, id_2))
        
        elif q==8:
            institute=input("Enter name of institute :")
            print(a2.find_alumni(upd_rec, institute))
            
        elif q==9:
            print(a2.find_topper_of_each_institute(upd_rec))
            
        elif q==10:
            receiver=int(input("Enter receiver's id :"))
            print(a2.find_blood_donors(upd_rec, receiver))
            
        elif q==11:
            print("Enter the ids separated by a single space :")
            l=list(map(int,input().split()))
            print(a2.get_common_friends(upd_rec, l))
            
        elif q==7:
            add={} 
            house=input("enter house no or leave blank :")
            if house!='':
                add["house_no"]=int(house)
            block=input("Enter block no or leave blank")
            if block!='':
                add["block"]=block
            town=input("Enter town or leave blank :")
            if town!='':
                add["town"]=town
            city=input("Enter city or leave blank :")
            if city!='':
                add["city"]=city
            state=input("Enter the state or leave blank :")
            if state!='':
                add["state"]=state
            pin=input("Enter pincode or leave blank :")
            if pin!='':
                add["pincode"]=int(pin)
            print(a2.filter_by_address(upd_rec, add))
                
        elif q==13:
            did=int(input("Enter the id :"))
            upd_rec=a2.delete_by_id(upd_rec,did)
            
        elif q==14:
            p=int(input("Enter person id :")); f=int(input("Enter friends id :"));
            upd_rec=a2.add_friend(upd_rec, p, f)
            
        elif q==15:
            pi=int(input("Enter person id :")); fi=int(input("Enter friends id :"));
            upd_rec=a2.remove_friend(upd_rec, pi, fi)
            
        elif q==16:
            pid=int(input("Enter person id :")); insti=input("Enter institute name :");
            ong=input("Enter onging status :");  perc= float(input("Enter percentage :"));
            upd_rec=a2.add_education(upd_rec, pid, insti, ong, perc)
            
        else:
            print(" Invalid ! please enter a valid no :")
            
            
if __name__ == '__main__':
    main()            
            
            
            
                
                
                
            
            
                   
                   
            
            
                  