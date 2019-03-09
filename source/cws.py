import numpy as np
import time
import timetak
import math

def pcws_set(hs,st,hidx):
    start=time.time()
    for i in range(hidx,nhash):
        amax=math.inf
        j=0
        while j<len(st):
            p=int(st[j])
            
            t= np.floor((np.log(st[j+1])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
            y= np.exp((t - b[i][p]) * -np.log(r[i][p]))
            aint= -np.log(c1[i][p])*r1[i][p]/y
            if aint<amax:
                amax=aint
                hs[i][0]=p
                hs[i][1]=int(y)
            j+=2
        
    end=time.time()
    timetak.tt=end-start
    #print(timetak.tt)

def icws_set(hs,st,hidx):
    
    start=time.time()
    for i in range(hidx,nhash):
        amax=math.inf
        j=0
        while j<len(st):
            p=int(st[j])
            t= np.floor((np.log(st[j+1])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
            y= np.exp((t - b[i][p]) * -np.log(r[i][p]))
            aint= -np.log(c[i][p])*r[i][p]/y
            if aint<amax:
                amax=aint
                hs[i][0]=p
                hs[i][1]=int(y)
            j+=2
        
    end=time.time()
    timetak.tt=end-start
    #print(timetak.tt)
    
def icws(hs,v,hidx):
    start=time.time()
    for i in range(hidx,nhash):
        a = np.zeros(dim, dtype=np.float)
        y = np.zeros(dim, dtype=np.float)
        
        for p in range(dim):
            if v[p]>0:             
                t= np.floor((np.log(v[p])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
                y[p]= np.exp((t - b[i][p]) * -np.log(r[i][p]))
                a[p]= -np.log(c[i][p])*r[i][p]/y[p]
                #print(t)
            else:
                a[p]=math.inf
        k = np.nanargmin(a)
        hs[i][0]=k
        hs[i][1]=int(y[k])
    end=time.time()
    timetak.tt=end-start
    
    

def pcws(hs,v,hidx):
    
    start=time.time()
    for i in range(hidx,nhash):
        a = np.zeros(dim, dtype=np.float)
        y = np.zeros(dim, dtype=np.float)
        for p in range(dim):
            if v[p]>0: 
                t= np.floor((np.log(v[p])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
                y[p]= np.exp((t - b[i][p]) * -np.log(r[i][p]))
                a[p]= -np.log(c1[i][p])*r1[i][p]/y[p]
            else:
                a[p]=math.inf
        k = np.nanargmin(a)
        hs[i][0]=k
        hs[i][1]=int(y[k])
    end=time.time()
    timetak.tt=end-start
    return hs    
    
def wmh(hs, v,hidx):
    
    start=time.time()
    for i in range(hidx,nhash):
        
        mn=0
        generator = np.random.RandomState(seed[i])
        while True:       
            u1= generator.uniform(0, R, 1).astype(np.float)
            indx=int(np.floor(u1))
            
            indx1=m[indx]
            if u1[0]<=rr[indx1]+v[indx1]:
                break
            
            mn+=1
        hs[i]=mn
    end=time.time()
    timetak.tt=end-start
    
  


def iwmh(hs,v,hidx):
    #vec=vectoriz(v)
    start=time.time()
    for i in range(hidx,nhash):
        generator = np.random.RandomState(seed[i])
        generator2 = np.random.RandomState(seed[i])
        
        mn=0
        #print(seed)
        
        while(True):
            u = generator.random_integers(0,dim-1, 1 )
            if v[u[0]]>0:
                b= generator2.uniform(0, 1, 1).astype(np.float)
                norvec=v[u[0]]/(v[u[0]]+b[0])
                #norvec=v[u[0]]/(v[u[0]]+0.99)
                u1= generator2.uniform(0, 1, 1).astype(np.float)
                if u1[0]<=norvec:
                    break
            
            mn=mn+1
        hs[i]=mn
    end=time.time()
    timetak.tt=end-start
    
     
        
if __name__== "__main__":
    
    main()    
