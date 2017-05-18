def topK(arrlist, k):    
    a=[]    
    b=dict()   
    c=[]    
    for i in range(0,len(arrlist)):        
       if(arrlist[i] not in a):           
          a.append(arrlist[i])           
          b[arrlist[i]]=1        
       else:           
          b[arrlist[i]]+=1    
    d = sorted(b.items(), key=lambda x : x[1], reverse=True)    
    for i in d:    
        c.append(i[0])    
    return c[0:k]



topK([1,1,1,2,2,3], 2)
