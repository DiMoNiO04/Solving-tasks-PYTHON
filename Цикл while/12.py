n,k = map(int,input().split())     
i = 0                                             
time=0                                       
while time<=240-k and i<=n:  
    i+=1                                       
    time = time+(5*i)                
if i<n:                                       
    print(i) 
else:
    print(i-1)
