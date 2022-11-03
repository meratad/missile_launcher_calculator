#1 additional USSR Ballistic Missile above 200: +2
#1 additional US Ballistic Missile above 0: -2
#1 additional US Cruise Missile above 100: -1

a = int(input ("USA Ballistic: "))
b = int(input ("USA Cruise: "))
c = int(input ("USSR Ballistic: "))

#USA Ballistic for points
if a >= 0:
    x = a*(-2)
else:
    x = 0

#USA Cruise for points
if b >= 100:
    y = (b-100)*(-1)
else:
    y = 0

#USSR Ballistic for points
if c >= 200:
    z = (c-200)*(2)
else:
    z = 0

#USA Ballistic for missiles
u = a*1

#USA Cruise for missiles
p = b*4

#USSR Ballistic for missiles
r = c*3


print ("Total point for USSR is:", x+y+z)
print("Total possible targets the USA can hit is:", u+p)
print("Total possible targets the USSR can hit is:", r)