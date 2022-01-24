#HARJEET SINGH YADAV
#2020561 - CSAI 
# IIIT - DELHI


menu=[  ["Tshirt",      "Apparels",    500   ],
        ["Trausers",    "Apparels",    600   ],
        ["Scarf",       "Apparels",    250   ],
        ["Smartphone",  "Electronics", 20000 ],
        ["iPad",        "Electronics", 30000 ],
        ["Laptop",      "Electronics", 50000 ],
        ["Eggs",        "Eatables",    5     ],
        ["Chocolate",   "Eatables",    10    ],
        ["Juice",       "Eatables",    100   ],
        ["Milk",        "Eatables",    45    ]    ]


def show_menu():
    print('='*50,' '*21 + 'MY BAZAAR','='*50,'Hello! Welcome to my grocery store!','Following are the products available in the shop:',sep='\n')
    print('-'*50,'CODE | DESCRIPTION | CATEGORY | COST (Rs)','-'*50,sep=('\n'))
    for i in range(10):
        print(i,'|',menu[i][0],'|',menu[i][1],'|',menu[i][2])
    print('-'*50)
            



def get_regular_input():

    qr=[0,0,0,0,0,0,0,0,0,0]
    print('-'*50, ' '*10 +'ENTER ITEMS YOU WISH TO BUY','-'*50,'Enter the item codes (space-separated): ',sep='\n')
    e = list(map(int,input().split()))
    for i in e:
        if(0<= i <=9):
             qr[i]+=1
        else:
            print('invalid code:',i)
                
    return qr
    


def get_bulk_input():
    
    qb=[0,0,0,0,0,0,0,0,0,0]
    print('-'*50 ,' '*13 + "ENTER CODE AND QUANTITY",'-'*50,sep='\n')
    while True:
        print("Enter code and quantity (leave blank to stop): ",end='')
        s=input()
        if s=='':
            break
        else:
            s=s.split("  ")
            s=list(map(int,s))
            if (s[0]<0 or s[0]>9) and s[1]<0:
                print("Invalid code and quantity. Try again. ")
                continue
            elif s[1]<0:
                print("invalid quantity. try again")
                continue
            elif s[0]<0 or s[0]>9:
                print("invalid code. try again")
                continue


        qb[s[0]]+=s[1]
        print("You added",s[1],menu[s[0]][0])
        
    return qb

def print_order_details(quantities):

    c=1
    print('-'*50,' '*18 + 'ORDER DETAILS','-'*50,sep='\n')
    for i in range(10):
        if quantities[i]==0:
            continue
        else:
            print('[',c,']',menu[i][0],'x',quantities[i],'= Rs',menu[i][2],'*',quantities[i],'= Rs',menu[i][2]*quantities[i])
            c+=1
    


def calculate_category_wise_cost(quantities):
    a,e,ea=0,0,0
    for i in range(10):
        if 0<=i<=2:
            a=a+menu[i][2]*quantities[i]
        elif 3<=i<=5:
             e=e+menu[i][2]*quantities[i]
        elif 6<=i<=9:
             ea=ea+menu[i][2]*quantities[i]
    print('-'*50,' '*15 + 'CATOGARY WISE COST','-'*50,sep='\n')
    print('Apparels = Rs',a)
    print('Electronics = Rs',e)
    print('Eatables = Rs',ea)
                
    return (a,e,ea)
    


def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    
    x,y,z,ad,ed,ead=0,0,0,apparels_cost, electronics_cost, eatables_cost
    print("-"*50,' '*21+'DISCOUNTS','-'*50,sep='\n')
    
    if apparels_cost>=2000:
        x=get_discount(apparels_cost,0.1)
        ad=apparels_cost - x
        print('[APPARELS] Rs',apparels_cost,'- Rs',x,'= Rs',ad)
        
    if electronics_cost>=25000:
        y=get_discount(electronics_cost,0.1)
        ed=electronics_cost - y
        print('[ELECTRONICS] Rs',electronics_cost,'- Rs',y,'= Rs',ed)
        
    if eatables_cost>=500:
        z=get_discount(eatables_cost,0.1)
        ead=eatables_cost -z
        print('[EATABLES] Rs',eatables_cost,'- Rs',z,'= Rs',ead)
    print()    
    print("TOTAL DISCOUNT ",x+y+z)
    print("TOTAL COST ",ad+ed+ead)
    
    return (ad,ed,ead)


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):

    p,q,r,at,et,eat=0,0,0,apparels_cost, electronics_cost, eatables_cost
    print('-'*50,' '*24 + 'TAX','-'*50,sep='\n')
    
    p=get_tax(at,0.1)
    at=at+p
    print('[APPARELS] Rs',apparels_cost,'* 0.10 = Rs',p)
    
    q=get_tax(et,0.15)
    et=et+q
    print('[ELECTRONICS] Rs',electronics_cost,'* 0.15 = Rs',q)
    
    r=get_tax(eat,0.05)
    eat=eat+r
    print("[EATABLES] Rs",eatables_cost,'* 0.05 = Rs',r)
    
    print()
    print("TOTAL TAX = Rs ",p+q+r)
    print('TOTAL COST = Rs ',at+et+eat)
    
    return (at+et+eat,p+q+r)
    
    
    


def apply_coupon_code(total_cost):

    d1,d2=0,0
    print('-'*50,' '*20 + 'COUPON CODE','-'*50,sep='\n')
    while True:
        s=input('Enter coupon code ( else leave blank ): ')
        if s=='':
            break
        if s=='HELLE25':
            if total_cost>=25000:
                print('[HELLE25] min( 5000 , Rs',total_cost,'* 0.25 ) = Rs 5000')
                total_cost=total_cost-5000
                d1=5000
            else:
                print("your total cost is less than the minimum eligibility criteria")
            break
        if s=='CHILL50':
            if total_cost>=50000:
                print('[CHILL50] min( 10000, Rs',total_cost,'* 0.50 ) = Rs 10000')
                total_cost=total_cost-10000
                d2=10000
            else:
                print('your total cost is less than the minimum eligibility criteria')
            break
            
        print('Invalid coupon code. Try again.')
        print()
        continue
    print()
    print('TOTAL COUPON DISCOUNT = Rs ',d1+d2)
    print('TOTAL COST = Rs ',total_cost)
    
    return (total_cost,d1+d2)
                
            
        


def main():
    
    show_menu()
    quantities=[]
    while True:
        o=input('Would you like to buy in bulk (y or Y / n or N ):')
        if o=='y' or o=='Y':
            quantities=get_bulk_input()
            break
        if o=='n' or o=='N':
            quantities=get_regular_input()
            break
            
        print('invalid input. try again :')
        print()
        continue
    print_order_details(quantities)
    cwc=calculate_category_wise_cost(quantities)
    cwdc=calculate_discounted_prices(cwc[0],cwc[1],cwc[2])
    cat=calculate_tax(cwdc[0],cwdc[1],cwdc[2])
    total=apply_coupon_code(cat[0])
    print()
    print('Thank you for visiting')
    
    
    
    


if __name__ == '__main__':
	main()
