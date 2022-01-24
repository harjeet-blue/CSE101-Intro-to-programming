#HARJEET SINGH YADAV
#2020561 - CSAI 
# IIIT - DELHI

import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        Shape.__init__(self)
        self.A=A.transpose()
        self.B=A.transpose()
 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        a=self.A.transpose()
        self.B=a.transpose()
        
        Shape.translate(self,dx,dy)
        self.A=self.T_t@self.A
        
        lx=self.A[0].tolist()
        ly=self.A[1].tolist()
        for i in range(len(lx)):
            lx[i]=round(lx[i],2)
            ly[i]=round(ly[i],2)
        
        return lx , ly
        

    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        a=self.A.transpose()
        self.B=a.transpose()
        
        Shape.scale(self,sx,sy)
        n=len(self.A[0])
        h=np.sum(self.A[0])/n
        k=np.sum(self.A[1])/n
        
        Shape.translate(self,h,k)
        a=self.T_t
        Shape.translate(self,-h,-k)
        b=self.T_t
        
        self.A= a@self.T_s@b@self.A
        
        lx=self.A[0].tolist()
        ly=self.A[1].tolist()
        for i in range(len(lx)):
            lx[i]=round(lx[i],2)
            ly[i]=round(ly[i],2)
        
        return lx , ly
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        a=self.A.transpose()
        self.B=a.transpose()
        
        Shape.rotate(self,deg)
        Shape.translate(self,rx,ry)
        a=self.T_t
        Shape.translate(self,-rx,-ry)
        b=self.T_t
        self.A=a@self.T_r@b@self.A
        
        lx=self.A[0].tolist()
        ly=self.A[1].tolist()
        for i in range(len(lx)):
            lx[i]=round(lx[i],2)
            ly[i]=round(ly[i],2)
        
        return lx , ly
        

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        x1=max(np.max(self.B[0]), abs(np.min(self.B[0])))
        y1=max(np.max(self.B[1]), abs(np.min(self.B[1])))
        x2=max(np.max(self.A[0]), abs(np.min(self.A[0])))
        y2=max(np.max(self.A[1]), abs(np.min(self.A[1])))
        
        plt.plot( np.append(self.B[0],self.B[0][0]) , np.append(self.B[1],self.B[1][0]) , linestyle='dashed' )
        plt.plot( np.append(self.A[0],self.A[0][0]) , np.append(self.A[1],self.A[1][0]) )
        
        Shape.plot(self,max(x1,x2)+1 , max(y1,y2)+1)
        
        

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        
        Shape.__init__(self)
        self.r=radius
        self.A=np.array([[x],[y],[1]])
        self.B=np.array([[x],[y],[1]])
        self.rp=radius


    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        a=self.A.transpose()
        self.B=a.transpose()
        self.rp=self.r
        
        Shape.translate(self,dx,dy)
        self.A=self.T_t@self.A
        
        x= round(self.A[0][0],2)
        y= round(self.A[1][0],2)
        rd=round(self.r,2)
        
        return x,y,rd
        
        
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        a=self.A.transpose()
        self.B=a.transpose()
        self.rp=self.r
        self.r=self.r*sx
        
        x= round(self.A[0][0],2)
        y= round(self.A[1][0],2)
        rd=round(self.r,2)
        
        return x,y,rd
        
        
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        a=self.A.transpose()
        self.B=a.transpose()
        self.rp=self.r
        
        Shape.rotate(self,deg)
        Shape.translate(self,rx,ry)
        a=self.T_t
        Shape.translate(self,-rx,-ry)
        b=self.T_t
        self.A=a@self.T_r@b@self.A
        
        x= round(self.A[0][0],2)
        y= round(self.A[1][0],2)
        rd=round(self.r,2)
        
        return x,y,rd
 
    
    def plot(self):
        circle1=plt.Circle((self.B[0][0],self.B[1][0]),self.rp,color='g',fill=False,linestyle='dashed')
        fig,ax=plt.subplots()
        ax.add_patch(circle1)
        
        circle2=plt.Circle((self.A[0][0],self.A[1][0]),self.r,color='g',fill=False)
        
        ax.add_patch(circle2)
        ax.set_aspect(1)
        
        x=max(abs(self.B[0][0]),abs(self.A[0][0]))
        y=max(abs(self.B[1][0]),abs(self.A[1][0]))
        rad=max(abs(self.rp),abs(self.r))
        
        Shape.plot(self,x+rad,y+rad)

if __name__ == "__main__":
   
    
   
  
        v=int(input("Enter verbose 0 or 1 :"))
 
        
        t=int(input("Enter no of test cases :"))
        
        for i in range(t):
            s=input("Enter the type of shape 0 for polygon & 1 for circle :")
            
            if s=='0':
                x=[]                                  #list for  x coordinates 
                y=[]                                  #list for  y coordinates
                z=[]
                sides=int(input("Enter no of sides of the polygon > 2  :"))
                for j in range(sides):
                    dim=input(f" enter space separated coordinates ( x{j+1} , y{j+1} )")
                    dim=dim.split()
                    x.append(float(dim[0]))
                    y.append(float(dim[1]))
                    z.append(1)
                
                A=np.array([x,y,z])                 # A has intial coordinates 
                A=A.transpose()
                p1=Polygon(A)                       #creating a object of polygon class
                A=A.transpose()
                
                q=int(input("Enter no of queries :"))
                
                for k in range(q):
                    qry1=input("\n Enter query with space separated input : ")
                    qry=qry1.split()
                    
                    if qry[0]=='T':                          #handling diff queries 
                        if len(qry)==2:
                            qry.append(qry[1])
                        
                        dx=float(qry[1])
                        dy=float(qry[2])
                        
                        new_c= p1.translate(dx,dy)          # new-c is a tuple of ([x],[y]) return by function
                        
                        for i in A[0]:print(round(i,2),end=' ')      # printing intitial coordinates
                        for i in A[1]:print(round(i,2),end=' ')
                        print()
                        for i in new_c[0]:print(i,end=' ')  # printing new coordinates after this query
                        for i in new_c[1]:print(i,end=' ')
                           
                        A=p1.A                              # assigning new coordinates to variable A
                        if v==1:
                            p1.plot()
                        
                    elif qry[0]=='S':
                        if len(qry)==2:
                            qry.append(qry[1])
                            
                        sx=float(qry[1])                       #converting to floats
                        sy=float(qry[2])
                        
                        new_c= p1.scale(sx,sy)                        # new-c is a tuple of ([x],[y]) return by function
                        
                        for i in A[0]:print(round(i,2),end=' ')       # printing intitial coordinates
                        for i in A[1]:print(round(i,2),end=' ')
                        print()
                        for i in new_c[0]:print(round(i,2),end=' ')    # printing new coordinates after this query
                        for i in new_c[1]:print(round(i,2),end=' ')
                        
                        A=p1.A                                         # assigning new coordinates to variable A
                        if v==1:
                            p1.plot()
                            
                    elif qry[0]=='R':
                        if len(qry)==2:
                            qry.extend(['0','0'])            # appending 0 0 at the end if rotation point is not given
                        elif len(qry)==3:
                            qry.append(ary[2])
                            
                        do=float(qry[1])
                        rx=float(qry[2])
                        ry=float(qry[3])
                        
                        new_c = p1.rotate(do,rx,ry)               # new-c is a tuple of ([x],[y]) return by function
                            
                        for i in A[0]:print(round(i,2),end=' ')      # printing intitial coordinates
                        for i in A[1]:print(round(i,2),end=' ')
                        print()
                        for i in new_c[0]:print(i,end=' ')       # printing new coordinates after this query
                        for i in new_c[1]:print(i,end=' ')
                            
                        A=p1.A
                        if v==1:
                            p1.plot()
                            
                    elif qry[0]=='P':                       #ploting of circle
                        p1.plot()
                        
                           
            elif s=='1':
                centre=input(" Enter specifications space separated :")
                centre=centre.split()
                
                a=float(centre[0])
                b=float(centre[1])
                r=float(centre[2])
                
                c1=Circle(a,b,r)                             #creating object of circle class
                
                q=int(input("Enter no of queries :"))
                
                for k in range(q):
                    qry1=input("\n Enter query with space separated input : ")
                    qry=qry1.split()
                    
                    if qry[0]=='T':
                        if len(qry)==2:
                            qry.append(qry[1])
                        
                        dx=float(qry[1])
                        dy=float(qry[2])
                        
                        new_c=c1.translate(dx,dy)                     # new-c is a tuple of (x,y,radius) returned by function
                        print(round(c1.B[0][0],2),round(c1.B[1][0],2),round(c1.rp,2),end=' ')
                        print()
                        for i in new_c:print(i,end=' ')               #printing new coordinates
                        
                        if v==1:
                            c1.plot()
                            
                    elif qry[0]=='S':
                        sr=float(qry[1])
                        new_c=c1.scale(sr)                         # new-c is a tuple of (x,y,radius) returned by function
                           
                        print(round(c1.B[0][0],2),round(c1.B[1][0],2),round(c1.rp,2),end=' ')
                        print()
                        for i in new_c:print(i,end=' ')             #printing new coordinates
                        
                        if v==1:
                            c1.plot()
                            
                    elif qry[0]=='R':
                        if len(qry)==2:
                            qry.extend(['0','0'])                   # appending 0 0 at the end if rotation point is not given
                        elif len(qry)==3:
                            qry.append(qry[2])
                            
                        do=float(qry[1])
                        rx=float(qry[2])
                        ry=float(qry[3])
                        
                        new_c=c1.rotate(do,rx,ry)                     # new-c is a tuple of (x,y,radius) returned by function
                        
                        print(round(c1.B[0][0],2),round(c1.B[1][0],2),round(c1.rp,2),end=' ')
                        print()
                        for i in new_c:print(i,end=' ')                  #printing new coordinates
                        
                        if v==1:
                            c1.plot()
                            
                    elif qry[0]=='P':                   # simply plot the circle
                        c1.plot()
                        
                            
                        
                        
                
                
                        
                        
                        
              
                    
                    
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
