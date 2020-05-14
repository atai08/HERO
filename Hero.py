
import random
class Parent: 
    def __init__(self, n,team):
        self.n=n
        self.team=team
class heroes(Parent):
    def __init__(self,name,n,team,level=0):
        self.name=name
        self.level = level
        self.team=team
    def level_up(self, incr):
        self.level+=incr
 
class soldier(Parent): 
    def follow_heroes(self,heroes):
        print("\n"+"The hero {} has chosen soldier number {} to assist him in the night Watch.".format(heroes.name, self.n))
Manas,Chinghizkhan = heroes("Manas",1,"kyrgyz"),heroes("Chinghizkhan",2,"mongol") 
kyrgyz=[] 
mongol=[]
quantity=int(input("Количество воинов:"))+1 
for i in range(1,quantity):
    t=random.randint(0,1)
    i=soldier(i,t)
    if i.team==0:
        kyrgyz.append(i)
        i.team="kyrgyz"
    else:
        mongol.append(i)
        i.team="mongol"
if len(kyrgyz)>len(mongol): 
    Manas.level_up(1)
elif len(kyrgyz)<len(mongol):
    Chinghizkhan.level_up(1)

 
# выводим на экран списки команд
print("In army of ",Manas.name+", with the level ",str(Manas.level)+", there are ",len(kyrgyz),"mighty warriors!")
for i in kyrgyz:
    print(i.n, i.team, end=", ")
print("\n"+"In army of ",Chinghizkhan.name+", with the level ",str(Chinghizkhan.level)+", there are ",len(mongol),"mighty warriors!")
for i in mongol:
    print(i.n,i.team, end=", ")
#выводим случайное имя героя и номер одного из солдат
who=random.randint(0,1)
if who==1:
    t=kyrgyz
    h=Manas
else:
    t=mongol
    h=Chinghizkhan
random.choice(t).follow_heroes(h)

