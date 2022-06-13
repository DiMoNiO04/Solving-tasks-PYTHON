#number=int(input())
#sum=0
#while(delitel==number):
#    delitel+=1
 #   if number//delitel==0:
  #      sum=sum+delitel
#print(sum)

n=int(input())
sum=0
for i in range(n,0,-1):
    if n%i==0:
        sum+=i
print(sum)

