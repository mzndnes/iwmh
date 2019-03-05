import numpy as np
import csv
import os,sys

def rtovec_sweight(rfl):
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'setweight',rfl)
    csvf=open(tarpath,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    
    data=[]
    c=0
    for row in csvRD:
        instt=np.zeros(dim+1,dtype=np.float)
        flg=0
        for col in row:
            if flg==0:
                instt[0]=float(col) #put class
                flg=1
            elif flg==1:
                f=float(col)
                indx=int(f) #read index
                flg=2
                
            elif flg==2:
                if indx==dim:
                    print(indx)
                instt[indx+1]=float(col) #put weight
                flg=1
            
        data.append(instt)
        #print(intdata)
        #input()
        
        
        del instt
        
##        c=c+1
##        if c==1:
##            break
        
    
    return data
    csvf.close()

def rtoset_sweight(rfl): #reads weight as the set
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'setweight',rfl)
    csvf=open(tarpath,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    data=[]
    for row in csvRD:
        intdata=[]
        
        for col in row:
            f=float(col)
            intdata.append(f)
            
        data.append(intdata)
        break
    return data
    csvf.close()




    
def knnwfl(errr,trtime,ttime,etime,cltime):
    saveFile=open(wfl_cl,'a')
    saveFile.write(str(errr)+',')
    saveFile.write(str(trtime)+',')
    saveFile.write(str(ttime)+',')
    saveFile.write(str(etime)+',')
    saveFile.write(str(cltime)+'\n')
    saveFile.close()
    
def wr_preci(preci):
    saveFile=open(wfl_preci,'a')
    for i in range(len(preci)):
        if i==len(preci)-1:
            saveFile.write(str(preci[i])+'\n')
        else:
            saveFile.write(str(preci[i])+',')
    saveFile.close()

def wr_map(mapp):
    saveFile=open(wfl_map,'a')
    for i in range(len(mapp)):
        if i==len(mapp)-1:
            saveFile.write(str(mapp[i])+'\n')
        else:
            saveFile.write(str(mapp[i])+',')
    saveFile.close()
    
    
def wr_tim(trtime,ttime,etime,tptime):
    saveFile=open(wfl_t,'a')   
    saveFile.write(str(trtime)+',')
    saveFile.write(str(ttime)+',')
    saveFile.write(str(etime)+',')
    saveFile.write(str(tptime)+'\n')
    saveFile.close()


        


names=['News20','Rcv','Realsim','gisette','kdda2010',
       'Syn','Url','FordA','StarLightCurves','HandOutlines',
       'Webspam','CinCECGtorso','Leukemia']
dm=[541956,34464,18517,5000,86293,
    8,66436,500,1024,2709,
    309277,1639,7129]

