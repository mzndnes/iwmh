import random
import numpy as np
import gc
import time
from operator import itemgetter
import timetak
import fhand
#import cws
import mapping
    
def main():
    
    '''['News20','Rcv','Realsim','gisette','kdda2010',
       'Syn','Url','FordA','StarLightCurves','HandOutlines',
       'webspam','CinCECGtorso','Leukemia']'''

    algo=['iwmh','wmh']
    indd=0
    bhash=8
    
    nhty=7
    mapping.nhty=nhty
    maxh=bhash*(2**(nhty-1)) 
    mapping.maxh=maxh #needed for random variables icws
    
    dim=fhand.dm[indd] 
    fhand.dim=dim #needed to read into vector
    mapping.dim=dim

    seed =np.zeros((maxh),dtype=np.int)
    for i in range(maxh):
        seed[i]=random.randint(1,10000)
    
    mapping.seed=seed
    mapping.setdimseed(seed,dim) #setting dim and seed
    
    wfl_cl='knn.txt'
    wfl_mse='mse.txt'
    fhand.wfl_cl=wfl_cl
    fhand.wfl_mse=wfl_mse
    rfl=fhand.names[indd]

    
    train=fhand.rtovec_sweight(rfl+'train.txt')
    test=fhand.rtovec_sweight(rfl+'test.txt')
    #print(train)
    #print(test)
    trinst=len(train)
    tinst=len(test)    

    tmap=mapping.mapp_fvec(train,test)   #time for mapping
    trhash=np.zeros((trinst,maxh), dtype=np.int64)
    thash=np.zeros((tinst,maxh), dtype=np.int64)
    
    #accsim=fhand.rtoset_sweight(rfl+'accsim.txt')
    for alg in range(len(algo)):
                
        hidx=0
        pretrtime=0
        prettime=0
        precltime=0
        preetime=0
        nhash=bhash
        
        saveFile=open(wfl_cl,'a')
        saveFile.write(rfl+' '+algo[alg]+'  \n')
        saveFile.close()

        saveFile=open(wfl_mse,'a')
        saveFile.write(rfl+' '+algo[alg]+'  \n')
        saveFile.close()
        
        preinter=np.zeros((nhty,tinst,trinst), dtype=np.int)
        hty=0
        nrep=1
        flg=0
        
        while hty<nhty:

            rerr_cl=np.empty(nrep, dtype=np.float)
            #rerr_mse=np.empty(nrep, dtype=np.float)
            rtrtime=np.empty(nrep, dtype=np.float)
            rttime=np.empty(nrep, dtype=np.float)
            rcltime=np.empty(nrep, dtype=np.float)
            retime=np.empty(nrep, dtype=np.float)
            mapping.chnh(nhash)
            rep=0
            
            while rep<nrep:
                trtime=0
                ttime=0          
                cltime=0
                etime=0
                
                for i in range(trinst):
                    mapping.wmhhash(trhash[i],train[i][1:],alg,hidx)
                    trtime=trtime+timetak.tt
                                                
                for i in range(tinst):
                    mapping.wmhhash(thash[i],test[i][1:],alg,hidx)
                    ttime=ttime+timetak.tt
                    
                
                estsim=np.zeros((tinst,trinst),dtype=np.float)
                pc=0
                pi=0
                tr_terr = []
                for i in range(tinst):
                    es=onnidx=0
                    for j in range(trinst):                       
                        curinter=mapping.egjs_num(thash[i][hidx:nhash],trhash[j][hidx:nhash])
                        etime=etime+timetak.tt
                        if hty==0:
                            estsim[i][j]=round(curinter/nhash,4)
                            preinter[hty][i][j]=curinter
                        else:
                            estsim[i][j]=round((preinter[hty-1][i][j]+curinter)/nhash,4)
                            preinter[hty][i][j]=preinter[hty-1][i][j]+curinter
                        #one NN
                        if estsim[i][j]>es:
                            onnidx=j
                            es=estsim[i][j]
                        #tr_terr.append((accsim[i][j]-estsim[i][j])**2)
                    start=time.time()
                     #number of incorrectly classified
                    if test[i][0]==train[onnidx][0]:# onnidx after checking all train            
                        pc=pc+1
                    else:
                        pi=pi+1
                    end=time.time()
                    cltime=end-start
                #avgerr = np.mean(tr_terr) 
                
                
                del estsim
                rtrtime[rep]=trtime
                rcltime[rep]=cltime
                rttime[rep]=ttime
                retime[rep]=etime
                rerr_cl[rep]=pi/tinst
                #rerr_mse[rep]=avgerr
                rep+=1
                
            if alg==1 and flg==0:
                rtrtime[0]=rtrtime[0]+tmap
                flg=1
                

            pretrtime+=np.mean(rtrtime)
            prettime+=np.mean(rttime)
            precltime=np.mean(rcltime)
            preetime+=np.mean(retime)
            
            
            fhand.knnwfl(np.mean(rerr_cl),pretrtime,prettime,preetime,precltime)
            #fhand.msewfl(np.mean(rerr_mse),pretrtime,prettime,preetime)
            
            
            hidx=nhash   
            nhash=nhash*2
            hty=hty+1
            
            print(hty)
            gc.collect()
    gc.collect()
    
#
if __name__== "__main__":
    main()
