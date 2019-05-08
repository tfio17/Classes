#
#
# Animal main prg
#
#

#import anilib
from anilib import Animal, Cat, Dog

# Main

anilist = []

cat1 = Cat("Felix",50,"black")
print(cat1.getColor(), cat1.getName(), cat1.getaCount())
anilist.append(cat1)
cat2 = Cat("Rex",30,"orange")
print(cat2.getColor(), cat2.getName())
anilist.append(cat2)
dog1 = Dog("Fido",45,"red")
print(dog1.getColor(), dog1.getName(), dog1.getaCount())
anilist.append(dog1)

'''
del cat2
print("Animals left: ",Animal.aCount)
'''

print(cat1)
print(anilist)

for i in anilist:
    i.speak()
