d={232:"Rakshit",878:"Rahul",908:"Vraj",767:"Mohit"}

print(d)
print(d[878])
print(d.get(908))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(232))
print(d)
d.popitem()
print(d)
d1={123:"Mohit",455:"Rakshit"}
d.update(d1)
print(d)
d[111]="Jigar"
print(d)

for i in d:
    print(i," : ",d[i])
