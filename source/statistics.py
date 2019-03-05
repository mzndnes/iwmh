import random
import numpy as np
import gc
import time
from operator import itemgetter
import fhand
import timetak

def mapp_fset(train,test,dim):
    #print(dim)
    #print(len(train[0]))
    
    
    trinst=len(train)
    tinst=len(test)
    
    start=time.time() 
    maxi=np.zeros(dim,dtype=np.float)
    
    trps=np.zeros(trinst,dtype=np.float)
    tps=np.zeros(tinst,dtype=np.float)
    
    for i in range(tinst):
        j=1
        g=0
        while j<len(test[i][1:]):
            indx=int(test[i][j])
            maxi[indx]=max(maxi[indx],test[i][j+1])
            g+=test[i][j+1]
            j=j+2
        tps[i]=g
        
    for i in range(trinst):
        j=1
        g=0
        while j<len(train[i][1:]):
            indx=int(train[i][j])
            maxi[indx]=max(maxi[indx],train[i][j+1])
            g+=train[i][j+1]
            j=j+2
        trps[i]=g

    
    maxx=np.ceil(maxi)
    
    #print(maxi)
    for i in range(len(maxi)):
        if maxx[i]<=0:
            maxx[i]=1
        
    trg=sum(maxx)
    
    trps/=trg
    tps/=trg    
    
    mntr=np.mean(trps)
    mnt=np.mean(tps)
    mn=(mntr+mnt)/2
    return mn

def cal_avwei(train,test,dim):
    trinst=len(train)
    tinst=len(test)
    
    w=0    
    for i in range(tinst):
        j=1
        while j<len(test[i][1:]):
            w+=test[i][j+1]
            j=j+2
        
    for i in range(trinst):
        j=1
        while j<len(train[i][1:]):
            w+=train[i][j+1]
            j=j+2
    return w

    
def main():
    '''['News20','Rcv','Realsim','gisette','kdda2010',
       'Syn','Url','FordA','StarLightCurves','HandOutlines',
       'webspam','CinCECGtorso','Leukemia']'''
    
    indd=3
    
    fl=fhand.names[indd]
    dim=fhand.dm[indd]
    fhand.dim=dim
    
    #train=fhand.rtovec_sweight(fl+'train.txt')
    #test=fhand.rtovec_sweight(fl+'test.txt')

    train=fhand.rtoset_sweight(fl+'train.txt')
    test=fhand.rtoset_sweight(fl+'test.txt')
    
    trinst=len(train)
    tinst=len(test)

    trnz=0
    for i in range(trinst):
        trnz+=len(train[i][1:])/2

    tnz=0
    for i in range(tinst):
        tnz+=len(test[i][1:])/2

    tnz=trnz+tnz
    densi=tnz/((trinst+tinst)*dim)
    print('Sparsity=',1-densi)
    print('density=',densi)
    print('average weight=',cal_avwei(train,test,dim)/tnz)
    #print(mapp_fset(train,test,dim))

    
##    trvar=np.var(train,axis=0)
##    atrvar=np.mean(trvar)
##    tvar=np.var(test,axis=0)
##    atvar=np.mean(tvar)
##    mndata=(atrvar+atvar)/2
##    print('mean var',mndata)

    
     
        
if __name__== "__main__":
    main()  

