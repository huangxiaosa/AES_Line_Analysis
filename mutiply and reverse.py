import androidhelper
import time
import time
from numpy import *
app = androidhelper.Android()

def multi(a,b):

    TimeBegin = time.time()*1000
    
    c = int_(random.random(size=100000)*254)+1;
    d = int_(random.random(size=100000)*254)+1;

    e = b[c]
    f = b[d]

    g = int_(e+f)
    result = a[g]
    #for i in range(100000):
     #   result = a[e[i]+f[i]]
    #result = a[b[c]+b[d]]

    TimeEnd = time.time()*1000

    return TimeEnd-TimeBegin
    
def inverse(a,b):

    TimeBegin = time.time()*1000
    c = int_(random.random(size=100000)*254)+1;
    e = int_(254-b[c])
    result = a[e]
    TimeEnd = time.time()*1000

    return TimeEnd - TimeBegin

if __name__ == '__main__':
    a = zeros(510)
    b = zeros(256)
    
    filename = "table.txt"
    f = open(filename,"r")
    for line in f:
        l,r = line.split()        
        l = int(l)
        r = int(r,2)        
        a[l] = r
        a[l+255] = r
        b[r] = l

    app.dialogCreateAlert('GF calculate')
    app.dialogSetPositiveButtonText('multy')
    app.dialogSetNegativeButtonText('inverse')
    app.dialogShow()
    resp=app.dialogGetResponse().result
while 1:
  if resp['which'] in ('positive'):
    app.dialogCreateAlert('The multy time is: /ms',str(multi(a,b)))
    app.dialogSetPositiveButtonText('return')
  #  app.dialogSetNegativeButtonText('quit')
    app.dialogShow()
    resp=app.dialogGetResponse().result
    if resp['which'] in ('positive'):
      app.dialogCreateAlert('GF calculate')
      app.dialogSetPositiveButtonText('multy')
      app.dialogSetNegativeButtonText('inverse')
      app.dialogShow()
      resp=app.dialogGetResponse().result
  
  
  else:
    app.dialogCreateAlert('The inverse time is: /ms',str(inverse(a,b)))
    app.dialogSetPositiveButtonText('return')
  #  app.dialogSetNegativeButtonText('quit')
    app.dialogShow()
    resp=app.dialogGetResponse().result
    if resp['which'] in ('positive'):
      app.dialogCreateAlert('GF calculate')
      app.dialogSetPositiveButtonText('multy')
      app.dialogSetNegativeButtonText('inverse')
      app.dialogShow()
      resp=app.dialogGetResponse().result
  
