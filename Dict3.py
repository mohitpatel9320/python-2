d1={"A":10,"B":20,"C":30}
d2={"A":60,"B":70,"C":80}
d3={}
for i in d1:
   if i in d2:
       d3[i]=d1[i]+d2[i]
print(d3)





