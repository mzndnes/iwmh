import numpy as np
import time
import cws
import timetak
import random

def mapp_fvec(train,test):
    #print(dim)
    #print(len(train[0]))
    
    
    trinst=len(train)
    tinst=len(test)
    
    start=time.time() 
    maxi=np.zeros(dim,dtype=np.float)
    
    for i in range(tinst):
        inte=test[i][1:]
        for j in range(dim):
            maxi[j]=max(maxi[j],inte[j])
            
    for i in range(trinst):
        inte=train[i][1:]
        for j in range(dim):
            maxi[j]=max(maxi[j],inte[j])
            
            
    #print(maxi)
    for i in range(len(maxi)):
        if maxi[i]<=0:
            maxi[i]=1
        
    
    maxx=np.ceil(maxi)
    R=0
    rr=np.zeros(len(maxi)+1,dtype=np.int)
    
    for i in range(len(maxi)):
        rr[i]=R
        R=R+maxx[i]

    
    
    rr[i+1]=R
    #print(maxx)
    #print(r)
    #print(R)
    cws.R=R
    
    m=np.zeros(int(R),dtype=np.int)
    for i in range(len(rr)-1):
        for j in range(rr[i],rr[i+1]):
            m[j]=i
    #m[j]=i
    #print(m)
    #input()
    cws.m=m
    cws.rr=rr

    end=time.time()
    
    return end-start

def mapp_fset(train,test):
    #print(dim)
    #print(len(train[0]))
    
    
    trinst=len(train)
    tinst=len(test)
    
    start=time.time() 
    maxi=np.zeros(dim,dtype=np.float)
    for i in range(tinst):
        j=1
        while j<len(test[i][1:]):
            indx=int(test[i][j])
            maxi[indx]=max(maxi[indx],test[i][j+1])
            j=j+2
            
    for i in range(trinst):
        j=1
        while j<len(train[i][1:]):
            indx=int(train[i][j])
            maxi[indx]=max(maxi[indx],train[i][j+1])
            j=j+2

    maxx=np.ceil(maxi)
    
    #print(maxi)
    for i in range(len(maxi)):
        if maxx[i]<=0:
            maxx[i]=1

    R=0
    rr=np.zeros(len(maxi)+1,dtype=np.int)
    
    for i in range(len(maxi)):
        rr[i]=R
        R=R+maxx[i]
        
    rr[i+1]=R
    #print(maxx)
    #print(r)
    #print(R)
    cws.R=R
    
    m=np.zeros(int(R),dtype=np.int)
    for i in range(len(rr)-1):
        for j in range(rr[i],rr[i+1]):
            m[j]=i
    #m[j]=i
    #print(m)
    #input()
    cws.m=m
    cws.rr=rr
    
    end=time.time()
    
    return end-start

def genrand(nhash):
    alg=2
    r1 =np.zeros((maxh,dim),dtype=np.float)
    r2=np.zeros((maxh,dim),dtype=np.float)
    r=np.zeros((maxh,dim),dtype=np.float)
    c1=np.zeros((maxh,dim),dtype=np.float)
    c2=np.zeros((maxh,dim),dtype=np.float)
    c=np.zeros((maxh,dim),dtype=np.float)
    b =np.zeros((maxh,dim),dtype=np.float)
    alg_ttak=np.zeros((alg,nhty),dtype=np.float)
    
    i=0
    for j in range(nhty):
        while i<nhash:
            generator = np.random.RandomState(seed[i])
            start=time.time()
            r1[i] = generator.uniform(0, 1, dim).astype(np.float)
            r2[i] = generator.uniform(0, 1, dim).astype(np.float)
            c1[i] = generator.uniform(0, 1, dim).astype(np.float)
            b[i] = generator.uniform(0, 1, dim).astype(np.float)
            r[i]=r1[i]*r2[i]
            end=time.time()
            c_all=end-start
            
            start=time.time()
            c2[i] = generator.uniform(0, 1, dim).astype(np.float)
            c[i]=c1[i]*c2[i]
            end=time.time()
            o_i=end-start
            
            alg_ttak[0][j]+=c_all
            alg_ttak[1][j]+=o_i+c_all
            #print(alg_ttak[1])
            #input()
            i=i+1
        nhash=nhash*2
        
        
    #print(alg_ttak[0])
    #print(alg_ttak[1])
    for j in range(1,nhty):
        alg_ttak[0][j]+=alg_ttak[0][j-1]
        alg_ttak[1][j]+=alg_ttak[1][j-1]
    #print(alg_ttak[0])
    #print(alg_ttak[1])

    
        
    cws.r=r
    cws.b=b
    cws.c=c
    cws.c1=c1
    cws.r1=r1
    
    return alg_ttak

def chnh(nh):
    cws.nhash=nh
    


def sweight_vect(v):
    hash1=np.zeros(dim, dtype=np.float)
    i=0
    while i<len(v):
        idx=int(v[i])
        hash1[idx]=v[i+1]
        i=i+2
    #print("hi")
    #print(hash1[366])
    return hash1

    
def egjs_list(v1,v2):
    start=time.time()
    intersection=0
    for k in range(len(v1)):
        if v1[k][0]==v2[k][0] and v1[k][1]==v2[k][1]:
            intersection += 1
            
    end=time.time()
    timetak.tt=end-start
    #print(intersection/len(v1))
    return intersection


def egjs_num(v1,v2):
    start=time.time()
    intersection=0
    for k in range(len(v1)):
        if v1[k]==v2[k]:
            intersection += 1
            
    end=time.time()
    timetak.tt=end-start
    return intersection

def cal_pnap(k,topk):
    start=time.time()   
    tp=0
    fp=0
    c_preci=0
    
    for i in range(topk):
        
        nnb=int(estsim[k][i][0])
        
        #input()
        if test[k][0]==train[nnb][0]:
            tp=tp+1
            c_preci+=tp/(tp+fp)
        else:
            fp=fp+1

    preci=tp/(fp+tp)
    
    end=time.time()
    timetak.tt=end-start   
    if tp==0:
        return preci,0
    else:
        return preci,c_preci/tp
    
def setdimseed(seed,dim):
    cws.seed=seed
    cws.dim=dim
    
def selhash(hs,v,ic,hidx):
    if ic==0:
        cws.pcws_set(hs,v,hidx)
    else:
        cws.icws_set(hs,v, hidx)
    
def wmhhash(hs,v,ic,hidx):
    if ic==0:
        cws.iwmh(hs,v,hidx)
    else:
        cws.wmh(hs,v,hidx)

if __name__== "__main__":
    main()  

