x = map(int, (input().split()))              
n = list(map(int, input().split()))       
m = list(map(int, input().split()))      
s = n + m                                               
f = []                                                       
while len(s) != 0:                                   
    a = min(s)                                         
    f.append(a)                                       
    a = s.index(a)                                   
    del s[a]                                         
print(*f) 
