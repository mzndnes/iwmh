import random
import numpy as np
import gc
import time
from operator import itemgetter
import timetak
import fhand
#import cws
import mapping
from scipy import stats
    
def main():
    
     '''['Gisette','FordA','StarLightCurves','HandOutlines',
       'Webspam','CinCECGtorso','Leukemia']'''

     algo=['iwmh','wmh']
     indd=5
     bhash=8
    
     nhty=7
     mapping.nhty=nhty
     maxh=bhash*(2**(nhty-1))
     mapping.maxh=maxh
     topk=[50,100,200,500]

     dim=fhand.dm[indd]
     mapping.dim=dim
     fhand.dim=dim

     seed =np.zeros((maxh),dtype=np.int)
     for i in range(maxh):
          seed[i]=random.randint(1,10000)

     mapping.seed=seed
     mapping.setdimseed(seed,dim)

     wfl_preci='preci.txt'
     wfl_t='topk.txt'
     wfl_map='map.txt'
     #wfl_tt='ttest.txt'
     fhand.wfl_preci=wfl_preci
     fhand.wfl_t=wfl_t
     fhand.wfl_map=wfl_map
     rfl=fhand.names[indd]


     train=fhand.rtovec_sweight(rfl+'train.txt')
     test=fhand.rtovec_sweight(rfl+'test.txt')
     

     mapping.train=train
     mapping.test=test
     
     trinst=len(train)
     tinst=len(test)

         
     tmap=mapping.mapp_fvec(train,test)
     
     trhash=np.zeros((trinst,maxh), dtype=np.int)
     thash=np.zeros((tinst,maxh), dtype=np.int)
     
     for alg in range(len(algo)):
          
          hidx=0
          pretrtime=0
          prettime=0
          pretptime=0
          preetime=0
          nhash=bhash
          
                
          saveFile=open(wfl_preci,'a')
          saveFile.write(rfl+' '+algo[alg]+'  \n')
          saveFile.close()
          
          saveFile=open(wfl_map,'a')
          saveFile.write(rfl+' '+algo[alg]+'  \n')
          saveFile.close()

          saveFile=open(wfl_t,'a')
          saveFile.write(rfl+' '+algo[alg]+'  \n')
          saveFile.close()
          
          preinter=np.zeros((nhty,tinst,trinst), dtype=np.int)
          hty=0
          nrep=1
          
          while hty<nhty:

               rmn_preci=np.empty((nrep,4), dtype=np.float)
               rmap=np.empty((nrep,4), dtype=np.float)
               rtrtime=np.empty(nrep, dtype=np.float)
               rttime=np.empty(nrep, dtype=np.float)
               rtptime=np.empty(nrep, dtype=np.float)
               retime=np.empty(nrep, dtype=np.float)
               rep=0
               mapping.hty=hty # only required for setreq
               mapping.chnh(nhash)
                              
               
               while rep<nrep:
                    trtime=0
                    tptime=0
                    ttime=0
                    etime=0
                    for i in range(trinst):
                         mapping.wmhhash(trhash[i],train[i][1:],alg,hidx)
                         trtime=trtime+timetak.tt
                         #print(99)
                     
                    for i in range(tinst):
                         #vec_t=mapping.sweight_vect(test[i][1:])
                         vec_t=test[i][1:]
                         mapping.wmhhash(thash[i],vec_t,alg,hidx)
                         ttime=ttime+timetak.tt
                         
                    estsim=np.zeros((tinst,trinst,2),dtype=np.float)
                    
                    for i in range(tinst):
                         for j in range(trinst):
                              
                              curinter=mapping.egjs_num(thash[i][hidx:nhash],trhash[j][hidx:nhash])
                              etime=etime+timetak.tt
                              estsim[i][j][0]=j
                              # find estsim
                              if hty==0:
                                   estsim[i][j][1]=round(curinter/nhash,4)
                                   preinter[hty][i][j]=curinter
                              else:
                                   estsim[i][j][1]=round((preinter[hty-1][i][j]+curinter)/nhash,4)
                                   preinter[hty][i][j]=preinter[hty-1][i][j]+curinter
                             
                    start=time.time()       
                    for i in range(tinst):
                         ff=sorted(estsim[i],key=itemgetter(1),reverse=True)
                         estsim[i]=ff
                    mapping.estsim=estsim
                    
                    #average precision
                    apreci=np.zeros((tinst,4),dtype=np.float)
                    #precision
                    preci=np.zeros((tinst,4),dtype=np.float)
        
                    for i in range(tinst):
                         for d in range(4):
                              preci[i][d],apreci[i][d]=mapping.cal_pnap(i,topk[d])
                    end=time.time()

                    
                    #mean precision
                    rmn_preci[rep]=np.mean(preci,axis=0)
                    #Mean average precision
                    rmap[rep]=np.mean(apreci,axis=0)
                    rtrtime[rep]=trtime
                    rtptime[rep]=end-start
                    rttime[rep]=ttime
                    retime[rep]=etime
                    rep+=1

               if alg==1 and hty==0:
                    rtrtime[0]=rtrtime[0]+tmap
                
               fhand.wr_preci(np.mean(rmn_preci,axis=0))
               fhand.wr_map(np.mean(rmap,axis=0))
                         
               pretrtime+=np.mean(rtrtime)
               pretptime=np.mean(rtptime)
               prettime+=np.mean(rttime)
               preetime+=np.mean(retime)

               
               fhand.wr_tim(pretrtime,prettime,preetime,pretptime)

               hidx=nhash   
               nhash=nhash*2
               hty=hty+1
               print(hty)
               gc.collect()
    
     gc.collect()
    
    
if __name__== "__main__":
    main() 
