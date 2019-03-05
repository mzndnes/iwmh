import numpy as np
import fhand
import mapping
import timetak

'''News20','Artif1','Artif3','gisette','Artif5',
'Syn','Url','FordA','StarLightCurves','HandOutlines',
'webspam','CinCECGtorsotest','Leukemia']'''
indd=1
rfl=fhand.names[indd]
wfl=rfl+'accsim.txt'
fhand.wfl=wfl
dim=fhand.dm[indd]
fhand.dim=dim
mapping.dim=dim

print(rfl)
train=fhand.rtovec_sweight(rfl+'train.txt')
test=fhand.rtovec_sweight(rfl+'test.txt')

trinst=len(train)
tinst=len(test)




t=0
accsim=np.zeros(trinst,dtype=np.float)
for i in range(tinst):
    print('test num',i)
    for j in range(trinst):
        accsim[j]=mapping.gjs_fvec(test[i][1:],train[j][1:])
        t=t+timetak.tt
        #print('train number',j)
    fhand.wr_accsim(accsim)
    
print(t)


##accsim=fhand.rtoset_sweight(rfl+'accsim.txt')
##print(len(accsim))
##print(len(accsim[0]))
